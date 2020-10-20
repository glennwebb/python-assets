#!/usr/bin/env python3

class Holding:
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price


    def asset_value(self):
        return self.shares*self.price


    def sell(self, numshares):
        self.shares -= numshares
