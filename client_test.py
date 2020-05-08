import unittest
from client import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'] ,quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getRatio_forDifferentprice_b(self):
    quotes = [
      {'price_a': 120.48, 'price_b': 117.87}, # if a > b (non-zero)
      {'price_a': 101.48, 'price_b': 117.87}, # if b > a (non-zero)
      {'price_a': 0, 'price_b': 117.87},      # if numeator is zero
      {'price_a': 101.48, 'price_b': 0},      # if denominator is zero # (test fails)
      {'price_a': 101, 'price_b': 0.87},      # if numerator is not float
      {'price_a': 101.23, 'price_b': 87},     # if denominator is not float
    ]

    for qoute in quotes:
      self.assertEqual(getRatio(qoute['price_a'], qoute['price_b']), (qoute['price_a'] / qoute['price_b']))

if __name__ == '__main__':
    unittest.main()
