import time

from playwright.sync_api import Page, expect ,Playwright


def test_Basics(playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()  ## When we have multiple pages in ase we use if there is a single page then it is not mandatory to use.
    page=context.new_page()
    page.goto("https://rahulshettyacademy.com")  #invoke browser

#chromium headless mode 1 single context
def test_shortcuts(page:Page):
    page.goto("https://google.com")  #for to run with terminal in headed mode we have to pass --headed in it (pytest test_Basics.py::test_Basics--headed)


def test_corelocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning3456")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button",name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()



def test_Firefoxbrowser(playwright :Playwright):
    ffbrowser=playwright.firefox.launch(headless=False)
    page=ffbrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning3456")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    



