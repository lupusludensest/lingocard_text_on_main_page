from behave import *

@then("Click on learn more button")
def learn_more_btn(context):
    """
    Click on learn more button
    """
    context.app.main_page.learn_more_btn()

@then("Make sure {text} is here")
def verify_cr_and_dev_pltfrm(context, text):
    """
    Make sure Creating and developing platform is here
    """
    context.app.main_page.verify_cr_and_dev_pltfrm(text)


