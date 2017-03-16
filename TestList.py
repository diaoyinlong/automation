from InterfaceTest.TestCase import testApp
from MobileTest.testMSite import MSiteTestCase
from WebTest.TestCase.testAuction import AuctionTestCase
from WebTest.TestCase.testAuctionOrder import AuctionOrderTestCase
from WebTest.TestCase.testBookOrder import BookOrderTestCase
from WebTest.TestCase.testBookStore import BookStoreTestCase
from WebTest.TestCase.testBuyerCenter import BuyerCenterTestCase
from WebTest.TestCase.testEvaluation import EvaluationTestCase
from WebTest.TestCase.testFund import FundTestCase
from WebTest.TestCase.testSearch import SearchTestCase
from WebTest.TestCase.testSellerCenter import SellerCenterTestCase

# 书店测试用例集
BookStore = [BookStoreTestCase('testBookBuyerCreateOrder'),
             BookStoreTestCase('testAddBookToFavFolder'),
             BookStoreTestCase('testAddShopToFavFolder'),
             BookStoreTestCase('testBatchDeleteCartProd'),
             BookStoreTestCase('testBatchMoveCartProdToFav'),
             BookStoreTestCase('testBookReport')]

# 拍卖测试用例集
Auction = [AuctionTestCase('testBidAuction'),
           AuctionTestCase('testAddAuctionToFav')]

# 买家中心测试用例集
BuyerCenter = [BuyerCenterTestCase('testManageFavSite'),
               BuyerCenterTestCase('testManageReceiveAddress'),
               BuyerCenterTestCase('testChangeLoginPassword'),
               BuyerCenterTestCase('testMyFriend')]

# 卖家中心测试用例集
SellerCenter = [SellerCenterTestCase('testAddBook'),
                SellerCenterTestCase('testDeleteProd'),
                SellerCenterTestCase('testBestBook'),
                SellerCenterTestCase('testManageShopProdType'),
                SellerCenterTestCase('testDecorateBookShop'),
                SellerCenterTestCase('testShopMemo'),
                SellerCenterTestCase('testShopBlackList'),
                SellerCenterTestCase('testAddAuction'),
                SellerCenterTestCase('testAuctionBlackList')]

# 信誉系统测试用例集
Evaluation = [EvaluationTestCase('testBookBuyerCreateEditEval'),
              EvaluationTestCase('testBookSellerCreateEditEval'),
              EvaluationTestCase('testBookBuyerEditEvalReplyDelReply'),
              EvaluationTestCase('testBookSellerEditEvalReplyDelReply'),
              EvaluationTestCase('testAuctionBuyerCreateEditEval'),
              EvaluationTestCase('testAuctionSellerCreateEditEval'),
              EvaluationTestCase('testAuctionBuyerEditEvalReplyDelReply'),
              EvaluationTestCase('testAuctionSellerEditEvalReplyDelReply')]

# 资金系统测试用例集
Fund = [FundTestCase('testPostalRecharge'),
        FundTestCase('testFundTransfer'),
        FundTestCase('testManageCashAccount'),
        FundTestCase('testChangePayPwd'),
        FundTestCase('testCashBack')]

# 书店订单测试用例集
BookOrder = [BookOrderTestCase('testSellerWaitConfirmOrder'),
             BookOrderTestCase('testBuyerWaitPayOrder'),
             BookOrderTestCase('testSellerDeliveryOrder'),
             BookOrderTestCase('testSellerWaitReceiveOrder'),
             BookOrderTestCase('testBuyerConfirmReceiveOrder'),
             BookOrderTestCase('testRefundProdMoneyOrder')]

# 拍卖订单测试用例集
AuctionOrder = [AuctionOrderTestCase('testBuyerWaitToPayTrade'),
                AuctionOrderTestCase('testSellerWaitToPayTrade'),
                AuctionOrderTestCase('testSellerDeliveryTrade'),
                AuctionOrderTestCase('testBuyerConfirmReceiveTrade'),
                AuctionOrderTestCase('testRefundAndReturnProdTrade')]

# 搜索测试用例集
Search = [SearchTestCase('testSearchSmoke')]

# App接口测试列表
IAppUser = [testApp.UserAppInterfaceTest('testUserLogin'),
            testApp.UserAppInterfaceTest('testSellerLogin'),
            testApp.UserAppInterfaceTest('testSellerLogout'),
            testApp.UserAppInterfaceTest('testUserInfo'),
            testApp.UserAppInterfaceTest('testUserRegister'),
            testApp.UserAppInterfaceTest('testAddUserAddress'),
            testApp.UserAppInterfaceTest('testEditUserAddress'),
            testApp.UserAppInterfaceTest('testSetDefaultAddress'),
            testApp.UserAppInterfaceTest('testListUserAddress'),
            testApp.UserAppInterfaceTest('testDeleteUserAddress'),
            testApp.UserAppInterfaceTest('testGetAreaList'),
            testApp.UserAppInterfaceTest('testGetSupportPayType'),
            testApp.UserAppInterfaceTest('testGetUserCommissionInfo'),
            testApp.UserAppInterfaceTest('testSearchUserByName'),
            testApp.UserAppInterfaceTest('testSearchUserByID')]

IAppAuction = [testApp.AuctionAppInterfaceTest('testAddLeaveWord'),
               testApp.AuctionAppInterfaceTest('testGetAuction'),
               testApp.AuctionAppInterfaceTest('testBidAuction'),
               testApp.AuctionAppInterfaceTest('testProxyBidAuction'),
               testApp.AuctionAppInterfaceTest('testChangeMyMaxPrice'),
               testApp.AuctionAppInterfaceTest('testInsertUserFav'),
               testApp.AuctionAppInterfaceTest('testIsInUserFav'),
               testApp.AuctionAppInterfaceTest('testListUserFav'),
               testApp.AuctionAppInterfaceTest('testEditUserFavRemark'),
               testApp.AuctionAppInterfaceTest('testDeleteUserFav'),
               testApp.AuctionAppInterfaceTest('testGetBaiInfo'),
               testApp.AuctionAppInterfaceTest('testGetUserTrade'),
               testApp.AuctionAppInterfaceTest('testListAuction'),
               testApp.AuctionAppInterfaceTest('testListAuctionRecord')]

# 移动站测试用例集
MSite = [MSiteTestCase('testSearch')]
