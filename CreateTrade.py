from WebTest.TestCase.testSellerCenter import SellerCenterTestCase
from WebTest.TestCase.testAuction import AuctionTestCase
import sys
import time

if len(sys.argv) != 3:
    print(u'请确认输入的格式是否正确，示例：CreateTrade.py 拍品种类[小说、名人字画、名人墨迹、古玩杂项、线装古旧书] 10')
elif int(sys.argv[2]) > 20:
    print(u'由于拍卖交易的特殊性，一次最多只能创建20个交易<(＿　＿)>')
else:
    auction_creator = SellerCenterTestCase()
    try:
        auction_creator.setUp()
        auction_creator.testAddAuction(sys.argv[1], int(sys.argv[2]))
    finally:
        auction_creator.tearDown()

        print(u'12分钟后将对拍品进行竞价购买，请耐心等待...')
        time.sleep(12 * 60)

        trade_creator = AuctionTestCase()

        try:
            trade_creator.setUp()
            trade_creator.testBatchBuyAuction()
            print(u'竞价购买成功，拍卖结束后会自动生成交易！')
        finally:
            trade_creator.tearDown()
