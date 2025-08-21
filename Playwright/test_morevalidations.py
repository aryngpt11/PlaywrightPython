import time

from playwright.sync_api import Page, expect


def test_UiChecks(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    page.on("dialog",lambda dialog:dialog.accept())
    page.get_by_role("button",name="Confirm").click()

    # Hovermouse

    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()

    #Frames Handling
    pageframe=page.frame_locator("#courses-iframe")
    pageframe.get_by_role("link",name="All Access plan").click()
    expect(pageframe.locator("body")).to_contain_text("Happy Subscibers!")
    time.sleep(5)



def test_AddtoCart(page:Page):

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    #page.locator("th[role='columnheader']")
    for i in range(page.locator("th").count()):
        if page.locator("th").nth(i).filter(has_text="Price").count()>0:
            colvalue=i
            break

    Ricerow=page.locator("tr").filter(has_text="Rice")
    expect(Ricerow.locator("td").nth(colvalue)).to_have_text("37")
