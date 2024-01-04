import os

from selene import browser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption(
        "--browser_version",
        default="100.0"
    )

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def browser_config(request):
    browser_version = request.config.getoption("--browser_version")
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1440
    browser.config.window_height = 900
    options = Options()
    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": browser_version,
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)

    # Использовать класс Remote из модуля selenium.webdriver, а не selene.support.webdriver
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options,
    )

    browser.config.driver = driver

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
