#!/usr/bin/python

"""
Product inventory class that can be used to manage an inventory of products
@author: Madhav Murthy
"""

import random as r

class Inventory(object):
    def __init__(self, products=[]):
        self.products = products

    def add_product(self, price, pid, quantity):
        for product in self.products:
            if(product.pid == pid):
                product.quantity += quantity
                return
        self.products.append(Product(price, pid, quantity))

    def get_product(self, pid):
        for product in self.products:
            if(product.pid == pid):
                return product
        return None

    def remove_product(self, pid, quantity):
        for product in self.products:
            if(product.pid == pid):
                product.quantity -= quantity

    def change_price(self, pid, price):
        for product in self.products:
            if(product.pid == pid):
                product.price = price

    def total_value(self):
        total = 0
        for product in self.products:
            total += product.product_value()
        return total

    def tostring(self):
        for product in self.products:
            product.tostring()


class Product(object):
    def __init__(self, price, pid, quantity):
        self.price = price
        self.pid = pid
        self.quantity = quantity

    """
    effects: prints the information of the given product
    """
    def tostring(self):
        print 'price: ' + str(self.price) + ', id: ' + str(self.pid) + ', quantity: ' + str(self.quantity)

    """
    returns: total value of this product
    """
    def product_value(self):
        return (self.price * self.quantity)

def main():
    inven = Inventory()
    pids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 2]
    prices = [100, 200, 120, 300, 400, 20, 35, 220, 25, 40, 300, 120]
    quantities = [5, 7, 2, 3, 1, 10, 12, 11, 3, 7, 4, 20]
    for i in range(len(pids)):
        inven.add_product(prices[i], pids[i], quantities[i])
    inven.tostring()
    print inven.total_value()

if(__name__ == '__main__'):
    main()
