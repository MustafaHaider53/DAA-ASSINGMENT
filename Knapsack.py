def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build table 
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Print the  table
    print("Dynamic Programming Table:")
    for row in dp:
        print(row)

    # Find out which items to include in knapsack
    w = capacity
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)  
            w -= weights[i - 1]

    selected_items.reverse()
    return dp[n][capacity], selected_items

# Take user input
num_items = int(input("Enter the number of items: "))
values = []
weights = []

print("Enter the values and weights of the items:")
for i in range(num_items):
    value = int(input(f"Value of item {i+1}: "))
    weight = int(input(f"Weight of item {i+1}: "))
    values.append(value)
    weights.append(weight)

capacity = int(input("Enter the maximum weight: "))

# Compute the knapsack solution
max_value, selected_items = knapsack(values, weights, capacity)

# Display the results
print(f"\nMaximum value in knapsack: {max_value}")
print("Items included :", selected_items)
