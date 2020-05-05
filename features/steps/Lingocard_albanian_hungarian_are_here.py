from behave import *

@then("Verify {language} is here")
def verify_albanian(context, language):
    """
    Verify Albanian, Hungarian are here
    """
    context.app.main_page.verify_albanian(language)