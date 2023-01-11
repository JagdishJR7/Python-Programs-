#writing to a csv file:
import csv

with open('employee.txt',mode='w') as cf:
    data=csv.writer(cf, delimiter=',',quotechar='=',quoting=csv.QUOTE_MINIMA)
    data=writerow(['Name','Department'
