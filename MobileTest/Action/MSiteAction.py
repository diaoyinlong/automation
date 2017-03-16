from MobileTest.Page.MSitePage import MSitePage
from Module import Uri, UserInfo
from Public.Toolkit import Toolkit
import time


class MSiteAction:
    def __init__(self):
        self.page = MSitePage()
        self.temp_data = ''

    # 搜索
    def search(self, search_content, search_type):
        self.page.go_to(Uri.MSearchPage)
        self.page.wait_until_clickable(self.page.search_submit_css)
        if search_type == 'book':
            self.page.book_search_tab.click()
        if search_type == 'auction':
            self.page.auction_search_tab.click()
        if search_type == 'shop':
            self.page.shop_search_tab.click()
        self.page.search_txt.send_keys(search_content)
        self.page.search_submit_btn.click()

    # 获取搜索结果
    def get_search_result(self, search_type):
        results = []
        if search_type == 'book':
            for result in self.page.book_search_result:
                results.append(result.text)
        if search_type == 'auction':
            for result in self.page.auction_search_result:
                results.append(result.text)
        if search_type == 'shop':
            for result in self.page.shop_search_result:
                results.append(result.text)
        return results

    # 添加图书到收藏夹
    def add_book_to_favorite(self):
        self.page.go_to(Uri.MBookDetailPage)
        self.page.book_fav_btn.click()

    # 删除收藏夹内的图书
    def delete_book_in_favorite(self):
        for del_btn in self.page.del_fav_book_btn:
            del_btn.click()
            time.sleep(1)

    # 验证图书收藏夹
    def verify_book_fav(self, is_exist):
        result = False
        self.page.go_to(Uri.FavMProdPage)
        time.sleep(1)
        self.page.wait_until_not_clickable(self.page.loading_css)
        if is_exist is True:
            for book_name in self.page.fav_books_name:
                if book_name.text == '测试用书请勿购买':
                    result = True
        if is_exist is False:
            if self.page.no_data.text == '暂无数据':
                result = True
        return result

    # 添加店铺到收藏夹
    def add_shop_to_favorite(self):
        self.page.go_to(Uri.MShopPage)
        self.page.shop_fav_btn.click()

    # 删除收藏夹内的店铺
    def delete_shop_in_favorite(self):
        for del_btn in self.page.del_fav_shop_btn:
            del_btn.click()
            time.sleep(1)

    # 验证店铺收藏夹
    def verify_shop_fav(self, is_exist):
        result = False
        self.page.go_to(Uri.FavMShopPage)
        time.sleep(1)
        self.page.wait_until_not_clickable(self.page.loading_css)
        if is_exist is True:
            for shop_name in self.page.fav_shops_name:
                if shop_name.text == UserInfo.User3 + '的书店':
                    result = True
        if is_exist is False:
            if self.page.no_data.text == '暂无数据':
                result = True
        return result

    # 添加拍品到收藏夹
    def add_auction_to_favorite(self):
        self.page.go_to(Uri.MAuctionDetailPage)
        self.page.wait_until_clickable(self.page.auction_fav_css)
        self.page.auction_fav_btn.click()

    # 删除拍品到收藏夹
    def delete_auction_to_favorite(self):
        for del_btn in self.page.del_fav_auction_btn:
            del_btn.click()
            time.sleep(1)

    # 验证拍卖收藏夹
    def verify_auction_fav(self, is_exist):
        result = False
        self.page.go_to(Uri.FavMAuctionPage)
        time.sleep(2)
        if is_exist is True:
            for shop_name in self.page.fav_auction_name:
                if '测试拍卖请勿购买' in shop_name.text:
                    result = True
        if is_exist is False:
            if self.page.no_data.text == '暂无数据':
                result = True
        return result

    # 登录
    def login(self,user='user2'):
        self.page.go_to(Uri.MLoginPage)
        if user == 'user1':
            self.page.login_name_txt.send_keys(UserInfo.User1)
        if user == 'user2':
            self.page.login_name_txt.send_keys(UserInfo.User2)
        self.page.login_pwd_txt.send_keys(UserInfo.PwdLogin)
        self.page.login_submit_btn.click()
        time.sleep(2)

    # 修改登录密码
    def change_login_pwd(self, old, new):
        self.page.go_to(Uri.MChangePwdPage)
        self.page.old_pwd_txt.send_keys(old)
        self.page.new_pwd_txt.send_keys(new)
        self.page.change_pwd_submit_btn.click()
        self.page.wait_until_clickable(self.page.success_msg_css)

    # 获取成功提示文本
    def get_success_txt(self):
        return self.page.success_msg.text

    # 添加收货地址
    def add_receive_address(self):
        self.page.go_to(Uri.MReceiveAddressPage)
        self.page.wait_until_clickable(self.page.address_submit_css)
        self.page.address_submit_btn.click()
        self.page.receiver_name_txt.send_keys('自动化')
        self.page.receiver_mobile_txt.send_keys('18510291234')
        self.page.receiver_area.click()
        time.sleep(1)
        self.page.receiver_area_confirm_btn.click()
        self.page.receiver_address_txt.send_keys('红厂孔夫子A6')
        self.page.address_submit_btn.click()

    # 编辑收货地址
    def edit_receive_address(self):
        self.page.go_to(Uri.MReceiveAddressPage)
        self.page.wait_until_clickable(self.page.edit_address_css)
        self.page.edit_address_btn.click()
        time.sleep(1)
        self.page.address_submit_btn.click()

    # 删除收货地址
    def del_receive_address(self):
        self.page.go_to(Uri.MReceiveAddressPage)
        self.page.wait_until_clickable(self.page.address_submit_css)
        for btn in self.page.del_address_btn:
            btn.click()
            self.page.wait_until_clickable(self.page.confirm_css)
            self.page.confirm_btn.click()
            time.sleep(1)

    # 获取提示框内文本
    def get_tip_view_txt(self):
        self.page.wait_until_clickable(self.page.tip_view_css)
        return self.page.tip_view.text

    # 将图书加到购物车
    def add_book_to_cart(self):
        self.page.go_to(Uri.MBookDetailPage)
        self.page.add_cart_btn.click()

    # 去购物车结算
    def settle_in_cart(self):
        self.page.go_to(Uri.MCartPage)
        self.page.wait_until_clickable(self.page.cart_item_css)
        self.page.check_all_rdo.click()
        self.page.go_to_pay_btn.click()
        self.page.wait_until_clickable(self.page.order_book_box_css)
        self.page.create_order_btn.click()

    # 获取生成订单后的文本
    def get_submit_result_txt(self):
        self.page.wait_until_clickable(self.page.submit_order_result_css)
        time.sleep(1)
        return self.page.submit_order_result.text

    # 进行常规竞价
    def bid(self):
        self.page.go_to(Uri.MAuctionDetailPage)
        self.page.wait_until_clickable(self.page.pop_bid_win_css)
        self.page.pop_bid_win_btn.click()
        time.sleep(1)
        self.page.bid_btn.click()

    # 设置代理价
    def set_agent(self):
        self.page.go_to(Uri.MAuctionDetailPage)
        self.page.pop_bid_win_btn.click()
        time.sleep(1)
        self.page.agent_bid_tab.click()
        time.sleep(1)
        self.page.agent_bid_btn.click()

    # 跳转到联系人列表页
    def go_to_contact_page(self):
        self.page.go_to(Uri.MContactPage)

    # 搜索用户
    def search_user(self, user):
        if user == 'user1':
            self.page.search_friend_txt.send_keys(UserInfo.User1)
        if user == 'user2':
            self.page.search_friend_txt.send_keys(UserInfo.User2)
        self.page.search_user_btn.click()

    # 发送消息
    def send_message(self):
        self.temp_data = Toolkit.get_random_value()
        self.page.search_user_result.click()
        time.sleep(1)
        self.page.send_message_txt.send_keys(self.temp_data)
        self.page.send_btn.click()

    # 验证收到消息
    def verify_message_received(self):
        self.go_to_contact_page()
        self.search_user('user1')
        self.page.search_user_result.click()
        time.sleep(1)
        result = False
        for message in self.page.message_collection:
            if message.text == self.temp_data:
                result = True
        return result

    # 买家评价订单/交易
    def eval(self, user_type, eval_type):
        if user_type == 'buyer':
            self.page.go_to(Uri.MLoginPage, token=Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin))
            if eval_type == 'order':
                self.page.go_to(Uri.MBuyerEvalOrderPage)
                self.page.wait_until_clickable(self.page.order_action_css)
                self.page.order_action_btn.click()
            if eval_type == 'trade':
                self.page.go_to(Uri.MBuyerEvalTradePage)
                self.page.wait_until_clickable(self.page.trade_action_css)
                self.page.trade_action_btn.click()
        if user_type == 'seller':
            self.page.go_to(Uri.MLoginPage, token=Toolkit.get_user_token(UserInfo.User3, UserInfo.PwdLogin))
            self.page.go_to(Uri.MSellerEvalOrderPage)
            self.page.wait_until_clickable(self.page.order_action_css)
            self.page.order_action_btn.click()

        self.page.eval_content_txt.send_keys('automation test')
        self.page.submit_eval_btn.click()

    # 确认收货订单
    def receive_order(self):
        self.page.go_to(Uri.MReceivedBookOrderPage)
        self.page.wait_until_clickable(self.page.order_action_css)
        self.page.order_action_btn.click()
        time.sleep(1)
        self.page.book_confirm_btn.click()

    # 订单发货
    def send_order(self):
        self.page.go_to(Uri.MLoginPage, token=Toolkit.get_user_token(UserInfo.User3, UserInfo.PwdLogin))
        self.page.go_to(Uri.MSendBookOrderPage)
        self.page.wait_until_clickable(self.page.order_action_css)
        self.page.order_action_btn.click()
        self.page.wait_until_clickable(self.page.book_confirm_css)
        self.page.send_order_num_txt.send_keys('12345678')
        self.page.book_confirm_btn.click()

    # 确认交易订单
    def receive_trade(self):
        self.page.go_to(Uri.MLoginPage, token=Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin))
        self.page.go_to(Uri.MReceivedAuctionTradePage)
        self.page.wait_until_clickable(self.page.trade_action_css)
        self.page.trade_action_btn.click()
        time.sleep(1)
        self.page.trade_confirm_btn.click()
        time.sleep(1)

    # 支付订单
    def pay_order(self):
        self.page.go_to(Uri.MLoginPage, token=Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin))
        self.page.go_to(Uri.MBuyerPayOrderPage)
        self.page.wait_until_clickable(self.page.order_action_css)
        self.page.order_action_btn.click()
        self.page.wait_until_clickable(self.page.pay_step2_css)
        time.sleep(1)
        self.page.pay_step2_btn.click()
        time.sleep(1)
        self.page.pay_pass_txt.send_keys(UserInfo.PwdPay)
        self.page.pay_step3_btn.click()

    # 支付交易
    def pay_trade(self):
        self.page.go_to(Uri.MLoginPage, token=Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin))
        self.page.go_to(Uri.MBuyerPayTradePage)
        self.page.wait_until_clickable(self.page.trade_action_css)
        self.page.trade_action_btn.click()
        self.page.wait_until_clickable(self.page.pay_step1_css)
        time.sleep(1)
        self.page.pay_step1_btn.click()
        self.page.wait_until_clickable(self.page.pay_step2_css)
        time.sleep(1)
        self.page.pay_step2_btn.click()
        time.sleep(1)
        self.page.pay_pass_txt.send_keys(UserInfo.PwdPay)
        self.page.pay_step3_btn.click()

    # 获取支付成功信息
    def get_pay_success_msg(self):
        self.page.wait_until_clickable(self.page.pay_success_css)
        return self.page.pay_success_msg.text

    # 添加提现账号
    def add_cash_account(self):
        self.page.go_to(Uri.MLoginPage, token=Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin))
        self.page.go_to(Uri.MCashAccountPage)
        self.page.add_cash_account_btn.click()
        self.page.alipay_chk.click()
        self.page.alipay_txt.send_keys('fish3@126.com')
        self.page.submit_btn_3.click()

    # 进行提现操作
    def do_cash_back(self):
        self.page.go_to(Uri.MLoginPage, token=Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin))
        self.page.go_to(Uri.MCashBackPage)
        self.page.cash_txt.send_keys('2')
        time.sleep(1)
        self.page.submit_btn_1.click()
        self.page.cash_back_pass_txt.send_keys(UserInfo.PwdPay)
        time.sleep(1)
        self.page.submit_btn_2.click()

    # 获取提现成功提示
    def get_fund_success_msg(self):
        self.page.wait_until_clickable(self.page.fund_success_css)
        return self.page.fund_success_msg.text

    # 删除提现账号
    def delete_cash_account(self):
        self.page.go_to(Uri.MLoginPage, token=Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin))
        self.page.go_to(Uri.MCashAccountPage)
        for btn in self.page.del_cash_account_btn:
            btn.click()
            self.page.wait_until_clickable(self.page.confirm_css)
            self.page.confirm_btn.click()
            time.sleep(1)

    # 获取书店收货后成功提示
    def get_book_receive_success_msg(self):
        self.page.wait_until_clickable(self.page.book_receive_success_css)
        return self.page.book_receive_success_msg.text

    # 获取拍卖收货后成功提示
    def get_auction_receive_success_msg(self):
        self.page.wait_until_clickable(self.page.auction_receive_success_css)
        return self.page.auction_receive_success_msg.text

    # 进行转账操作
    def do_fund_transfer(self):
        self.page.go_to(Uri.MLoginPage, token=Toolkit.get_user_token(UserInfo.User3, UserInfo.PwdLogin))
        self.page.go_to(Uri.MTransferPage)
        self.page.trans_fund_account_txt.send_keys(UserInfo.FundID1)
        self.page.trans_fund_money_txt.send_keys('1')
        self.page.submit_btn_1.click()
        self.page.trans_pay_password.send_keys(UserInfo.PwdPay)
        self.page.submit_btn_2.click()
