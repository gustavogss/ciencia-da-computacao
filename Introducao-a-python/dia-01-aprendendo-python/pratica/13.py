numbers = [6, 8, 5, 9, 10]
array = []

for number in numbers:
    array.append(number * 10)  # append - adiciona elementos na lista 
print(array)

new_result = [10 * number for number in numbers]
print(new_result)