import time

from WebTest.Page.BasePage import BasePage


class BookOrderPage(BasePage):
    @property
    def confirm_order_css(self):
        return 'a[class="btn_confirm_order btn_green_70_24"]'

    @property
    def confirm_order_btn(self):
        return self.browser.find_element_by_css_selector(self.confirm_order_css)

    @property
    def confirm_order_confirm_btn(self):
        return self.browser.find_element_by_id('confirmOrderWin').find_element_by_css_selector(self.confirm_btn_css)

    @property
    def edit_trans_fee_css(self):
        return 'a[class="btn_edit_fee font14"]'

    @property
    def edit_trans_fee_link(self):
        return self.browser.find_element_by_css_selector(self.edit_trans_fee_css)

    @property
    def trans_type_list(self):
        self.browser.find_element_by_id('delivery_type_select_2').click()
        return self.browser.find_element_by_id('delivery_type_select_2').find_elements_by_tag_name('li')

    @property
    def trans_company_list(self):
        self.browser.find_element_by_id('logistics_company_select_2').click()
        return self.browser.find_element_by_id('logistics_company_select_2').find_elements_by_tag_name('li')

    @property
    def trans_fee_txt(self):
        return self.browser.find_element_by_name('deliveryFee')

    @property
    def edit_trans_fee_confirm_btn(self):
        return self.browser.find_element_by_id('editFeeWin').find_element_by_css_selector('a[class="subBtn f_left"]')

    @property
    def cancel_order_link(self):
        return self.browser.find_element_by_class_name('btn_cancel_order')

    @property
    def seller_cancel_reason_list(self):
        self.browser.find_element_by_id('cancelOrderSelect').click()
        return self.browser.find_element_by_id('cancelOrderSelect').find_elements_by_tag_name('li')

    @property
    def buyer_cancel_reason_list(self):
        self.browser.find_element_by_id('cancel_order_select').click()
        return self.browser.find_element_by_id('cancel_order_select').find_elements_by_tag_name('li')

    @property
    def seller_cancel_reason_confirm_btn(self):
        return self.browser.find_element_by_id('cancelOrderWin').find_element_by_css_selector(self.confirm_btn_css)

    @property
    def buyer_cancel_reason_confirm_btn(self):
        return self.browser.find_element_by_id('cancelOrderWin').find_element_by_css_selector(
            'a[class="subBtn f_left"]')

    @property
    def pay_order_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_pay btn_orange_41_24"]')

    @property
    def change_pay_link(self):
        return self.browser.find_element_by_id('changeType')

    @property
    def pay_way_confirm_btn(self):
        return self.browser.find_element_by_id('payWayWin').find_element_by_css_selector(
            'a[class="subBtn orange_btn90"]')

    @property
    def next_step_btn(self):
        return self.browser.find_element_by_id('btn_step_next')

    @property
    def pay_password_txt(self):
        return self.browser.find_element_by_id('payPass')

    @property
    def pay_submit_btn(self):
        return self.browser.find_element_by_id('btn_pay_submit')

    @property
    def pay_success_css(self):
        return 'div[class="pay_result_box clearfix"]'

    @property
    def pay_success_msg(self):
        return self.browser.find_element_by_css_selector(self.pay_success_css)

    @property
    def quick_pay_rdo(self):
        return self.browser.find_element_by_id('payWayRadio_2')

    @property
    def offline_pay_rdo(self):
        return self.browser.find_element_by_id('payWayRadio_3')

    @property
    def offline_bank_rdo(self):
        return self.browser.find_element_by_id('payWayBank_0')

    @property
    def offline_pay_date_link(self):
        self.browser.find_element_by_name('payTime').click()
        time.sleep(1)
        return self.browser.find_element_by_css_selector(
            'td[class=" ui-datepicker-days-cell-over  ui-datepicker-today"]')

    @property
    def offline_confirm_btn(self):
        return self.browser.find_element_by_id('payWayBankWin').find_element_by_css_selector(
            'a[class="subBtn orange_btn90"]')

    @property
    def seller_receive_payment_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_confirm_pay btn_gray_70_24"]')

    @property
    def seller_receive_payment_confirm_btn(self):
        return self.browser.find_element_by_id('confirmPayWin').find_element_by_css_selector(self.confirm_btn_css)

    @property
    def seller_delivery_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_deliver_goods btn_green_41_24"]')

    @property
    def delivery_type_list(self):
        self.browser.find_element_by_id('delivery_type_select').click()
        return self.browser.find_element_by_id('delivery_type_select').find_elements_by_tag_name('li')

    @property
    def delivery_confirm_btn(self):
        return self.browser.find_element_by_id('deliverGoodsWin').find_element_by_css_selector(
            'a[class="subBtn f_left"]')

    @property
    def confirm_receive_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_confirm_receipt btn_green_70_24"]')

    @property
    def confirm_receive_confirm_btn(self):
        return self.browser.find_element_by_id('confirmReceiptWin').find_element_by_css_selector(self.confirm_btn_css)

    @property
    def refund_link(self):
        return self.browser.find_element_by_class_name('btn_refund')

    @property
    def receive_status_rdo(self):
        return self.browser.find_elements_by_name('receiveStatus')

    @property
    def prod_back_rdo(self):
        return self.browser.find_elements_by_name('isBackShipment')

    @property
    def prod_back_reason_list(self):
        self.browser.find_element_by_id('causeCode').click()
        return self.browser.find_element_by_id('causeCode').find_elements_by_tag_name('li')

    @property
    def refund_amount_txt(self):
        return self.browser.find_element_by_name('backAmount')

    @property
    def edit_refund_agreement_css(self):
        return 'a[class="btn_gray_90 f_left m_r10 editAgreement"]'

    @property
    def refund_submit_btn(self):
        return self.browser.find_element_by_id('subbut')

    @property
    def confirm_receive_and_refund_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_confirm_receipt_refund btn_green_110_24"]')

    @property
    def confirm_receive_and_refund_confirm_btn(self):
        return self.browser.find_element_by_id('confirmReceiptRefundWin').find_element_by_css_selector(
            self.confirm_btn_css)

    @property
    def refund_pay_password(self):
        return self.browser.find_element_by_name('password')

    @property
    def refund_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_gray_70 backAmount"]')

    @property
    def refund_confirm_btn(self):
        return self.browser.find_element_by_id('kfz_confirmWin').find_element_by_css_selector(self.confirm_btn_css)

    @property
    def return_prod_detail_css(self):
        return 'a[class="btn_returngoods_details"]'

    @property
    def return_prod_detail_link(self):
        return self.browser.find_element_by_css_selector(self.return_prod_detail_css)

    @property
    def agree_return_prod_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_green_70_24 f_left m_r10 applyAgreementgoods"]')

    @property
    def agree_return_confirm_btn(self):
        return self.browser.find_element_by_id('backgWin').find_element_by_css_selector('a[class="subBtn f_left"]')

    @property
    def return_prod_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_returngoods btn_green_70_24"]')

    @property
    def express_type_css(self):
        return '#express'

    @property
    def express_type_list(self):
        self.browser.find_element_by_css_selector(self.express_type_css).click()
        return self.browser.find_element_by_css_selector(self.express_type_css).find_elements_by_tag_name('li')

    @property
    def return_prod_confirm_btn(self):
        return self.browser.find_element_by_id('commit')

    @property
    def agree_info_css(self):
        return 'a[class="btn_gray_90 f_left m_r10 addAgreementInfo"]'

    @property
    def refund_status_css(self):
        return 'div[class="shou_box clearfix "]'

    @property
    def refund_status_msg(self):
        return self.browser.find_element_by_css_selector(self.refund_status_css)

    @property
    def edit_delivery_info_link(self):
        return self.browser.find_element_by_css_selector('a[class="btn_modify_deliver_goods btn_gray_100_24"]')

    @property
    def delay_receive_time_link(self):
        return self.browser.find_element_by_class_name('btn_delay_confirm')

    @property
    def delivery_sheet_num_txt(self):
        return self.browser.find_element_by_name('modifyShipmentNum')

    @property
    def edit_delivery_confirm_btn(self):
        return self.browser.find_element_by_id('modifyDeliverGoodsWin').find_element_by_css_selector(
            'a[class="subBtn f_left"]')

    @property
    def delay_time_list(self):
        self.browser.find_element_by_id('delayConfirmSelect').click()
        return self.browser.find_element_by_id('delayConfirmSelect').find_elements_by_tag_name('li')

    @property
    def delay_time_confirm_btn(self):
        return self.browser.find_element_by_id('delayConfirmWin').find_element_by_css_selector(self.confirm_btn_css)
