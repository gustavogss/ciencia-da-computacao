number = int(input('Digite um numero maior que 0: '))
count = 1
result=1

while count <= number:
    result = result * count
    count +=1
print(f'\nO fatorial de !{number} é = {result}\n')
