def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def find_average(numbers):
    if len(numbers) == 0:
        return "List is empty"
    total_sum = calculate_sum(numbers)
    average = total_sum / len(numbers)
    return average

# Test data
#numbers = [10, 20, 30, 40, 50]
numbers = [10]
# Function calls
total = calculate_sum(numbers)
average = find_average(numbers)

print("Total:", total)
print("Average:", average)