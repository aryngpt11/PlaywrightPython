from playwright.sync_api import Playwright, expect

from Playwright.utils.apiBase import APIUtils


def test_e2e_web_api(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    #createorder
    apiutils=APIUtils()
    order_id=apiutils.createOrder(playwright)


    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("qwertyuiopasdfgh@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("A1@qwerty")
    page.get_by_role("button",name="Login").click()
    page.get_by_role("button",name="ORDERS").click()

    row=page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()