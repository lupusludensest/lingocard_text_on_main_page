from behave import *

@given("Loginpage")
def open_homepage(context):
    context.app.main_page.open_page()

@then('Verify if {text_here} is on page')
def verify_text_here(context, text_here):
    context.app.main_page.verify_text_here(text_here)

@then('Verify if there are {expected_value} boxes in the hamburger menu')
def verify_items_here(context, expected_value):
    context.app.main_page.click_hamburger()
    context.app.main_page.verify_items_here(expected_value)
