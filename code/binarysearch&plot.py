import time
import matplotlib.pyplot as plt
import random

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

input_sizes = [10, 100, 1000, 10000, 100000]
execution_times = []

for size in input_sizes:
    input_array = list(range(size))
    target_value = random.randint(0, size - 1)  # Choose a random value in the array
    start_time = time.time()
    binary_search(input_array, target_value)
    end_time = time.time()
    execution_times.append(end_time - start_time)

plt.plot(input_sizes, execution_times, marker='o')
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Binary Search Algorithm Complexity")
plt.xscale('log')
plt.yscale('log')
plt.show()
