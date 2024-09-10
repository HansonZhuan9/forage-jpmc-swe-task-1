import unittest
import random
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        bid = quote['top_bid']['price']
        ask = quote['top_ask']['price']
        self.assertEqual(getDataPoint(quote), (quote['stock'], bid, ask, (bid+ask)/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        bid = quote['top_bid']['price']
        ask = quote['top_ask']['price']
        self.assertEqual(getDataPoint(quote), (quote['stock'], bid, ask, (bid+ask)/2))


  def test_getRatio(self):
      for i in range(10):
          price_a = random.randint(1,200)
          price_b = random.randint(1,200)
          self.assertEqual(getRatio(price_a, price_b), price_a/price_b)

  def test_getRatio_price_b_equal_zero(self):
      price_a = random.randint(1, 200)
      price_b = 0
      self.assertIsNone(getRatio(price_a,price_b))



if __name__ == '__main__':
    unittest.main()
