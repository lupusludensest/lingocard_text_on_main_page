from behave import *

@then("User enters first name {name}")
def user_enters_f_name(context, name):
    """
    User enters first name
    """
    context.app.main_page.user_enters_f_name(name)

@then("User enters last name {l_name}")
def user_enters_l_name(context, l_name):
    """
    User enters last name
    """
    context.app.main_page.user_enters_l_name(l_name)

@then("User enters e-mail {e_mail}")
def user_enters_email(context, e_mail):
    """
    User enters e-mail
    """
    context.app.main_page.user_enters_email(e_mail)

@then("User enters request {any}")
def user_enters_text(context, any):
    """
    User enters text
    """
    context.app.main_page.user_enters_text(any)

@then("User clicks on send button")
def user_clicks_send_btn(context):
    """
    User clicks on send button
    """
    context.app.main_page.user_clicks_send_btn()


@then("Verify that field Your message has no text {text}")
def text_message_fld(context, text):
    """
    Verify that field Your message has text Your message
    """
    context.app.main_page.text_message_fld(text)