from BasePage import BasePage
from SearchResultsPage import SearchResultsPage


class MainPage(BasePage):
    sign_in_button = "id:nav-link-accountList"
    account_line = "css:[data-nav-role='signin']"
    search_field = "id:twotabsearchtextbox"
    search_button = "id:nav-search-submit-button"

    def click_on_sign_in_button(self):
        self.sl().click_element(self.sign_in_button)

    def user_should_be_logged_in(self, name):
        self.sl().wait_until_element_contains(self.account_line, f"Hello, {name}")

    def type_in_search_field(self, text):
        self.sl().wait_until_element_is_visible(self.search_field)
        self.sl().input_text(self.search_field, text)
        self.sl().click_element(self.search_button)
        self.sl().wait_until_element_is_visible(SearchResultsPage.item_title)
