import time

from Module import Uri, UserInfo, TestData
from WebTest.Action.BaseAction import BaseAction
from WebTest.Page.AuctionOrderPage import AuctionOrderPage


class AuctionOrderAction(BaseAction):
    def __init__(self):
        self.auctionOrderPage = AuctionOrderPage()
        BaseAction.__init__(self, self.auctionOrderPage)

    # 确认收款
    def confirm_receipt(self, trade_type):
        self.auctionOrderPage.go_to(Uri.AuctionSellerTradePage)
        if trade_type == 'wait_pay':
            self.auctionOrderPage.go_to(Uri.AuctionSellerWaitToPayOrderPage)
        if trade_type == 'wait_receipt':
            self.auctionOrderPage.go_to(Uri.AuctionSellerConfirmPaymentOrderPage)
        self.auctionOrderPage.confirm_receipt_btn.click()
        time.sleep(1)
        self.auctionOrderPage.confirm_receipt_confirm_btn.click()

    # 修改运费
    def edit_trans_fee(self):
        self.auctionOrderPage.browser.refresh()
        self.auctionOrderPage.edit_trans_fee_link.click()
        time.sleep(1)
        self.auctionOrderPage.trans_fee_type_list[1].click()
        self.auctionOrderPage.edit_trans_fee_confirm_btn.click()

    # 发货
    def deliver_prod(self):
        self.auctionOrderPage.browser.refresh()
        self.auctionOrderPage.go_to(Uri.AuctionSellerWaitToDeliveryOrderPage)
        self.auctionOrderPage.delivery_prod_btn.click()
        time.sleep(1)
        self.auctionOrderPage.delivery_type_list[9].click()
        self.auctionOrderPage.delivery_prod_confirm_btn.click()

    # 付款
    def pay(self, pay_method):
        self.auctionOrderPage.go_to(Uri.AuctionBuyerWaitToPayOrderPage)
        self.auctionOrderPage.pay_trade_btn.click()
        self.auctionOrderPage.switch_to_new_window()
        self.auctionOrderPage.wait_until_clickable(self.auctionOrderPage.begin_pay_css)
        self.auctionOrderPage.begin_pay_btn.click()
        self.auctionOrderPage.change_pay_link.click()
        time.sleep(1)

        if pay_method == 'protect':
            self.auctionOrderPage.protect_pay_rdo.click()
        if pay_method == 'quick':
            self.auctionOrderPage.quick_pay_rdo.click()
        if pay_method == 'offline':
            self.auctionOrderPage.offline_pay_rdo.click()
        self.auctionOrderPage.begin_pay_confirm_btn.click()
        time.sleep(1)
        if pay_method == 'protect' or pay_method == 'quick':
            self.auctionOrderPage.pay_next_step_btn.click()
            self.auctionOrderPage.pay_password_txt.send_keys(UserInfo.PwdPay)
            self.auctionOrderPage.pay_submit_btn.click()
        else:
            self.auctionOrderPage.offline_pay_bank_rdo.click()
            self.auctionOrderPage.offline_pay_date_time.click()
            self.auctionOrderPage.browser.switch_to_frame(
                self.auctionOrderPage.browser.find_element_by_tag_name('iframe'))
            self.auctionOrderPage.offline_pay_today_btn.click()
            self.auctionOrderPage.browser.switch_to_default_content()
            self.auctionOrderPage.offline_pay_confirm_btn.click()

    # 确认收货
    def confirm_receive_prod(self):
        self.auctionOrderPage.go_to(Uri.AuctionBuyerWaitToReceiveOrderPage)
        self.auctionOrderPage.confirm_receive_btn.click()
        time.sleep(1)
        self.auctionOrderPage.confirm_receive_confirm_btn.click()

    # 退货并退款
    def refund_and_return_prod(self):
        self.auctionOrderPage.go_to(Uri.AuctionBuyerWaitToReceiveOrderPage)
        self.auctionOrderPage.refund_return_prod_link.click()
        TestData.TempID = self.auctionOrderPage.first_trade.get_attribute('tradeid')
        self.auctionOrderPage.switch_to_new_window()
        self.auctionOrderPage.receive_status_rdo[1].click()
        self.auctionOrderPage.return_prod_rdo[1].click()
        self.auctionOrderPage.return_reason_list[1].click()
        self.auctionOrderPage.refund_amount_txt.send_keys('1')
        self.auctionOrderPage.refund_submit_btn.click()

    # 同意退货
    def agree_return_prod(self):
        self.auctionOrderPage.go_to(Uri.AuctionSellerRefundOrderPage)
        self.search_trade(TestData.TempID)
        self.auctionOrderPage.refund_return_detail_link.click()
        self.auctionOrderPage.switch_to_new_window()
        self.auctionOrderPage.agree_return_btn.click()
        time.sleep(1)
        self.auctionOrderPage.agree_return_confirm_btn.click()

    # 买家退货
    def return_prod(self):
        self.auctionOrderPage.go_to(Uri.AuctionBuyerRefundOrderPage)
        self.search_trade(TestData.TempID)
        self.auctionOrderPage.return_prod_btn.click()
        self.auctionOrderPage.switch_to_new_window()
        self.auctionOrderPage.return_prod_delivery_type_list[9].click()
        self.auctionOrderPage.return_prod_confirm_btn.click()

    # 卖家确认收货并退款
    def confirm_receive_and_refund(self):
        self.auctionOrderPage.go_to(Uri.AuctionSellerRefundOrderPage)
        self.search_trade(TestData.TempID)
        self.auctionOrderPage.confirm_receive_prod_and_refund.click()
        pay_method = self.auctionOrderPage.trade_pay_method_msg.text
        if pay_method == '中介保护':
            time.sleep(1)
            self.auctionOrderPage.confirm_receive_prod_and_refund_confirm_btn.click()
            self.auctionOrderPage.wait_until_clickable(self.auctionOrderPage.msg_bar_css)
            self.auctionOrderPage.browser.refresh()
            self.auctionOrderPage.go_to(Uri.AuctionSellerAllTradeOrderPage)
            self.search_trade(TestData.TempID)
            self.auctionOrderPage.return_detail_link.click()
            self.auctionOrderPage.switch_to_new_window()
        else:
            self.auctionOrderPage.switch_to_new_window()
            self.auctionOrderPage.refund_pay_password.send_keys(UserInfo.PwdPay)
            self.auctionOrderPage.refund_btn.click()
            time.sleep(1)
            self.auctionOrderPage.refund_confirm_btn.click()

    # 搜索交易
    def search_trade(self, trade_id):
        self.auctionOrderPage.wait_until_clickable(self.auctionOrderPage.trade_id_field_css)
        self.auctionOrderPage.trade_id_field_txt.send_keys(trade_id)
        self.auctionOrderPage.trade_search_btn.click()

    # 获取提示条信息
    def get_top_msg_text(self):
        self.auctionOrderPage.wait_until_clickable(self.auctionOrderPage.msg_bar_css)
        return self.auctionOrderPage.msg_bar.text

    # 获取支付结果
    def get_pay_result(self):
        self.auctionOrderPage.wait_until_clickable(self.auctionOrderPage.pay_success_css)
        return self.auctionOrderPage.pay_success_msg.text

    # 获取退款退货结果
    def get_refund_return_prod_result(self):
        self.auctionOrderPage.wait_until_clickable(self.auctionOrderPage.refund_status_css)
        return self.auctionOrderPage.refund_status_msg.text
