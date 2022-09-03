from selenium.webdriver.remote.webelement import WebElement

from BasePage import BasePage


class SearchResultsPage(BasePage):
    price_filter = "id:priceRefinements"
    item = "css:.s-result-item"
    item_price = f"{item} .a-price-whole"
    item_title = f"{item} .s-card-container"
    brand_filter = "css:#brandsRefinements"

    def filter_results_by_price(self, text):
        self.sl().click_element(f"{self.price_filter} >> xpath://*[contains(text(),'{text}')]")

    def price_of_fist_item_should_be_between(self, min_price: int, max_price: int):
        element: WebElement = self.sl().find_element(self.item_price)
        assert min_price < int(element.text) < max_price, "price of item is not in expected range"

    def filter_results_by_brand(self, brand):
        self.sl().click_element(f"{self.brand_filter} [aria-label='{brand}'] .a-icon-checkbox")
        self.sl().checkbox_should_be_selected(f"{self.brand_filter} [aria-label='{brand}'] input")

    def title_of_first_item_should_contain(self, text):
        self.sl().wait_until_element_is_visible(self.item_title)
        self.sl().element_should_contain(self.item_title, text, ignore_case=True)
