from behave import *

@then("Click on info@lingocard.com button")
def click_contact_us_btn(context):
    """
    Verify Contact us has and redirect to info@lingocard.com
    """
    context.app.main_page.click_contact_us_btn()

    @then("Verify that href with e-mail is here {e_mail}")
    def step_impl(context, e_mail):
        """
        Verify that href with e-mail is here info@lingocard.com
        """
        context.app.main_page.email_is_hr_in_href(e_mail)





