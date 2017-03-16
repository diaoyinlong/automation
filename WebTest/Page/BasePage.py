from Public.Browser import Browser


class BasePage(Browser):
    @property
    def login_name_txt(self):
        return self.browser.find_element_by_css_selector('#loginName')

    @property
    def login_password_txt(self):
        return self.browser.find_element_by_css_selector('#loginPass')

    @property
    def login_submit_btn(self):
        return self.browser.find_element_by_css_selector('#btn_form_submit_button')

    @property
    def order_id_field_txt(self):
        return self.browser.find_element_by_name('orderId')

    @property
    def order_id_field_css(self):
        return 'input[name="orderId"]'

    @property
    def trade_id_field_txt(self):
        return self.browser.find_element_by_name('tradeId')

    @property
    def trade_id_field_css(self):
        return 'input[name="tradeId"]'

    @property
    def order_search_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_search_submit btn_blue"]')

    @property
    def trade_search_btn(self):
        return self.browser.find_element_by_id('btn_search_submit')

    @property
    def first_order(self):
        return self.browser.find_element_by_css_selector('#order_list_box > div')

    @property
    def first_trade(self):
        return self.browser.find_element_by_css_selector('#trade_list_box > div')

    @property
    def msg_bar(self):
        return self.browser.find_element_by_css_selector(self.msg_bar_css)

    @property
    def msg_bar_css(self):
        return 'div[class="tiplay"]'

    @property
    def confirm_btn_css(self):
        return 'a[class="subBtn"]'

    @property
    def confirm_btn(self):
        return self.browser.find_element_by_css_selector(self.confirm_btn_css)

    @property
    def no_record_msg(self):
        return self.browser.find_element_by_class_name('no_record').text

    @property
    def page_index_css(self):
        return '#page_index'
