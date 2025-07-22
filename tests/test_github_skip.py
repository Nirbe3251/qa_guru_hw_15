import pytest
from selene import browser, by


def test_skip_mobile(setup_browser):
    if setup_browser == 'mobile':
        pytest.skip("Это мобильное приложение")
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()

def test_skip_desktop(setup_browser):
    if setup_browser == 'desktop':
        pytest.skip("Это десктопное приложение")
    browser.open("https://github.com/")
    browser.element('[class=Button-content]').click()
    browser.element(by.text("Sign up")).click()