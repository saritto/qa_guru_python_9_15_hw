from selene import browser, have, command
import os


class ShoppingSite:

    def open(self):
        browser.open('https://www.saucedemo.com/')

    def auth(self):
        username = os.getenv('USERNAME')
        password = os.getenv('PASSW')
        browser.element('#user-name').type(username)
        browser.element('#password').type(password)
        browser.element('#login-button').click()

    def add_items_to_cart(self):
        browser.element('#add-to-cart-sauce-labs-backpack').click()
        browser.element('#add-to-cart-sauce-labs-bolt-t-shirt').click()

    def go_to_cart(self):
        browser.element('#shopping_cart_container').click()
        browser.element('.cart_list').all('.inventory_item_name').should(have.exact_texts('Sauce Labs Backpack',
                                                                                          'Sauce Labs Bolt T-Shirt'))

    def buy(self):
        # checkout
        browser.element('#checkout').click()
        # fill info
        browser.element('#first-name').type('Sara')
        browser.element('#last-name').type('Test')
        browser.element('#postal-code').type('123456789')
        browser.element('#continue').click()
        # check info
        browser.element('.cart_list').all('.inventory_item_name').should(have.exact_texts('Sauce Labs Backpack',
                                                                                          'Sauce Labs Bolt T-Shirt'))
        browser.element('.summary_total_label').perform(command.js.scroll_into_view).should(
            have.exact_text('Total: $49.66'))

    def finish(self):
        browser.element('#finish').click()
        browser.element('.complete-header').should(have.exact_text('Thank you for your order!'))
