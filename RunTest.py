#!/usr/bin/python3.5

import os
import time
import unittest

import TestList
from Module import Config
from Public.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    testSuite = unittest.TestSuite()

    # 书店
    testSuite.addTests(TestList.BookStore)

    # 拍卖
    testSuite.addTests(TestList.Auction)

    # 资金
    testSuite.addTests(TestList.Fund)

    # 买家中心
    testSuite.addTests(TestList.BuyerCenter)

    # 卖家中心
    testSuite.addTests(TestList.SellerCenter)

    # 书店订单
    testSuite.addTests(TestList.BookOrder)

    # 拍卖订单
    testSuite.addTests(TestList.AuctionOrder)

    # 信誉评价
    testSuite.addTests(TestList.Evaluation)

    # 搜索
    testSuite.addTests(TestList.Search)

    timeStampArr = time.localtime(time.time())
    folder = './Log/' + time.strftime('%Y-%m-%d', timeStampArr) + '/'
    os.makedirs(folder, exist_ok=True)
    with open(folder + Config.log + '_' + Config.env + '_' + time.strftime('%H-%M-%S') + '.html', 'w',
              encoding='utf-8') as f:
        HTMLTestRunner(stream=f, title='Automation Test Report', description=u'').run(testSuite)
