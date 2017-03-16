import unittest

from Module import TestData
from WebTest.Action.EvalAction import EvalAction


class EvaluationTestCase(unittest.TestCase):
    def setUp(self):
        self.action = EvalAction()

    def tearDown(self):
        self.action.evalPage.quit()

    def testBookBuyerCreateEditEval(self):
        """
        测试书店买家在评价页创建并修改评价
        :return:
        """
        # 进入到评价订单列表页
        self.action.go_to_eval_order('book', 'buyer')

        # 去评价页面
        self.action.go_to_eval_page()

        # 进行差评
        self.action.do_bad_eval()

        # 验证提交成功
        self.assertEqual('添加评价成功！',
                         self.action.get_msg_bar_text())

        # 查询已提交评价的订单
        self.action.search_eval_order('book', 'buyer')

        # 进入编辑评价页面
        self.action.go_to_edit_eval_page()

        # 验证评价过的订单数据载入正确性
        self.assertTrue(self.action.evalPage.bad_eval.is_selected() and
                        self.action.evalPage.quality_1.is_selected() and
                        self.action.evalPage.ship_time_1.is_selected() and
                        self.action.evalPage.service_1.is_selected())

        # 由差评改为中评
        self.action.edit_eval_to_mid()

        # 验证提交成功
        self.assertEqual('修改评价成功！',
                         self.action.get_msg_bar_text())

        # 查询已提交评价的订单
        self.action.search_eval_order('book', 'buyer')

        # 进入编辑评价页面
        self.action.go_to_edit_eval_page()

        # 修改评价内容由中评改为差评
        self.action.edit_eval_to_bad()

        # 验证错误提示
        self.assertEqual('中评只能改成好评',
                         self.action.get_msg_bar_text())

    def testBookSellerCreateEditEval(self):
        """
        测试书店卖家在评价页创建并修改评价
        :return:
        """
        # 进入到评价订单列表页
        self.action.go_to_success_order('book', 'seller')

        # 查询买家已提交评价的订单
        self.action.search_eval_order('book', 'seller')

        # 去评价页面
        self.action.go_to_eval_page()

        # 进行差评
        self.action.do_bad_eval()

        # 验证提交成功
        self.assertEqual('添加评价成功！',
                         self.action.get_msg_bar_text())

        # 查询已提交评价的订单
        self.action.search_eval_order('book', 'seller')

        # 进入编辑评价页面
        self.action.go_to_edit_eval_page()

        # 验证评价过的订单数据载入正确性
        self.assertTrue(self.action.evalPage.bad_eval.is_selected() and
                        self.action.evalPage.pay_speed_1.is_selected() and
                        self.action.evalPage.receive_speed_1.is_selected())

        # 由差评改为中评
        self.action.edit_eval_to_mid()

        # 验证提交成功
        self.assertEqual('修改评价成功！',
                         self.action.get_msg_bar_text())

        # 查询已提交评价的订单
        self.action.search_eval_order('book', 'seller')

        # 进入编辑评价页面
        self.action.go_to_edit_eval_page()

        # 修改评价内容由中评改为差评
        self.action.edit_eval_to_bad()

        # 验证错误提示
        self.assertEqual('中评只能改成好评',
                         self.action.get_msg_bar_text())

    def testBookBuyerEditEvalReplyDelReply(self):
        """
        测试书店买家在评价详情页修改评价并添加删除回复
        :return:
        """
        # 进入到评价订单列表页
        self.action.go_to_success_order('book', 'buyer')

        # 查找到双方互评的订单
        self.action.search_eval_order('book', 'buyer')

        # 在评价详情页进行回复
        self.action.reply_eval('book')

        # 验证回复成功
        self.assertEqual('我的回复：' + TestData.Words101, self.action.get_reply_text())

        # 删除回复
        self.action.delete_reply()

        # 验证删除成功
        self.assertEqual('我的回复：暂无回复', self.action.get_reply_text())

        # 在评价详情页进行修改评价
        self.action.edit_eval_to_good()

        # 验证修改评价成功
        self.assertEqual('修改评价成功！',
                         self.action.get_msg_bar_text())

    def testBookSellerEditEvalReplyDelReply(self):
        """
        测试书店卖家在评价详情页修改评价并添并删除回复
        :return:
        """
        # 进入到评价订单列表页
        self.action.go_to_success_order('book', 'seller')

        # 查找到双方互评的订单
        self.action.search_eval_order('book', 'seller')

        # 在评价详情页进行回复
        self.action.reply_eval('book')

        # 验证回复成功
        self.assertEqual('我的回复：' + TestData.Words101, self.action.get_reply_text())

        # 删除回复
        self.action.delete_reply()

        # 验证删除成功
        self.assertEqual('我的回复：暂无回复', self.action.get_reply_text())

        # 在评价详情页进行修改评价
        self.action.edit_eval_to_good()

        # 验证修改评价成功
        self.assertEqual('修改评价成功！',
                         self.action.get_msg_bar_text())

    def testAuctionBuyerCreateEditEval(self):
        """
        测试拍卖买家创建并修改评价拍卖订单
        :return:
        """
        # 进入到评价订单列表页
        self.action.go_to_eval_order('auction', 'buyer')

        # 去评价页面
        self.action.go_to_eval_page()

        # 进行差评
        self.action.do_bad_eval()

        # 验证提交成功
        self.assertEqual('添加评价成功！',
                         self.action.get_msg_bar_text())

        # 查询已提交评价的订单
        self.action.search_eval_order('auction', 'buyer')

        # 进入编辑评价页面
        self.action.go_to_edit_eval_page()

        # 验证评价过的订单数据载入正确性
        self.assertTrue(self.action.evalPage.bad_eval.is_selected() and
                        self.action.evalPage.quality_1.is_selected() and
                        self.action.evalPage.ship_time_1.is_selected() and
                        self.action.evalPage.service_1.is_selected())

        # 由差评改为中评
        self.action.edit_eval_to_mid()

        # 验证提交成功
        self.assertEqual('修改评价成功！',
                         self.action.get_msg_bar_text())

        # 查询已提交评价的订单
        self.action.search_eval_order('auction', 'buyer')

        # 进入编辑评价页面
        self.action.go_to_edit_eval_page()

        # 修改评价内容由中评改为差评
        self.action.edit_eval_to_bad()

        # 验证错误提示
        self.assertEqual('中评只能改成好评',
                         self.action.get_msg_bar_text())

    def testAuctionSellerCreateEditEval(self):
        """
        测试拍卖卖家创建并修改评价拍卖订单
        :return:
        """
        # 进入到评价订单列表页
        self.action.go_to_success_order('auction', 'seller')

        # 查询买家已提交评价的订单
        self.action.search_eval_order('auction', 'seller')

        # 去评价页面
        self.action.go_to_eval_page()

        # 进行差评
        self.action.do_bad_eval()

        # 验证提交成功
        self.assertEqual('添加评价成功！',
                         self.action.get_msg_bar_text())

        # 查询已提交评价的订单
        self.action.search_eval_order('auction', 'seller')

        # 进入编辑评价页面
        self.action.go_to_edit_eval_page()

        # 验证评价过的订单数据载入正确性
        self.assertTrue(self.action.evalPage.bad_eval.is_selected() and
                        self.action.evalPage.pay_speed_1.is_selected() and
                        self.action.evalPage.receive_speed_1.is_selected())

        # 由差评改为中评
        self.action.edit_eval_to_mid()

        # 验证提交成功
        self.assertEqual('修改评价成功！',
                         self.action.get_msg_bar_text())

        # 查询已提交评价的订单
        self.action.search_eval_order('auction', 'seller')

        # 进入编辑评价页面
        self.action.go_to_edit_eval_page()

        # 修改评价内容由中评改为差评
        self.action.edit_eval_to_bad()

        # 验证错误提示
        self.assertEqual('中评只能改成好评',
                         self.action.get_msg_bar_text())

    def testAuctionBuyerEditEvalReplyDelReply(self):
        """
        测试拍卖买家在信誉详情页修改评价并添加删除回复
        :return:
        """
        # 进入到成功完成订单列表页
        self.action.go_to_success_order('auction', 'buyer')

        # 查找到双方互评的订单
        self.action.search_eval_order('auction', 'buyer')

        # 在评价详情页进行回复
        self.action.reply_eval('auction')

        # 验证回复成功
        self.assertEqual('我的回复：' + TestData.Words101, self.action.get_reply_text())

        # 删除回复
        self.action.delete_reply()

        # 验证删除成功
        self.assertEqual('我的回复：暂无回复', self.action.get_reply_text())

        # 在评价详情页进行修改评价
        self.action.edit_eval_to_good()

        # 验证修改评价成功
        self.assertEqual('修改评价成功！',
                         self.action.get_msg_bar_text())

    def testAuctionSellerEditEvalReplyDelReply(self):
        """
        测试拍卖卖家在信誉详情页修改评价并添加删除回复
        :return:
        """
        # 进入到成功完成订单列表页
        self.action.go_to_success_order('auction', 'seller')

        # 查找到双方互评的订单
        self.action.search_eval_order('auction', 'seller')

        # 在评价详情页进行回复
        self.action.reply_eval('auction')

        # 验证回复成功
        self.assertEqual('我的回复：' + TestData.Words101, self.action.get_reply_text())

        # 删除回复
        self.action.delete_reply()

        # 验证删除成功
        self.assertEqual('我的回复：暂无回复', self.action.get_reply_text())

        # 在评价详情页进行修改评价
        self.action.edit_eval_to_good()

        # 验证修改评价成功
        self.assertEqual('修改评价成功！',
                         self.action.get_msg_bar_text())
