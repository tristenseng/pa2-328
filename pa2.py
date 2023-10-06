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
            item_value.append(int(line[0]))
            item_weight.append(int(line[1]))

    #create matrix[rows == len(item_array), cols == len(knapsack_capacity)]
    rows = len(item_value)
    cols = knapsack_capacity
    matrix = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
    n = rows

    #fill matrix
    for i in range(rows+1):
        for j in range(cols+1):
            #if curr item weight > curr capacity
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif item_weight[i-1] > j:
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j - item_weight[i-1]] + item_value[i-1])

    #max value stored here
    max_value = matrix[rows][cols]

    #find items taken
    items = []
    for i in range(n, 0, -1):
        if matrix[i][knapsack_capacity] != matrix[i-1][knapsack_capacity-1]:
            items.append(i-1)
            knapsack_capacity -= item_weight[i-1]

    print("Maximum Value:", max_value)
    print(items)

