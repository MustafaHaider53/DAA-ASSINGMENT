def coin_change(amount):
    # Denominations of Pakistani rupees
    denominations = [5000, 1000, 500, 100, 75, 50, 20, 10, 5, 2, 1]
    # To store the count of each denomination
    result = {}

    for denom in denominations:
        if amount >= denom:
            count = amount // denom
            amount -= count * denom
            result[denom] = count

    return result

# Amount to change
amount = 1988
# Get the result
change = coin_change(amount)

# Print the results
print(f"Amount: Rs. {amount}")
print("Denominations required:")
for denom, count in change.items():
    print(f"Rs. {denom}: {count}")
