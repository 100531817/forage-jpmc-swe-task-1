import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      price = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], price))


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      price = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], price))

  """ ------------ Add more unit tests ------------ """

  def test_getRatio_calculateRatio(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    prices = {}
    for quote in quotes:
      price = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
      prices[quote['stock']] = price

    self.assertEqual(getRatio(prices["ABC"], prices["DEF"]), (prices["ABC"] / prices["DEF"]))

  def test_getRatio_calculateRatioALessThanB(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 121.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    prices = {}
    for quote in quotes:
      price = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
      prices[quote['stock']] = price

    self.assertEqual(getRatio(prices["ABC"], prices["DEF"]), (prices["ABC"] / prices["DEF"]))

  def test_getRatio_ZeroDivisionError(self):
    self.assertEqual(None, getRatio(1, 0))

if __name__ == '__main__':
    unittest.main()
