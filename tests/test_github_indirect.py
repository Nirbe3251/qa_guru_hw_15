import pytest
from selene import browser, by


@pytest.mark.parametrize('desktop_browser', [(1920, 1080)], indirect=True, ids=['desktop_size'])
def test_desktop_sing_up_reparam(desktop_browser):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('mobile_browser', [(800, 600)], indirect=True, ids=['mobile_size'])
def test_mobile_sing_up_reparam(mobile_browser):
    browser.open('https://github.com/')
    browser.element('[class=Button-content]').click()
    browser.element(by.text("Sign up")).click()