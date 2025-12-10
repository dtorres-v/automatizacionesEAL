import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

# Define las capabilities aquí o impórtalas de un config
capabilities = {
    "appium:appPackage": "uy.com.assist.eaf",
    "appium:appActivity": ".MainActivity",
    "platformName": "Android",
    "appium:deviceName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:udid": "ZY223VK2N7"
}


@pytest.fixture(scope="class")
def driver_setup(request):

    options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote("http://localhost:4723", options=options)

    # Inyectamos el driver en la clase que usa el test
    request.cls.driver = driver

    yield driver  # Aquí se ejecutan los tests

    # Teardown: Se ejecuta al finalizar
    driver.quit()