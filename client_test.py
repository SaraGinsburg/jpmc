import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_ask']['price'] + quote['top_bid']['price']) / 2))


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_ask']['price'] + quote['top_bid']['price']) / 2))
  

  def test_getRatio_checkPricesObjectAndCalculateRatio(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    pricesArr = []

    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual((quote['top_ask']['price'] + quote['top_bid']['price']) / 2, price)
      pricesArr.append(price)
    self.assertEqual(getRatio(pricesArr[0],pricesArr[1]), pricesArr[0] / pricesArr[1])


  def test_getRatio_checkPriceBZero(self):
    price_a = 121.68
    price_b = 0
    self.assertIsNone(getRatio(price_a, price_b))


  def test_getRatio_checkPriceAZero(self):
    price_a = 0
    price_b = 119.2
    self.assertEqual(getRatio(price_a, price_b),0)


  def test_getRatio_greaterThan1(self):
    price_a = 121.68
    price_b = 70.86
    self.assertGreater(getRatio(price_a, price_b),1)


  def test_getRatio_greaterThan1(self):
    price_a = 70.86
    price_b = 121.68
    self.assertLess(getRatio(price_a, price_b),1)


  def test_getRatio_exactly1(self):
    price_a = 119.2
    price_b = 119.2
    self.assertEqual(getRatio(price_a, price_b),1)


    

if __name__ == '__main__':
    unittest.main()
