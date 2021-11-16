from behave import *

from tests.test import *


@given('Factory')
def first_step(context):
    context.a = Test_Shoe_store()


@when('test_receiving_sneakers return OK')
def check_sneakers(context):
    context.a.test_receiving_sneakers()


@when('test_style_slates return OK')
def check_slates(context):
    context.a.test_style_slates()


@then('good job')
def last_step(context):
    pass
