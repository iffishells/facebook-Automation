from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup



# for input css selector
#     input[aria-label='Phone number, username, or email']
# for input password css selector

# for submit button
#     button[type='submit']
# class facebook automationa and their controller
class InstagramAutomation:

    def __init__(self,url):
        self.url =  url
        self.starting_message = 'Instagram Automation script is going to be started...'


    def login(self):
        with sync_playwright() as p:
            # browser object/instance
            browser = p.chromium.launch(headless=False ,  slow_mo = 500)
            page =  browser.new_page()
            page.goto(self.url)

            # inputting credentionals for accounts
            page.fill('css=[aria-label="Phone number, username, or email"]','iffishells@gmail.com')
            page.fill('css=[aria-label="Password"]', 'Razerblade1394!@#()')
            page.click('button[type="submit"]')



            #


if __name__ =='__main__':
    # instagram login page url
    url = 'https://www.instagram.com/accounts/login/'
    instagram  = InstagramAutomation(url)
    instagram.login()
