import unittest
from Public.Toolkit import Toolkit


class WebInterfaceTest(unittest.TestCase):
    def testEvaluateOrder(self):
        data = {
            'orderId': 37130885,
            'rating': 'good',
            'quality': 0,
            'shipInTime': 0,
            'service': 0,
            'content': '1',
            'method': 'edit'
        }
        values = Toolkit.get_response_from_server('http://xinyu.kongfz.com/seller/index/addReview',
                                                  data)
        self.assertEqual(1, values[0])
