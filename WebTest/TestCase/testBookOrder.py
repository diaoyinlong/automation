import unittest

from WebTest.Action.BookOrderAction import BookOrderAction


class BookOrderTestCase(unittest.TestCase):
    def setUp(self):
        self.action = BookOrderAction()

    def tearDown(self):
        self.action.bookOrderPage.quit()

    def testSellerWaitConfirmOrder(self):
        """
        测试卖家待确认订单
        :return:
        """
        self.action.login('user3')
        # 确认订单
        self.action.confirm_order()

        # 验证确认成功
        self.assertEqual('确认订单操作成功！', self.action.get_top_msg_text())

        # 设置运费
        self.action.edit_trans_fee()

        # 验证设置成功
        self.assertEqual('修改运费操作成功！', self.action.get_top_msg_text())

        # 取消订单
        self.action.cancel_order('seller')

        # 验证取消成功
        self.assertEqual('取消订单操作成功！', self.action.get_top_msg_text())

    def testBuyerWaitPayOrder(self):
        """
        测试买家待付款订单
        :return:
        """
        self.action.login('user1')
        # 中介保护付款
        self.action.pay('protect')

        # 验证付款成功
        self.assertIn('支付成功', self.action.get_pay_success_msg())

        # 即时到账支付
        self.action.pay('quick')

        # 验证付款成功
        self.assertIn('支付成功', self.action.get_pay_success_msg())

        # 线下支付
        self.action.pay('offline')

        # 验证线下付款成功
        self.assertTrue(self.action.verify_pay_offline())

    def testSellerDeliveryOrder(self):
        """
        测试卖家待发货订单
        :return:
        """
        self.action.login('user3')
        # 确认收款
        self.action.confirm_receive_payment()

        # 验证确认收款成功
        self.assertEqual('确认收款操作成功！', self.action.get_top_msg_text())

        # 进行发货操作
        self.action.delivery_product()

        # 验证发货成功
        self.assertEqual('发货操作成功！', self.action.get_top_msg_text())

    def testBuyerConfirmReceiveOrder(self):
        """
        测试买家待确认收货订单
        :return:
        """
        self.action.login('user1')
        # 确认收货
        self.action.confirm_receive_prod()

        # 验证确认收货成功
        self.assertEqual('确认收货操作成功！', self.action.get_top_msg_text())

        # 进行退货退款操作
        self.action.return_good_and_money()

    def testRefundProdMoneyOrder(self):
        """
        测试退货退款中订单
        :return:
        """
        self.action.login('user3')
        # 卖家同意退货退款
        self.action.agree_refund_prod_and_money()

        # 验证退货成功
        self.assertEqual('同意退货成功！', self.action.get_top_msg_text())

        # 买家退货
        action1 = BookOrderAction()
        action1.login('user1')
        action1.return_prod()
        action1.bookOrderPage.quit()

        # 卖家确认收货并退款
        self.action.confirm_receive_and_refund_money()

        # 验证确认收货并退款成功
        self.assertTrue(self.action.verify_refund_prod_money())

    def testSellerWaitReceiveOrder(self):
        """
        测试卖家待确认收货订单
        :return:
        """
        self.action.login('user3')
        # 修改配送信息
        self.action.edit_delivery_info()

        # 验证修改成功
        self.assertEqual('修改配送信息成功！', self.action.get_top_msg_text())

        # 延长收货时间
        self.action.delay_receive_time()

        # 验证延长成功
        self.assertEqual('延长收货的时间操作成功！', self.action.get_top_msg_text())
