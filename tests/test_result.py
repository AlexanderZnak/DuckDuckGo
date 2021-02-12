import pytest

from pages.result_page import ResultPage
from pages.search_page import SearchPage


@pytest.mark.flaky(reruns=3, reruns_delay=2)
@pytest.mark.parametrize("phrase", ["Panda", "Python", "Java"])
def test_result_page_should_be_opened_with_exact_request(browser, phrase, screenshot):
    search_page = SearchPage(browser)
    result_page = ResultPage(browser)

    # Arrange
    search_page.open_page()

    # Act
    search_page \
        .fill_in_search_field(phrase) \
        .click_search_button()

    # Assert
    assert phrase in result_page.get_title()
    for title_link in result_page.get_all_links_values():
        assert phrase.lower() in title_link.lower()


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_more_results_should_be_appeared_after_click_by_button_more_results(browser, screenshot):
    search_page = SearchPage(browser)
    result_page = ResultPage(browser)
    phrase = "Panda"

    # Arrange
    search_page \
        .open_page() \
        .fill_in_search_field(phrase) \
        .click_search_button()

    default_numbers_of_results = len(result_page.get_all_links_values())

    # Act
    result_page.click_more_results_button()

    increased_numbers_of_results = len(result_page.get_all_links_values())

    # Assert
    assert default_numbers_of_results < increased_numbers_of_results, "'More results' button should be appeared more " \
                                                                      "results "


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_after_click_by_result_link_selected_page_should_be_opened(browser, screenshot):
    search_page = SearchPage(browser)
    result_page = ResultPage(browser)
    phrase = "Panda"

    # Arrange
    search_page \
        .open_page() \
        .fill_in_search_field(phrase) \
        .click_search_button()

    # Act
    link = result_page.get_random_link()
    result_page.click_by_result_link(link)

    # Assert
    link_text = link.text
    title_text = result_page.get_title()
    assert link_text in title_text, "New page should be opened"


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_after_search_text_changing_new_phrase_should_be_searched(browser, screenshot):
    search_page = SearchPage(browser)
    result_page = ResultPage(browser)
    phrase = "Panda"
    new_phrase = "Python"

    # Arrange
    search_page \
        .open_page() \
        .fill_in_search_field(phrase) \
        .click_search_button()

    # Act
    result_page \
        .clear_search_input() \
        .fill_in_search_field_new_search_text(new_phrase) \
        .click_search_button()

    # Assert
    assert new_phrase in result_page.get_title(), "New phrase should be searched"
    for title_link in result_page.get_all_links_values():
        assert new_phrase.lower() in title_link.lower(), "Part of new phrase should be contained into title of links"


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_image_results_should_be_appeared_after_switching_by_click_reference_images(browser, screenshot):
    search_page = SearchPage(browser)
    result_page = ResultPage(browser)
    phrase = "Panda"
    image_reference = "Images"
    img_attr = "img"

    # Arrange
    search_page \
        .open_page() \
        .fill_in_search_field(phrase) \
        .click_search_button()

    # Act
    result_page.click_to_switch_results_items_by(image_reference)

    # Assert
    list_of_images_attr_names = result_page.get_all_img_attr()
    assert result_page.is_item_bar_active(image_reference) is True, "Images reference should be active"
    for image_attr_name in list_of_images_attr_names:
        assert img_attr in image_attr_name, "Attribute img should be into each links according to image searching"


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_video_results_should_be_appeared_after_switching_by_click_reference_videos(browser, screenshot):
    search_page = SearchPage(browser)
    result_page = ResultPage(browser)
    phrase = "Panda"
    videos_reference = "Videos"

    # Arrange
    search_page \
        .open_page() \
        .fill_in_search_field(phrase) \
        .click_search_button()

    # Act
    result_page.click_to_switch_results_items_by(videos_reference)

    # Assert
    assert result_page.is_item_bar_active(videos_reference) is True, "Videos reference should be active"


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_news_results_should_be_appeared_after_switching_by_click_reference_news(browser, screenshot):
    search_page = SearchPage(browser)
    result_page = ResultPage(browser)
    phrase = "Panda"
    news_reference = "News"

    # Arrange
    search_page \
        .open_page() \
        .fill_in_search_field(phrase) \
        .click_search_button()

    # Act
    result_page.click_to_switch_results_items_by(news_reference)

    # Assert
    assert result_page.is_item_bar_active(news_reference) is True, "News reference should be active"


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_after_click_by_all_regions_dropdown_with_regions_should_be_appeared(browser, screenshot):
    search_page = SearchPage(browser)
    result_page = ResultPage(browser)
    phrase = "Panda"
    region = "Australia"

    # Arrange
    search_page \
        .open_page() \
        .fill_in_search_field(phrase) \
        .click_search_button()

    # Act
    result_page \
        .click_by_all_regions() \
        .select_particular_region(region)

    # Assert
    assert result_page.is_region_selected(region) is True, f"Region: {region} should be selected"
    assert result_page.is_switcher_enabled() is True, "Switcher should be auto enabled, when region is selected"


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_links_should_be_opened_in_new_tab_after_changing_settings_open_links_in_new_tab(browser, screenshot):
    search_page = SearchPage(browser)
    result_page = ResultPage(browser)
    phrase = "Panda"
    new_tab_switcher = "Open Links in a New Tab"
    # Arrange
    search_page \
        .open_page() \
        .fill_in_search_field(phrase) \
        .click_search_button()

    # Act
    result_page \
        .click_by_settings() \
        .click_by_switcher(new_tab_switcher)

    # Assert
    random_link = result_page.get_random_link()
    result_page.click_by_result_link(random_link)
    assert len(result_page.driver.window_handles) == 2, "Two tabs should be opened"


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_scrolling_should_be_infinite_by_autoloading_results_after_changing_settings_infinite_scroll(browser,
                                                                                                     screenshot):
    search_page = SearchPage(browser)
    result_page = ResultPage(browser)
    phrase = "Panda"
    infinite_scroll_switcher = "Infinite Scroll"

    # Arrange
    search_page \
        .open_page() \
        .fill_in_search_field(phrase) \
        .click_search_button()
    amount_of_links_before_changes = len(result_page.get_all_links())

    # Act
    result_page \
        .click_by_settings() \
        .click_by_switcher(infinite_scroll_switcher)

    # Assert
    amount_of_links_after_changes = len(result_page.do_scrolling_down().get_all_links())
    assert amount_of_links_after_changes > amount_of_links_before_changes, "Amount of result links should be far more"
