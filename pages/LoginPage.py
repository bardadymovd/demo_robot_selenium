import time

from BasePage import BasePage


class LoginPage(BasePage):
    login_field = "id:ap_email"
    continue_button = "id:continue"
    password_field = "id:ap_password"
    sign_in_button = "id:signInSubmit"

    def input_login_and_proceed(self, login):
        self.sl().input_text(self.login_field, login)
        self.sl().click_element(self.continue_button)

    def input_password_and_proceed(self, password):
        time.sleep(3)  # wait for bypass captcha
        self.sl().input_text(self.password_field, password)
        self.sl().click_element(self.sign_in_button)
