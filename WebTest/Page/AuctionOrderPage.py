from WebTest.Page.BasePage import BasePage


class AuctionOrderPage(BasePage):
    @property
    def confirm_receipt_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_confirm_pay btn_green_70_24"]')

    @property
    def close_trade_link(self):
        return self.browser.find_element_by_class_name('btn_close_trade')

    @property
    def edit_trans_fee_link(self):
        return self.browser.find_element_by_class_name('btn_edit_fee')

    @property
    def close_trade_link(self):
        return self.browser.find_element_by_class_name('btn_close_trade')

    @property
    def confirm_receipt_confirm_btn(self):
        return self.browser.find_element_by_id('confirmPayWin').find_element_by_css_selector(self.confirm_btn_css)

    @property
    def close_trade_confirm_btn(self):
        return self.browser.find_element_by_id('closeTradeWin').find_element_by_css_selector(self.confirm_btn_css)

    @property
    def trans_fee_type_list(self):
        self.browser.find_element_by_id('feeType').click()
        return self.browser.find_element_by_id('feeType').find_elements_by_tag_name('li')

    @property
    def edit_trans_fee_confirm_btn(self):
        return self.browser.find_element_by_id('editFeeWin').find_element_by_css_selector('a[class="subBtn f_left"]')

    @property
    def pay_trade_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_pay btn_orange_41_24"]')

    @property
    def begin_pay_css(self):
        return '#btn_pay'

    @property
    def change_pay_link(self):
        return self.browser.find_element_by_id('changeType')

    @property
    def begin_pay_btn(self):
        return self.browser.find_element_by_css_selector(self.begin_pay_css)

    @property
    def protect_pay_rdo(self):
        return self.browser.find_element_by_id('payWayRadio_1')

    @property
    def quick_pay_rdo(self):
        return self.browser.find_element_by_id('payWayRadio_2')

    @property
    def offline_pay_rdo(self):
        return self.browser.find_element_by_id('payWayRadio_3')

    @property
    def begin_pay_confirm_btn(self):
        return self.browser.find_element_by_id('payWayWin').find_element_by_css_selector(
            'a[class="subBtn orange_btn90"]')

    @property
    def pay_next_step_btn(self):
        return self.browser.find_element_by_id('btn_step_next')

    @property
    def pay_password_txt(self):
        return self.browser.find_element_by_id('payPass')

    @property
    def pay_submit_btn(self):
        return self.browser.find_element_by_id('btn_pay_submit')

    @property
    def pay_success_css(self):
        return 'div[class="m_b12"]'

    @property
    def pay_success_msg(self):
        return self.browser.find_element_by_css_selector(self.pay_success_css)

    @property
    def offline_pay_bank_rdo(self):
        return self.browser.find_element_by_id('payWayBank_0')

    @property
    def offline_pay_date_time(self):
        return self.browser.find_element_by_name('payTime')

    @property
    def offline_pay_today_btn(self):
        return self.browser.find_element_by_id('dpTodayInput')

    @property
    def offline_pay_confirm_btn(self):
        return self.browser.find_element_by_id('payWayBankWin').find_element_by_css_selector(
            'a[class="subBtn orange_btn90"]')

    @property
    def delivery_prod_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_deliver_goods btn_green_41_24"]')

    @property
    def delivery_type_list(self):
        self.browser.find_element_by_id('delivery_type_select').click()
        return self.browser.find_element_by_id('delivery_type_select').find_elements_by_tag_name('li')

    @property
    def delivery_prod_confirm_btn(self):
        return self.browser.find_element_by_id('deliverGoodsWin').find_element_by_css_selector(
            'a[class="subBtn f_left"]')

    @property
    def confirm_receive_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_confirm_receipt btn_green_70_24"]')

    @property
    def confirm_receive_confirm_btn(self):
        return self.browser.find_element_by_id('confirmReceiptWin').find_element_by_css_selector(self.confirm_btn_css)

    @property
    def refund_return_prod_link(self):
        return self.browser.find_element_by_css_selector(
            '#trade_list_box > div:nth-child(1) > div.border_notop > table > tbody > tr > td.last > p:nth-child(2) > a')

    @property
    def receive_status_rdo(self):
        return self.browser.find_elements_by_name('receiveStatus')

    @property
    def return_prod_rdo(self):
        return self.browser.find_elements_by_name('isBackShipment')

    @property
    def return_reason_list(self):
        self.browser.find_element_by_id('causeCode').click()
        return self.browser.find_element_by_id('causeCode').find_elements_by_tag_name('li')

    @property
    def refund_amount_txt(self):
        return self.browser.find_element_by_name('backAmount')

    @property
    def refund_submit_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_orange_90_25 f_left m_r20 submit"]')

    @property
    def refund_status_css(self):
        return 'div[class="trade_box_title"] > span[class="m_r20"]'

    @property
    def refund_status_msg(self):
        return self.browser.find_element_by_css_selector(self.refund_status_css)

    @property
    def refund_return_detail_link(self):
        return self.browser.find_element_by_css_selector(
            '#trade_list_box > div > div.border_notop > table > tbody > tr > td:nth-child(4) > div > p:nth-child(4) > a')

    @property
    def return_detail_link(self):
        return self.browser.find_element_by_css_selector(
            '#trade_list_box > div > div.border_notop > table > tbody > tr > td:nth-child(4) > div > p:nth-child(3) > a')

    @property
    def agree_return_btn(self):
        return self.browser.find_element_by_css_selector('a[class="m_r10 btn_green_70_24 f_left applyAgreementgoods"]')

    @property
    def agree_return_confirm_btn(self):
        return self.browser.find_element_by_id('backgWin').find_element_by_css_selector(self.confirm_btn_css)

    @property
    def return_prod_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_return_goods btn_green_41_24"]')

    @property
    def return_prod_delivery_type_list(self):
        self.browser.find_element_by_id('express').click()
        return self.browser.find_element_by_id('express').find_elements_by_tag_name('li')

    @property
    def return_prod_confirm_btn(self):
        return self.browser.find_element_by_css_selector('a[class="sure f_left m_r20"]')

    @property
    def confirm_receive_prod_and_refund(self):
        return self.browser.find_element_by_css_selector('a[class="btn_confirm_receipt_refund btn_green_110_24"]')

    @property
    def confirm_receive_prod_and_refund_confirm_btn(self):
        return self.browser.find_element_by_id('confirmReceiptRefundWin').find_element_by_css_selector(
            self.confirm_btn_css)

    @property
    def trade_pay_method_msg(self):
        return self.browser.find_element_by_id('trade_list_box').find_element_by_css_selector('p[class="gray6"]')

    @property
    def refund_pay_password(self):
        return self.browser.find_element_by_name('password')

    @property
    def refund_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_gray_70_25 submit"]')

    @property
    def refund_confirm_btn(self):
        return self.browser.find_element_by_id('refundPayWin').find_element_by_css_selector(self.confirm_btn_css)
