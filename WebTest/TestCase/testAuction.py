import unittest

from WebTest.Action.AuctionDetailAction import AuctionDetailAction


class AuctionTestCase(unittest.TestCase):
    def setUp(self):
        self.action = AuctionDetailAction()

    def tearDown(self):
        self.action.auctionDetailPage.quit()

    def testBidAuction(self):
        """
        测试竞价购买
        :return:
        """
        self.action.login('user2')
        # 进行常规竞价
        self.action.bid_to_buy()

        # 验证竞价成功
        self.assertEqual('竞价成功！', self.action.get_bid_success_txt())

        # 设置代理
        self.action.set_agent_to_bid()

        # 验证设置成功
        self.assertEqual('设置代理价成功！', self.action.get_bid_success_txt())

        self.tearDown()
        self.setUp()

        self.action.login('user1')
        # 进行常规竞价
        self.action.bid_to_buy()

        # 验证竞价成功
        self.assertEqual('竞价成功！', self.action.get_bid_success_txt())

        # 进行常规竞价
        self.action.bid_to_buy()

        # 验证竞价成功
        self.assertEqual('竞价成功！', self.action.get_bid_success_txt())

    def testAddAuctionToFav(self):
        """
        测试将拍品添加到收藏夹
        :return:
        """
        self.action.login('user1')
        # 清空收藏的拍品
        self.action.clean_up_auction_fav()

        # 将拍品添加到收藏夹
        self.action.add_auction_to_fav()

        # 验证添加成功
        self.assertEqual('拍品已成功放入收藏夹！', self.action.get_add_fav_success_txt())
        self.assertTrue(self.action.has_auction_in_fav())

        # 清空收藏的拍品
        self.action.clean_up_auction_fav()

        # 验证清空成功
        self.assertEqual('批量删除我收藏的拍品成功！', self.action.get_top_bar_msg())
        self.assertFalse(self.action.has_auction_in_fav())

    def testBatchBuyAuction(self):
        """
        仅作为批量造拍卖数据使用
        """
        self.action.login('user1')
        self.action.batch_bid_to_buy()
