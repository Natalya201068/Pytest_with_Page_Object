import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
load_dotenv()


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en/ru/es...(etc)")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    my_proxy = os.getenv("MY_PROXY")
    options = Options()
    options.add_argument(f"--proxy-server={my_proxy}")
    options.add_experimental_option('prefs', {
                                    'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
