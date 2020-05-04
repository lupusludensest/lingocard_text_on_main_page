from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):

    # locators
    TEXT_HERE = (By.XPATH, "//h1[@class='header-title flex-container content-center text-center lang']")
    CLICK_HAMBURGER = (By.CSS_SELECTOR, ".menu-link")
    ELEVEN_ITEMS_HERE = (By.CSS_SELECTOR, "#menu li a")
    F_NAME = (By.NAME, "name")
    L_NAME = (By.NAME, "lastName")
    E_MAIL = (By.NAME, "email")
    TEXT_FIELD = (By.NAME, "text")
    SEND_BTN = (By.CSS_SELECTOR, "button.btn.btn-white.form-btn")
    TEXT_FIELD_W_TEXT = (By. XPATH, "//textarea[@placeholder='Your message']")

    def verify_text_here(self, text):
        """
        Text is here
        """
        self.verify_text(text, *self.TEXT_HERE)

    def click_hamburger(self):
        """
        Click hamburger menu
        """
        self.click(*self.CLICK_HAMBURGER)

    def verify_items_here(self, expected_value):
        """
        Verify if there are 11 boxes in the hamburger menu
        """
        sleep(2)
        self.len_counting(expected_value, *self.ELEVEN_ITEMS_HERE)

    def user_enters_f_name(self, text):
        """
        User enters first name
        """
        self.input_text(text, *self.F_NAME)

    def user_enters_l_name(self, text):
        """
        User enters last name
        """
        self.input_text(text, *self.L_NAME)

    def user_enters_email(self, text):
        """
        User enters e-mail
        """
        self.input_text(text, *self.E_MAIL)

    def user_enters_text(self, text):
        """
        User enters text
        """
        self.input_text(text, *self.TEXT_FIELD)

    def user_clicks_send_btn(self):
        """
        User clicks on send button
        """
        self.click(*self.SEND_BTN)

    def text_message_fld(self, text):
        """
        Verify that field Your message has text Your message
        """
        self.string_is_empthy(text, *self.TEXT_FIELD_W_TEXT)


