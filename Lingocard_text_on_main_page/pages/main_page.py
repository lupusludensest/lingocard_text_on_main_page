from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):

    # locators
    TEXT_HERE = (By.XPATH, "//h1[@class='header-title flex-container content-center text-center lang']")
    CLICK_HAMBURGER = (By.CSS_SELECTOR, ".menu-link")
    ELEVEN_ITEMS_HERE = (By.CSS_SELECTOR, "#menu li a")


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
        sleep(5)
        self.len_counting(expected_value, *self.ELEVEN_ITEMS_HERE)


