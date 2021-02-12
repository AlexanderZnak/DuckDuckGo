import json
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


@pytest.fixture
def browser(config):
    if config["browser"] == "Chrome":
        driver = webdriver.Chrome(executable_path="resources/chromedriver.exe")
    elif config["browser"] == "Headless Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome(executable_path="resources/chromedriver.exe", options=options)
    else:
        raise WebDriverException(f'Browser "{config["browser"]} is not supported"')

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def config():
    with open("config.json") as config_file:
        config = json.load(config_file)

        assert config["browser"] in ["Headless Chrome", "Chrome"]

        return config


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def screenshot(request, browser):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            method_name: str = request.node.nodeid
            part_of_method_name = method_name.split(":test_")[1]
            print("executing test failed", method_name)
            browser.get_screenshot_as_file(
                f"screenshots/{part_of_method_name}_{datetime.today().strftime('%Y-%m-%d')}.png")
