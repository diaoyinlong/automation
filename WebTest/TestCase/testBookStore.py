import unittest

from WebTest.Action.BookStoreAction import BookStoreAction


class BookStoreTestCase(unittest.TestCase):
    def setUp(self):
        self.action = BookStoreAction()

    def tearDown(self):
        self.action.bookStorePage.quit()

    def testBookBuyerCreateOrder(self, n=1):
        """
        测试书店买家生成订单流程
        :param n:
        :return:
        """
        self.action.login('user1')
        for i in range(n):
            # 将商品加入购物车
            self.action.add_prod_to_cart()

            # 在购物车内进行结算
            self.action.settle_in_cart()

            # 验证生成订单成功
            self.assertIn('订单提交成功', self.action.get_create_order_success_text())

    def testAddBookToFavFolder(self):
        """
        测试将图书放入收藏夹的功能正确性
        :return:
        """
        self.action.login('user1')
        # 清空商品收藏夹
        self.action.clean_up_prod_fav()

        # 将商品放入收藏夹
        self.action.add_prod_to_fav_folder()

        # 验证商品成功加入收藏夹
        self.assertEqual('图书已成功添加到收藏夹！', self.action.get_add_book_to_fav_success_msg())
        self.assertTrue(self.action.has_fav_prod())

        # 清空商品收藏夹
        self.action.clean_up_prod_fav()

        # 验证清空成功
        self.assertEqual('批量删除收藏商品操作成功！', self.action.get_top_msg_text())
        self.assertFalse(self.action.has_fav_prod())

    def testBookReport(self):
        """
        测试图书举报功能
        :return:
        """
        self.action.login('user1')
        self.assertTrue(self.action.upload_report_file(), '上传图片失败')
        # 进行举报操作
        self.action.do_report()

        # 验证成功后的提示
        self.assertEqual('举报成功，感谢您对网站的支持和爱护！', self.action.get_report_success_msg())

    def testBatchDeleteCartProd(self):
        """
        测试批量删除购物车内的商品
        :return:
        """
        self.action.login('user1')
        # 将商品加入购物车
        self.action.add_prod_to_cart()

        # 批量删除购物车内商品
        self.action.batch_delete_cart_prod()

        # 验证删除成功
        self.assertEqual('批量删除购物车商品操作成功！', self.action.get_top_msg_text())

    def testBatchMoveCartProdToFav(self):
        """
        测试将购物车内的商品批量移入收藏夹
        :return:
        """
        self.action.login('user1')
        # 将商品加入购物车
        self.action.add_prod_to_cart()

        # 将商品批量移入收藏夹
        self.action.batch_move_cart_prod_to_fav()

        # 验证移入成功
        self.assertEqual('批量移入收藏夹操作成功！', self.action.get_top_msg_text())

    def testAddShopToFavFolder(self):
        """
        测试将店铺添加到收藏夹
        :return:
        """
        self.action.login('user1')
        # 清空店铺收藏夹
        self.action.clean_up_shop_fav()

        # 进行收藏店铺操作
        self.action.add_shop_to_fav_folder()

        # 验证店铺收藏成功
        self.assertEqual('书店收藏成功！', self.action.get_add_shop_to_fav_success_msg())
        self.assertTrue(self.action.has_fav_shop())

        # 清空店铺收藏夹
        self.action.clean_up_shop_fav()

        # 验证清空成功
        self.assertEqual('批量删除收藏店铺操作成功！', self.action.get_top_msg_text())
        self.assertFalse(self.action.has_fav_shop())
