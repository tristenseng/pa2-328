import sys
import csv

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file)
    arr = []
    weight = sys.argv[2]
    for line in csv_reader:
        arr.append(line)
    print(arr)
    print(weight)
        