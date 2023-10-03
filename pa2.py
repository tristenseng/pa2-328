import sys
import csv

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file)
    item_value = []
    item_weight = []


    knapsack_capacity = int(sys.argv[2])
    #csv input == [item_weight, item_value]
    #create array of item values
    #create array of item weights
    for line in csv_reader:
        item_value.append(line[0])
        item_weight.append(line[1])

    #create matrix[rows == len(item_array), cols == len(knapsack_capacity)]
    rows = len(item_value)
    cols = knapsack_capacity
    matrix = []
    
    for i in range(cols):
        print(i)
        