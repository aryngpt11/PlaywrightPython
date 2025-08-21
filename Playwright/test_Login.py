from playwright.sync_api import Page


def test_login(page: Page):
     page.goto('https://rahulshettyacademy.com/client/#/auth/login')
     page.get_by_role('textbox', name='email@example.com').click()
     page.get_by_role('textbox', name= 'email@example.com' ).fill('qwertyuiopasdfgh@gmail.com')
     page.get_by_role('textbox', name= 'enter your passsword' ).click()
     page.get_by_role('textbox', name= 'enter your passsword' ).fill('A1@qwerty')
     page.get_by_role('button', name= 'Login' ).click()
     page.get_by_role('button', name= ' Add To Cart' ).nth(1).click()
     page.get_by_role('button', name= '   Cart' ).click()
     page.get_by_role('button', name= 'Checkout❯' ).click()
     page.locator('input[type="text"]').nth(1).click()
     page.locator('input[type="text"]').nth(1).fill('444')
     #page.get_by_role('textbox', name= 'Select Country' ).click()
     page.get_by_role('textbox', name= 'Select Country' ).type('Ind')
     page.get_by_role('button', name= 'India').click()
     page.get_by_text('Place Order').click()










