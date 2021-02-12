import time

import pytest

from pages.result_page import ResultPage
from pages.search_page import SearchPage


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_search_page_should_be_opened(browser, screenshot):
    # Arrange
    search_page = SearchPage(browser)
    name_of_site = "DuckDuckGo"

    # Act
    search_page.open_page()

    # Assert
    assert name_of_site in search_page.get_title(), f"{name_of_site} should be opened"


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_auto_complete_should_be_appeared_pertain_search_text(browser, screenshot):
    search_page = SearchPage(browser)
    phrase = "Panda"

    # Arrange
    search_page.open_page()

    # Act
    search_page.fill_in_search_field(phrase)
    time.sleep(2)

    # Assert
    list_of_suggestions_values = search_page.get_all_values_of_suggestions_pertain_search_text()
    assert len(list_of_suggestions_values) > 0, "Search engine should suggest a variants"
    for pertain_search_text in list_of_suggestions_values:
        assert phrase.lower() in pertain_search_text.lower(), "Suggested variant should contain pertain search text"


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_after_click_by_auto_complete_suggestion_request_should_be_equal(browser, screenshot):
    search_page = SearchPage(browser)
    result_page = ResultPage(browser)
    phrase = "Panda"

    # Arrange
    search_page.open_page()

    # Act
    suggestion = search_page \
        .fill_in_search_field(phrase) \
        .get_random_suggestion()
    text_of_suggestion = suggestion.text
    search_page.click_by_auto_complete_suggestion(suggestion)

    # Assert
    text_of_actual_search = result_page.get_search_value()
    assert text_of_suggestion in text_of_actual_search, "Suggested variant should be showed accordingly"
