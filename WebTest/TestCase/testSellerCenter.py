import unittest

from WebTest.Action.BookStoreAction import BookStoreAction
from WebTest.Action.SellerCenterAction import SellerCenterAction


class SellerCenterTestCase(unittest.TestCase):
    def setUp(self):
        self.action = SellerCenterAction()

    def tearDown(self):
        self.action.sellerCenterPage.quit()

    def testAddBook(self):
        """
        测试上书
        :return:
        """
        self.action.login('user3')
        # for i in range(99):
        # 进行常规上书
        self.action.add_book_normal()

        # 验证上书成功提示
        self.assertEqual('商品添加成功！', self.action.get_top_msg_text())

        # 使用ISBN上书
        self.action.add_book_isbn()

        # 验证ISBN数据载入正确性
        data = self.action.get_isbn_load_data()
        self.assertTrue(data['book_name'] == '相墓手札' and
                        data['isbn'] == '9787229036201' and
                        data['author'] == '信周著' and
                        data['press'] == '重庆出版社' and
                        data['pub_date'] == '2011-06-01' and
                        data['binding'] == '平装' and
                        data['edition'] == '1' and
                        data['page'] == '303' and
                        data['origin_price'] == '29.80' and
                        data['pic_url'] is not None and
                        data['pic_url'] != '')

    def testDeleteProd(self):
        """
        测试删除图书
        :return:
        """
        self.action.login('user3')
        # 删除未审核图书
        self.action.delete_no_certify_book()

        # 验证删除成功
        self.assertTrue(self.action.get_delete_result())

        # 在回收站删除图书
        self.action.delete_book_in_recycle()

        # 验证删除成功
        self.assertTrue(self.action.get_delete_result())

    def testBestBook(self):
        """
        测试推荐图书功能
        :return:
        """
        self.action.login('user3')
        # 取消推荐
        self.action.cancel_best_book()

        # 推荐图书
        self.action.change_book_to_best()

        # 验证推荐成功
        self.assertTrue(self.action.verify_best_result())

        # 取消推荐
        self.action.cancel_best_book()

        # 验证取消推荐成功
        self.assertTrue(self.action.get_cancel_best_result())

    def testManageShopProdType(self):
        """
        测试店铺商品分类管理
        """
        try:
            self.action.login('user3')
            # 添加商品分类
            self.action.add_prod_type()

            # 验证添加成功
            self.assertEqual('添加成功！', self.action.get_top_msg_text())

            # 修改商品分类
            self.action.edit_prod_type()

            # 验证修改成功
            self.assertEqual('修改成功！', self.action.get_top_msg_text())

            # 开启商品分类
            self.action.switch_on_prod_type()

            # 验证开启成功
            self.assertEqual('auto_edit', self.action.get_prod_type())
        finally:
            # 清理商品分类
            self.action.batch_delete_prod_type()

    def testDecorateBookShop(self):
        """
        测试装扮店铺
        :return:
        """
        self.action.login('user3')
        # 编辑临时通知
        self.action.edit_temp_inform()

        # 验证编辑成功
        self.assertEqual('保存成功！', self.action.get_top_msg_text())

        # 编辑店铺公告
        self.action.edit_shop_notice()

        # 验证编辑成功
        self.assertEqual('保存成功！', self.action.get_top_msg_text())

        # 添加友情店铺
        self.action.add_friend_shop()

        # 验证添加成功
        self.assertEqual('添加友情店铺操作成功！', self.action.get_top_msg_text())

    def testShopMemo(self):
        """
        测试书店备忘录
        :return:
        """
        self.action.login('user3')
        # 新增备忘录
        self.action.add_shop_memo()

        # 验证新增备忘录成功提示
        self.assertEqual('添加便笺成功', self.action.get_top_msg_text())

        # 编辑备忘录
        self.action.edit_shop_memo()

        # 验证成功提示
        self.assertEqual('编辑便笺成功', self.action.get_top_msg_text())

        # 删除备忘录
        self.action.delete_shop_memo()

        # 验证删除成功提示
        self.assertEqual('删除便笺成功', self.action.get_top_msg_text())

    def testShopBlackList(self):
        """
        测试书店黑名单
        :return:
        """
        self.action.login('user3')
        # 将该会员移除黑名单
        self.action.delete_from_book_black_list()

        # 将某一会员添加进店铺黑名单
        self.action.add_book_black_list()

        # 验证添加成功
        self.assertEqual('添加书店黑名单成功', self.action.get_top_msg_text())

        # 买家将商品添加到购物车
        action2 = BookStoreAction()
        action2.login('user1')
        action2.add_prod_to_cart()

        # 验证添加失败
        self.assertEqual('您在该店铺的黑名单列表中，暂时不能订购该商品！', action2.get_add_cart_fail_txt())

        # 将该会员移除黑名单
        self.action.delete_from_book_black_list()

        # 验证移除成功
        self.assertEqual('删除黑名单成功', self.action.get_top_msg_text())

        # 买家再次将商品添加到购物车
        action2.add_prod_to_cart()

        # 验证添加成功
        self.assertEqual('商品已成功加入购物车！', action2.get_add_cart_success_txt())

        action2.bookStorePage.quit()

    def testAddAuction(self, m='小说', n=1):
        """
        测试添加拍品
        :param m:
        :param n:
        :return:
        """
        try:
            self.action.login('user3')
            for i in range(n):
                # 添加拍品
                self.action.add_auction(m)

                # 验证拍品成功添加
                self.assertIn('操作成功！', self.action.get_top_msg_text())

        finally:
            # 保存拍品ID
            self.action.save_auction_id()

    def testAuctionBlackList(self):
        """
        测试拍卖黑名单
        :return:
        """
        self.action.login('user3')
        # 添加到黑名单
        self.action.add_auction_black_list()

        # 验证添加成功
        self.assertEqual('添加黑名单成功！', self.action.get_top_msg_text())

        # 删除黑名单
        self.action.delete_from_auction_black_list()

        # 验证删除成功
        self.assertEqual('删除黑名单成功！', self.action.get_top_msg_text())
