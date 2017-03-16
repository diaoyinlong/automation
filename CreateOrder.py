from WebTest.TestCase.testBookStore import BookStoreTestCase
import sys

if len(sys.argv) != 2:
    print(u'请确认输入的格式是否正确，示例：CreateOrder.py 10')
else:
    creator = BookStoreTestCase()
    try:
        creator.setUp()
        creator.testBookBuyerCreateOrder(int(sys.argv[1]))
        print(u'订单生成成功！')
    finally:
        creator.tearDown()
