import random

def randomAverages(n):
    list_of_averages = []

    for _ in range(100): #for _ usado apenas para controlar os passos da varredura
        average = 0
        for _ in range(n):
            average += random.randrange(1, n)
        average = average/n
        list_of_averages.append(average)

    return list_of_averages

    '''
    A complexidade de execução é linear na ordem O(n)
    Quanto ao espaço de execução vai ser do tipo 0(1)
    '''