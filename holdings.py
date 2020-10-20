#!/usr/bin/env python3

class Holdings:
    '''
    This class is built for containing a portfolio of stock shares.
    The default constructor receives an open file handle for a csv file.
    '''
    def __init__(self, sharesfile):
        import csv
        self.holdings = []
        with open(sharesfile,'r') as f:
            rows = csv.reader(f)
            header = next(rows)
            for row in rows:
                myholding = dict()
                myholding["name"] = row[0]
                myholding["date"] = row[1]
                myholding["shares"] = int(row[2])
                myholding["price"] = float(row[3])
                self.holdings.append(myholding)


    def total_assets_value(self):
        sum = 0
        for holding in self.holdings:
            sum = sum + holding["shares"]*holding["price"]
        return sum


    def sell(self, sharename, numshares):
        import pandas as pd
        df = pd.DataFrame(self.holdings)
        if df.name == sharename:
            df.shares -= numshares
        '''
        for holding in self.holdings:
            if holding["name"] == name:
                holding["shares"] -= numshares
                break
        '''
