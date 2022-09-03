from SeleniumLibrary import SeleniumLibrary
from robot.libraries.BuiltIn import BuiltIn

from webdriver_manager.chrome import ChromeDriverManager


class BasePage:

    @staticmethod
    def get_chromedriver_path():
        return ChromeDriverManager().install()

    @staticmethod
    def sl() -> SeleniumLibrary:
        return BuiltIn().get_library_instance("SeleniumLibrary")

    def custom_open_browser(self):
        self.sl().open_browser(None, browser="Chrome", executable_path=self.get_chromedriver_path())
        self.sl().set_selenium_implicit_wait("15 seconds")
