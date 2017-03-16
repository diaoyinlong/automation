import time

from Module import Uri, TestData
from WebTest.Action.BaseAction import BaseAction
from WebTest.Page.EvalPage import EvalPage


class EvalAction(BaseAction):
    def __init__(self):
        self.evalPage = EvalPage()
        BaseAction.__init__(self, self.evalPage)

    # 进入评价订单列表页
    def go_to_eval_order(self, business_type, user_type):
        if business_type == 'book' and user_type == 'buyer':
            self.login('user1')
            self.evalPage.go_to(Uri.BookBuyerEvaluateOrderPage)

        elif business_type == 'book' and user_type == 'seller':
            self.login('user3')
            self.evalPage.go_to(Uri.BookSellerEvaluateOrderPage)

        elif business_type == 'auction' and user_type == 'buyer':
            self.login('user1')
            self.evalPage.go_to(Uri.AuctionBuyerEvaluateOrderPage)

        elif business_type == 'auction' and user_type == 'seller':
            self.login('user3')
            self.evalPage.go_to(Uri.AuctionSellerEvaluateOrderPage)

        if business_type == 'book':
            self.evalPage.wait_until_clickable(self.evalPage.eval_order_btn_css)
            TestData.TempID = self.evalPage.first_order.get_attribute('orderid')
        elif business_type == 'auction':
            self.evalPage.wait_until_clickable(self.evalPage.eval_order_btn_css)
            TestData.TempID = self.evalPage.first_trade.get_attribute('tradeid')

    # 进入到成功完成订单列表页
    def go_to_success_order(self, business_type, user_type):
        if business_type == 'book' and user_type == 'buyer':
            self.login('user1')
            self.evalPage.go_to(Uri.BookBuyerSuccessOrderPage)

        elif business_type == 'book' and user_type == 'seller':
            self.login('user3')
            self.evalPage.go_to(Uri.BookSellerSuccessOrderPage)

        elif business_type == 'auction' and user_type == 'buyer':
            self.login('user1')
            self.evalPage.go_to(Uri.AuctionBuyerSuccessOrderPage)

        elif business_type == 'auction' and user_type == 'seller':
            self.login('user3')
            self.evalPage.go_to(Uri.AuctionSellerSuccessOrderPage)

    # 进入到评价页面
    def go_to_eval_page(self):
        self.evalPage.eval_btn.click()

    # 进行一次常规差评
    def do_bad_eval(self):
        self.evalPage.switch_to_new_window()
        self.evalPage.bad_eval.click()
        self.evalPage.eval_content.send_keys(TestData.Words101)
        self.evalPage.submit_eval.click()

    # 查找一个评价订单
    def search_eval_order(self, business_type, user_type):
        if business_type == 'book' and user_type == 'buyer':
            self.evalPage.go_to(Uri.BookBuyerAllOrderPage)
            self.evalPage.order_id_field_txt.send_keys(TestData.TempID)
            self.evalPage.order_search_btn.click()

        elif business_type == 'book' and user_type == 'seller':
            self.evalPage.go_to(Uri.BookSellerAllOrderPage)
            self.evalPage.order_id_field_txt.send_keys(TestData.TempID)
            self.evalPage.order_search_btn.click()

        elif business_type == 'auction' and user_type == 'buyer':
            self.evalPage.go_to(Uri.AuctionBuyerAllTradeOrderPage)
            self.evalPage.trade_id_field_txt.send_keys(TestData.TempID)
            self.evalPage.trade_search_btn.click()

        elif business_type == 'auction' and user_type == 'seller':
            self.evalPage.go_to(Uri.AuctionSellerAllTradeOrderPage)
            self.evalPage.trade_id_field_txt.send_keys(TestData.TempID)
            self.evalPage.trade_search_btn.click()

    # 进入编辑评价页
    def go_to_edit_eval_page(self):
        self.evalPage.edit_eval_btn.click()
        self.evalPage.switch_to_new_window()

    # 将评价改为中评
    def edit_eval_to_mid(self):
        self.evalPage.mid_eval.click()
        self.evalPage.submit_eval.click()

    # 将评价改为差评
    def edit_eval_to_bad(self):
        self.evalPage.bad_eval.click()
        self.evalPage.submit_eval.click()

    # 将评价改为好评
    def edit_eval_to_good(self):
        self.evalPage.edit_eval_link.click()
        self.evalPage.wait_until_clickable(self.evalPage.good_eval_css)
        self.evalPage.good_eval.click()
        self.evalPage.submit_eval.click()

    # 对评价过的订单进行回复
    def reply_eval(self, business):
        if business == 'book':
            self.evalPage.look_book_eval_link.click()
        else:
            self.evalPage.look_auction_eval_link.click()

        self.evalPage.switch_to_new_window()
        self.evalPage.reply_eval_text_area.send_keys(TestData.Words101)
        self.evalPage.reply_submit_btn.click()
        self.evalPage.wait_until_clickable(self.evalPage.delete_reply_link_css)

    # 删除回复
    def delete_reply(self):
        self.evalPage.delete_reply_link.click()
        self.evalPage.wait_until_clickable(self.evalPage.confirm_btn_css)
        self.evalPage.confirm_btn.click()
        time.sleep(2)

    # 获取通知条的文本
    def get_msg_bar_text(self):
        self.evalPage.wait_until_clickable(self.evalPage.msg_bar_css)
        return self.evalPage.msg_bar.text

    # 获取回复的文本
    def get_reply_text(self):
        return self.evalPage.my_reply_message.text
