import pytest
from selene import browser


@pytest.fixture(params=[
    (1920, 1080),
    (1600, 900),
    (1366, 768),
    (1280, 1024),
    (1280, 768),
    (800, 600),
    (800, 480)])
def setup_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    if width > 900:
        yield 'desktop'
    else:
        yield 'mobile'

    browser.quit()


@pytest.fixture(params=[
    (1920, 1080),
    (1600, 900),
    (1366, 768),
    (1280, 1024),
    (1280, 768),
])
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[
    (800, 600),
    (800, 480)])
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()