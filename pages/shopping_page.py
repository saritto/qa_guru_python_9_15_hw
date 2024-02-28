from selene import browser, have, command
import os


class ShoppingPage:

    def open(self):
        browser.open('https://www.saucedemo.com/')

    def auth(self):
        username = os.getenv('USERNAME')
        password = os.getenv('PASSW')
        browser.element('#user-name').type(username)
        browser.element('#password').type(password)
        browser.element('#login-button').click()

    def check_login(self):
        browser.element('#react-burger-menu-btn').click()
        browser.element('#logout_sidebar_link').should(have.exact_text('Logout'))

    def auth_error(self):
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        browser.element('#user-name').type(username)
        browser.element('#password').type(password)
        browser.element('#login-button').click()

    def locked_user(self):
        username = os.getenv('LOCKED_USER')
        password = os.getenv('PASSW')
        browser.element('#user-name').type(username)
        browser.element('#password').type(password)
        browser.element('#login-button').click()

    def error_auth(self):
        browser.element('.error-message-container').should(have.exact_text(
            'Epic sadface: Username and password do not match any user in this service'))

    def error_locked_user(self):
        browser.element('.error-message-container').should(have.exact_text(
            'Epic sadface: Sorry, this user has been locked out.'))

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

    def logout(self):
        browser.element('#logout_sidebar_link').click()
        browser.element('.login_logo').should(have.exact_text('Swag Labs'))
        browser.element('#user-name').should(have.attribute('placeholder', 'Username'))
        browser.element('#password').should(have.attribute('placeholder', 'Password'))

    def check_cart_add(self):
        browser.element('#remove-sauce-labs-backpack').should(have.exact_text('Remove'))
        browser.element('#remove-sauce-labs-bolt-t-shirt').should(have.exact_text('Remove'))
        browser.element('.shopping_cart_badge').should(have.exact_text('2'))

    def check_cart_remove(self):
        browser.element('#remove-sauce-labs-backpack').click()
        browser.element('.shopping_cart_badge').should(have.exact_text('1'))
        assert browser.element('.removed_cart_item')


shopping_page = ShoppingPage()
