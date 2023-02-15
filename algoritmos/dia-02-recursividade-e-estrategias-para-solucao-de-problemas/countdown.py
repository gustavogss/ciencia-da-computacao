# Sem recursividade
def countdown(n):
    while n > 0:
        print(n)
        n=n-1
    print('FIM!')

'''
10
9
8
7
6
5
4
3
2
1
FIM!
'''

# Com recursividade
def countdown(n):
    if n == 0:
        print('FIM!')
    else:
        print(n)
        countdown(n - 1) #Chamando novamente a função
