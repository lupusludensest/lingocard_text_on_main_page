from behave import *

@then("Verify {language} is here")
def verify_language(context, language):
    """
    Verify Albanian, Hungarian are here
    """
    context.app.main_page.verify_language(language)