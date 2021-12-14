from behave import *

from tests.test import *


@given('Bot')
def first_step(context):
    context.a = Test_bikvadrat()


@when('test_a_equal_zero return OK')
def check_sneakers(context):
    context.a.test_a_equal_zero()


@when('test_result_bikvadrat return OK')
def check_slates(context):
    context.a.test_result_bikvadrat()


@then('good job')
def last_step(context):
    pass
