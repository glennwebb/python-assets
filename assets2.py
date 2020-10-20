#!/usr/bin/env python3

import csv

with open('portfolio2.csv','r') as f:
    sum = 0
    rows = csv.reader(f)
    header = next(rows)
    for row in rows:
        row[2] = int(row[2])
        row[3] = float(row[3])
        sum = sum + (row[2]*row[3])
    print('the sum is', sum)
