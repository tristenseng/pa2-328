#Tristen Seng
#tristen.seng@student.csulb.edu
#025683201
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
        if int(line[0]) < knapsack_capacity:
            item_weight.append(int(line[0]))
            item_value.append(int(line[1]))

    #create matrix[rows == len(item_array), cols == len(knapsack_capacity)]
    rows = len(item_value)
    cols = knapsack_capacity
    matrix = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
    n = rows

    #fill matrix
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            #if curr item weight > curr capacity
            if item_weight[i-1] > j:
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j - item_weight[i-1]] + item_value[i-1])

    #max value stored here
    max_value = matrix[rows][cols]

    #find items taken
    items = []
    i = n
    w = knapsack_capacity
    while i > 0 and w > 0:
        if matrix[i][w] != matrix[i - 1][w]:
            items.append(item_weight[i - 1])
            w -= item_weight[i - 1]
        i -= 1

    print("Max value of items taken is {}. Array of weights of items taken is {}".format(max_value, items))

