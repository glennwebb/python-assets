#!/usr/bin/env python3

with open('portfolio.csv', 'r') as f:
    header = next(f)
    sum = 0
    for line in f:
        line = line.strip()
        parts = line.split(',')
        sum = sum + (float(parts[2]) * float(parts[3]))
    print('the sum is', sum)


