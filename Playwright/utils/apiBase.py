from playwright.sync_api import Playwright

orders_payload = {"orders": [{"country": "India", "productOrderedId": "67a8df1ac0d3e6622a297ccb"}]}
login_payload= {"userEmail": "qwertyuiopasdfgh@gmail.com", "userPassword": "A1@qwerty"}
class APIUtils:

    def getToken(self,playwright:Playwright):
        api_rqst = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=api_rqst.post("/api/ecom/auth/login",data=login_payload)
        assert response.ok
        print(response.json())
        responseBody=response.json()
        return responseBody["token"]

    def createOrder(self, playwright: Playwright):
        token=self.getToken(playwright)
        api_rqst = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_rqst.post("/api/ecom/order/create-order",
                                 data=orders_payload, headers={"Authorization": token,
                                                               "Content-Type": "application/json"
                                                               })
        print(response.json())
        responseBody=response.json()
        order_id=responseBody["orders"][0]
        return order_id
