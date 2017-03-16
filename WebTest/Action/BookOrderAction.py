import time

from Module import UserInfo, Uri, TestData
from Public.Toolkit import Toolkit
from WebTest.Action.BaseAction import BaseAction
from WebTest.Page.BookOrderPage import BookOrderPage


class BookOrderAction(BaseAction):
    def __init__(self):
        self.bookOrderPage = BookOrderPage()
        BaseAction.__init__(self, self.bookOrderPage)

    # 确认订单
    def confirm_order(self):
        self.bookOrderPage.go_to(Uri.BookSellerPendingOrderPage)
        self.bookOrderPage.wait_until_clickable(self.bookOrderPage.confirm_order_css)
        self.bookOrderPage.confirm_order_btn.click()
        time.sleep(1)
        self.bookOrderPage.confirm_order_confirm_btn.click()

    # 设置运费
    def edit_trans_fee(self):
        self.bookOrderPage.go_to(Uri.BookSellerPendingOrderPage)
        self.bookOrderPage.wait_until_clickable(self.bookOrderPage.edit_trans_fee_css)
        self.bookOrderPage.edit_trans_fee_link.click()
        time.sleep(1)
        self.bookOrderPage.trans_type_list[9].click()
        self.bookOrderPage.trans_fee_txt.clear()
        self.bookOrderPage.trans_fee_txt.send_keys('1')
        self.bookOrderPage.edit_trans_fee_confirm_btn.click()

    # 取消订单
    def cancel_order(self, user_type):
        if user_type == 'seller':
            self.bookOrderPage.go_to(Uri.BookSellerPendingOrderPage)
        if user_type == 'buyer':
            self.bookOrderPage.go_to(Uri.BookBuyerPayOrderPage)
        self.bookOrderPage.cancel_order_link.click()
        time.sleep(1)
        if user_type == 'seller':
            self.bookOrderPage.seller_cancel_reason_list[5].click()
            self.bookOrderPage.seller_cancel_reason_confirm_btn.click()
        if user_type == 'buyer':
            self.bookOrderPage.buyer_cancel_reason_list[5].click()
            self.bookOrderPage.buyer_cancel_reason_confirm_btn.click()

    # 付款
    def pay(self, pay_type):
        self.bookOrderPage.go_to(Uri.BookBuyerPayOrderPage)
        self.bookOrderPage.move_mouse_to(self.bookOrderPage.pay_order_btn)
        time.sleep(1)
        TestData.TempID = self.bookOrderPage.first_order.get_attribute('orderid')
        self.bookOrderPage.pay_order_btn.click()
        self.bookOrderPage.switch_to_new_window()
        self.bookOrderPage.change_pay_link.click()
        time.sleep(1)

        if pay_type == 'quick':
            self.bookOrderPage.quick_pay_rdo.click()
        elif pay_type == 'offline':
            self.bookOrderPage.offline_pay_rdo.click()
        self.bookOrderPage.pay_way_confirm_btn.click()
        time.sleep(1)
        if pay_type == 'quick' or pay_type == 'protect':
            self.bookOrderPage.switch_to_new_window()
            self.bookOrderPage.next_step_btn.click()
            self.bookOrderPage.pay_password_txt.send_keys(UserInfo.PwdPay)
            self.bookOrderPage.pay_submit_btn.click()
        else:
            self.bookOrderPage.offline_bank_rdo.click()
            self.bookOrderPage.offline_pay_date_link.click()
            time.sleep(1)
            self.bookOrderPage.offline_confirm_btn.click()
            self.bookOrderPage.wait_until_clickable('#order_list_box > div')

    # 确认收款
    def confirm_receive_payment(self):
        self.bookOrderPage.go_to(Uri.BookSellerPayOrderPage)
        self.bookOrderPage.seller_receive_payment_btn.click()
        time.sleep(1)
        self.bookOrderPage.seller_receive_payment_confirm_btn.click()

    # 发货
    def delivery_product(self):
        self.bookOrderPage.browser.refresh()
        self.bookOrderPage.go_to(Uri.BookSellerDeliveryOrderPage)
        self.bookOrderPage.seller_delivery_btn.click()
        TestData.TempID = self.bookOrderPage.first_order.get_attribute('orderid')
        time.sleep(1)
        self.bookOrderPage.delivery_type_list[9].click()
        self.bookOrderPage.delivery_confirm_btn.click()

    # 确认收货
    def confirm_receive_prod(self):
        self.bookOrderPage.go_to(Uri.BookBuyerReceivingOrderPage)
        self.bookOrderPage.confirm_receive_btn.click()
        time.sleep(1)
        self.bookOrderPage.confirm_receive_confirm_btn.click()

    # 买家退货退款
    def return_good_and_money(self):
        self.bookOrderPage.go_to(Uri.BookBuyerReceivingOrderPage)
        self.bookOrderPage.refund_link.click()
        TestData.TempID = self.bookOrderPage.first_order.get_attribute('orderid')
        self.bookOrderPage.switch_to_new_window()
        self.bookOrderPage.receive_status_rdo[1].click()
        self.bookOrderPage.prod_back_rdo[1].click()
        self.bookOrderPage.prod_back_reason_list[1].click()
        self.bookOrderPage.refund_amount_txt.send_keys('0.01')
        self.bookOrderPage.refund_submit_btn.click()
        self.bookOrderPage.wait_until_clickable(self.bookOrderPage.edit_refund_agreement_css)

    # 卖家同意退货退款
    def agree_refund_prod_and_money(self):
        self.bookOrderPage.go_to(Uri.BookSellerRefundOrderPage)
        self.search_order(TestData.TempID)
        self.bookOrderPage.wait_until_clickable(self.bookOrderPage.return_prod_detail_css)
        self.bookOrderPage.return_prod_detail_link.click()
        self.bookOrderPage.switch_to_new_window()
        self.bookOrderPage.agree_return_prod_btn.click()
        time.sleep(1)
        self.bookOrderPage.agree_return_confirm_btn.click()

    # 买家退货
    def return_prod(self):
        self.bookOrderPage.go_to(Uri.BookBuyerRefundOrderPage)
        self.search_order(TestData.TempID)
        self.bookOrderPage.return_prod_btn.click()
        self.bookOrderPage.switch_to_new_window()
        self.bookOrderPage.wait_until_clickable(self.bookOrderPage.express_type_css)
        self.bookOrderPage.express_type_list[9].click()
        self.bookOrderPage.return_prod_confirm_btn.click()
        self.bookOrderPage.wait_until_clickable(self.bookOrderPage.agree_info_css)

    # 卖家确认收货并退款
    def confirm_receive_and_refund_money(self):
        self.bookOrderPage.go_to(Uri.BookSellerRefundOrderPage)
        self.search_order(TestData.TempID)
        self.bookOrderPage.confirm_receive_and_refund_btn.click()
        if self.bookOrderPage.confirm_receive_and_refund_btn.get_attribute('href') == 'javascript:;':
            time.sleep(1)
            self.bookOrderPage.confirm_receive_and_refund_confirm_btn.click()
            self.bookOrderPage.wait_until_clickable(self.bookOrderPage.msg_bar_css)
        else:
            self.bookOrderPage.switch_to_new_window()
            self.bookOrderPage.refund_pay_password.send_keys(UserInfo.PwdPay)
            self.bookOrderPage.refund_btn.click()
            time.sleep(1)
            self.bookOrderPage.refund_confirm_btn.click()
            self.bookOrderPage.wait_until_clickable(self.bookOrderPage.refund_status_css)

    # 修改配送信息
    def edit_delivery_info(self):
        self.bookOrderPage.go_to(Uri.BookSellerReceivingOrderPage)
        self.search_order(TestData.TempID)
        self.bookOrderPage.edit_delivery_info_link.click()
        time.sleep(1)
        self.bookOrderPage.delivery_sheet_num_txt.clear()
        self.bookOrderPage.delivery_sheet_num_txt.send_keys(Toolkit.get_random_number(8))
        self.bookOrderPage.edit_delivery_confirm_btn.click()

    # 延长收货时间
    def delay_receive_time(self):
        self.bookOrderPage.go_to(Uri.BookSellerReceivingOrderPage)
        self.bookOrderPage.delay_receive_time_link.click()
        time.sleep(1)
        self.bookOrderPage.delay_time_list[1].click()
        self.bookOrderPage.delay_time_confirm_btn.click()

    # 查询订单
    def search_order(self, order_id):
        self.bookOrderPage.wait_until_clickable(self.bookOrderPage.order_id_field_css)
        self.bookOrderPage.order_id_field_txt.clear()
        self.bookOrderPage.order_id_field_txt.send_keys(order_id)
        self.bookOrderPage.order_search_btn.click()

    # 获取成功提示条信息
    def get_top_msg_text(self):
        self.bookOrderPage.wait_until_clickable(self.bookOrderPage.msg_bar_css)
        time.sleep(1)
        return self.bookOrderPage.msg_bar.text

    # 获取成功支付后的文本
    def get_pay_success_msg(self):
        self.bookOrderPage.wait_until_clickable(self.bookOrderPage.pay_success_css)
        return self.bookOrderPage.pay_success_msg.text

    # 验证退货退款成功
    def verify_refund_prod_money(self):
        self.bookOrderPage.go_to(Uri.BookSellerRefundFinishOrderPage)
        self.search_order(TestData.TempID)
        self.bookOrderPage.return_prod_detail_link.click()
        self.bookOrderPage.switch_to_new_window()
        return self.bookOrderPage.refund_status_msg.text == '退货状态：已退货，已退款'

    # 验证线下付款成功
    def verify_pay_offline(self):
        self.bookOrderPage.go_to(Uri.BookBuyerConfirmPaymentOrderPage)
        self.search_order(TestData.TempID)
        time.sleep(2)
        return self.bookOrderPage.first_order.get_attribute('orderid') == TestData.TempID
