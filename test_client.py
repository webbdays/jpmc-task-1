# python testing framework
import unittest

# to get functions that we need to test
import client



class Test(unittest.TestCase):
    # To test client.getRatio
    def test_1(self):
        # need more test cases
        test_cases = [[2,4,0.5], [2,2,1], [1,4, 0.25]]
        for test_case in test_cases:
            self.assertEqual(client.getRatio(test_case[0], test_case[1]), test_case[2])
    
    # to test client.getDataPoint
    def test_2(self):
        # need more test cases
        test_cases = [
            [{'id': '0.5613286598732626', 'stock': 's1', 'timestamp': '2019-07-19 03:59:26.479899', 'top_bid': {'price': 14, 'size': 126}, 'top_ask': {'price': 16, 'size': 6}},("s1", 14,16,15)],
            [ {'id': '0.5613286598732626', 'stock': 's2', 'timestamp': '2019-07-19 03:59:26.479899', 'top_bid': {'price': 13, 'size': 29}, 'top_ask': {'price': 19, 'size': 20}}, ("s2", 13, 19, 16)]
            ]
        for test_case in test_cases:
            self.assertEqual(client.getDataPoint(test_case[0]),  test_case[1])
unittest.main()