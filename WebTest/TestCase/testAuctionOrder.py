import unittest

from WebTest.Action.AuctionOrderAction import AuctionOrderAction


class AuctionOrderTestCase(unittest.TestCase):
    def setUp(self):
        self.action = AuctionOrderAction()

    def tearDown(self):
        self.action.auctionOrderPage.quit()

    def testBuyerWaitToPayTrade(self):
        """
        测试买家待付款交易
        :return:
        """
        self.action.login('user1')
        # 中介保护付款
        self.action.pay('protect')

        # 验证付款成功
        self.assertEqual('付款成功', self.action.get_pay_result())

        # 即时到账付款
        self.action.pay('quick')

        # 验证付款成功
        self.assertEqual('付款成功', self.action.get_pay_result())

        # 线下付款
        self.action.pay('offline')

        # 验证付款成功
        self.assertEqual('付款成功', self.action.get_pay_result())

    def testSellerWaitToPayTrade(self):
        """
        测试卖家待付款交易
        :return:
        """
        self.action.login('user3')
        # 确认收款
        self.action.confirm_receipt('wait_pay')

        # 验证确认收款成功
        self.assertEqual('确认收款成功！', self.action.get_top_msg_text())

        # 修改运费
        self.action.edit_trans_fee()

        # 验证修改运费成功
        self.assertEqual('修改运费操作成功！', self.action.get_top_msg_text())

    def testSellerDeliveryTrade(self):
        """
        测试卖家待发货交易
        :return:
        """
        self.action.login('user3')
        # 确认收款
        self.action.confirm_receipt('wait_receipt')

        # 验证确认收款成功
        self.assertEqual('确认收款成功！', self.action.get_top_msg_text())

        # 发货
        self.action.deliver_prod()

        # 验证发货成功
        self.assertEqual('发货操作成功！', self.action.get_top_msg_text())

    def testBuyerConfirmReceiveTrade(self):
        """
        测试买家待确认收货交易
        :return:
        """
        self.action.login('user1')
        # 确认收货
        self.action.confirm_receive_prod()

        # 验证确认收货成功
        self.assertEqual('确认收货操作成功！', self.action.get_top_msg_text())

        # 退货并退款
        self.action.refund_and_return_prod()

        # 验证申请退货退款成功
        self.assertEqual('退货状态：申请退货中', self.action.get_refund_return_prod_result())

    def testRefundAndReturnProdTrade(self):
        """
        测试退货退款交易
        :return:
        """
        self.action.login('user3')
        # 同意退货
        self.action.agree_return_prod()

        # 验证同意退货成功
        self.assertEqual('同意退货成功！', self.action.get_top_msg_text())

        action1 = AuctionOrderAction()
        action1.login('user1')
        # 买家退货
        action1.return_prod()

        # 验证退货成功
        self.assertEqual('退货状态：卖家待收退货', action1.get_refund_return_prod_result())
        action1.auctionOrderPage.quit()

        # 卖家确认收货并退款
        self.action.confirm_receive_and_refund()

        # 验证成功
        self.assertEqual('退货状态：已退货，已退款', self.action.get_refund_return_prod_result())
