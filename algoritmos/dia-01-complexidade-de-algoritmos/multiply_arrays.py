def multiply_arrays(array1, array2):
    result = []
    number_of_iterations = 0

    for number1 in array1:
        print(f'Array 1: {number1}')
        for number2 in array2:
            print(f'Array 2: {number2}')
            result.append(number1 * number2)
            number_of_iterations += 1

    print(f'{number_of_iterations} iterações!')
    return result


meu_array = [1, 2, 3, 4, 5]

multiply_arrays(meu_array, meu_array)

'''
Array 1: 1
Array 2: 1
Array 2: 2
Array 2: 3
Array 2: 4
Array 2: 5
Array 1: 2
Array 2: 1
Array 2: 2
Array 2: 3
Array 2: 4
Array 2: 5
Array 1: 3
Array 2: 1
Array 2: 2
Array 2: 3
Array 2: 4
Array 2: 5
Array 1: 4
Array 2: 1
Array 2: 2
Array 2: 3
Array 2: 4
Array 2: 5
Array 1: 5
Array 2: 1
Array 2: 2
Array 2: 3
Array 2: 4
Array 2: 5
25 iterações!
'''

