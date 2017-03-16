import unittest

from MobileTest.Action.MSiteAction import MSiteAction
from Module import Config, UserInfo


class MSiteTestCase(unittest.TestCase):
    def setUp(self):
        self.action = MSiteAction()

    def tearDown(self):
        self.action.page.quit()

    def testSearch(self):
        key_word = ''
        if Config.env == 'Internal':
            key_word = '测试'
        if Config.env == 'External':
            key_word = '旧书'
        self.action.search(key_word, 'book')
        self.verify_search_result(key_word, 'book')

        self.action.search(key_word, 'auction')
        self.verify_search_result(key_word, 'auction')

        self.action.search(key_word, 'shop')
        self.verify_search_result(key_word, 'shop')

    def testManageBookFavorite(self):
        self.action.login()
        self.action.add_book_to_favorite()
        self.assertTrue(self.action.verify_book_fav(True))
        self.action.delete_book_in_favorite()
        self.assertTrue(self.action.verify_book_fav(False))

    def testManageShopFavorite(self):
        self.action.login()
        self.action.add_shop_to_favorite()
        self.assertTrue(self.action.verify_shop_fav(True))
        self.action.delete_shop_in_favorite()
        self.assertTrue(self.action.verify_shop_fav(False))

    def testManageAuctionFavorite(self):
        self.action.login()
        self.action.add_auction_to_favorite()
        self.action.verify_auction_fav(True)
        self.action.delete_auction_to_favorite()
        self.action.verify_auction_fav(False)

    def verify_search_result(self, key_word, search_type):
        results = self.action.get_search_result(search_type)
        if len(results) != 0:
            for result in results:
                self.assertIn(key_word, result)
        else:
            self.fail('No search result!!!')

    def testChangePassword(self):
        self.action.login()
        self.action.change_login_pwd(UserInfo.PwdLogin, '654321')
        self.assertEqual('修改成功', self.action.get_success_txt())
        self.action.change_login_pwd('654321', UserInfo.PwdLogin)
        self.assertEqual('修改成功', self.action.get_success_txt())

    def testManageReceiveAddress(self):
        self.action.login()
        self.action.add_receive_address()
        self.assertEqual('新增地址成功', self.action.get_tip_view_txt())
        self.action.edit_receive_address()
        self.assertEqual('修改地址成功', self.action.get_tip_view_txt())
        self.action.del_receive_address()
        self.assertEqual('删除成功', self.action.get_tip_view_txt())

    def testCreateBookOrder(self):
        self.action.login('user1')
        self.action.add_book_to_cart()
        self.assertEqual('加入购物车成功', self.action.get_tip_view_txt())
        self.action.settle_in_cart()
        self.assertEqual('订单提交成功', self.action.get_submit_result_txt())

    def testBidAuction(self):
        self.action.login('user1')
        self.action.bid()
        self.assertEqual('出价成功', self.action.get_tip_view_txt())
        self.action.set_agent()
        self.assertEqual('代理价设置成功', self.action.get_tip_view_txt())
        self.tearDown()
        self.setUp()
        self.action.login('user2')
        self.action.bid()
        self.assertEqual('出价成功', self.action.get_tip_view_txt())
        self.action.bid()
        self.assertEqual('出价成功', self.action.get_tip_view_txt())

    def testSendMessage(self):
        self.action.login('user1')
        self.action.go_to_contact_page()
        self.action.search_user('user2')
        self.action.send_message()
        self.tearDown()
        self.setUp()
        self.action.login('user2')
        self.assertTrue(self.action.verify_message_received())

    def testEvaluation(self):
        self.action.eval('buyer', 'order')
        self.assertEqual('评价成功', self.action.get_tip_view_txt())
        self.action.eval('seller', 'order')
        self.assertEqual('评价成功', self.action.get_tip_view_txt())
        self.action.eval('buyer', 'trade')
        self.assertEqual('评价成功', self.action.get_tip_view_txt())

    def testReceivedBookOrder(self):
        self.action.login('user1')
        self.action.receive_order()
        self.assertEqual('您已完成确认收货，现在可以去评价卖家了', self.action.get_book_receive_success_msg())

    def testSendBookOrder(self):
        self.action.send_order()
        self.assertEqual('操作成功', self.action.get_tip_view_txt())

    def testReceivedAuctionTrade(self):
        self.action.receive_trade()
        self.assertEqual('您已完成确认收货，现在可以去评价卖家了', self.action.get_auction_receive_success_msg())

    def testPay(self):
        self.action.pay_order()
        self.assertEqual('支付成功', self.action.get_pay_success_msg())
        self.action.pay_trade()
        self.assertEqual('支付成功', self.action.get_pay_success_msg())

    @unittest.skipIf(Config.env == 'External', 'External cannot do cash back action!!!')
    def testCashBack(self):
        self.action.add_cash_account()
        self.assertEqual('添加成功', self.action.get_tip_view_txt())
        self.action.do_cash_back()
        self.assertEqual('提现申请提交成功', self.action.get_fund_success_msg())
        self.action.delete_cash_account()
        self.assertEqual('删除成功', self.action.get_tip_view_txt())

    def testTransFund(self):
        self.action.do_fund_transfer()
        self.assertEqual('转账成功', self.action.get_fund_success_msg())
