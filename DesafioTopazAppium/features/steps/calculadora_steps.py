from appium import webdriver
from behave import given, when, then

# Inicializar o driver como variável global ou local
driver = None

@given('que a calculadora está aberta')
def step_given_calculator_open(context):
    global driver
    desired_caps = {
        'platformName': 'Android Emulator',
        'platformVersion': '11',
        'deviceName': 'TestCalculadora:5554',
        'appPackage': 'com.google.android.calculator',
        'appActivity': 'com.android.calculator2.Calculator',
        'automationName': 'UiAutomator2'
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

@when('eu digito o número {number}')
def step_when_i_type_number(context, number):
    driver.find_element_by_id(f'com.google.android.calculator:id/digit_{number}').click()

@when('eu aperto o botão "{button}"')
def step_when_i_press_button(context, button):
    driver.find_element_by_accessibility_id(button).click()

@then('o resultado deve ser {result}')
def step_then_result_should_be(context, result):
    actual_result = driver.find_element_by_id('com.google.android.calculator:id/result_final').text
    assert actual_result == result, f"Esperava {result}, mas obteve {actual_result}"
