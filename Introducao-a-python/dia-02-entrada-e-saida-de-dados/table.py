from tabulate import tabulate

titles = ['Animes', 'Temporadas']

data = [
    ['Digimon', 1],
    ['Jujutsu', 2],
    ['Titan', 1]]

# print(tabulate(data, headers=titles, tablefmt='fancy_grid'))
# print(tabulate(data, headers=titles, tablefmt='plain'))
# print(tabulate(data, headers=titles, tablefmt='github'))
print(tabulate(data, headers=titles, tablefmt='rounded_grid', numalign='center'))
# print(tabulate(data, headers=titles, tablefmt='mixed_grid'))
# print(tabulate(data, headers=titles, tablefmt='fancy_grid'))
# print(tabulate(data, headers=titles, tablefmt='pipe'))
# print(tabulate(data, headers=titles, tablefmt='tsv'))
# print(tabulate(data, headers=titles, tablefmt='fancy_grid', numalign='center'))

'''
tablefmt='fancy_grid' - é o formato da tabela
numalign='center' - centraliza os números na tabela
'''