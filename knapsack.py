def fractional_knapsack(items, capacity):
    for item in items:
        item.append(item[0] / item[1])
    items.sort(key=lambda x: x[2], reverse=True)
    total_value = 0.0
    knapsack = []
    for item in items:
        if capacity == 0:
            break
        if item[1] <= capacity:
            # we add the item to the knapsack
            knapsack.append((item[0], item[1]))
            total_value += item[0]
            capacity -= item[1]
        else:
            fraction = capacity / item[1]
            knapsack.append((item[0] * fraction, item[1] * fraction))
            total_value += item[0] * fraction
            capacity = 0
    return total_value, knapsack


if __name__ == "__main__":
    items = [[60, 10], [100, 20], [120, 30]]
    capacity = 50
    max_value, selected_item = fractional_knapsack(items, capacity)
    print("max_value", max_value)
    print("selected_item", selected_item)
