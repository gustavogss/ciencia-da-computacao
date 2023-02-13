def contains_duplicate(numbers):
    numbers.sort()
    previous_number = 'not a number';
    for number in numbers:
        if(previous_number == number): return True
        previous_number = number

    return False

    print()

    '''
    No pior caso - complexidade O(n)
    No médio caso - complexidade O(n)
    No melhor caso - complexidade O (n log n)
    '''