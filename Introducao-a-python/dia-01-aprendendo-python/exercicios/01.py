a = int(input('Digite um número:' ))
b = int(input('Digite outro número:' ))

def numbers(a,b):
    if (a>b):
        return (f'O numero {a} é maior que o número {b}\n')
    else:
         return (f'O numero {b} é maior que o número {a}\n')
     
print(numbers(a,b))