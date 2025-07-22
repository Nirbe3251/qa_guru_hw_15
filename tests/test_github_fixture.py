from selene import browser, by


def test_desktop_sing_up_own_fixture(desktop_browser):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_mobile_sing_up_own_fixture(mobile_browser):
    browser.open('https://github.com/')
    browser.element('[class=Button-content]').click()
    browser.element(by.text("Sign up")).click()