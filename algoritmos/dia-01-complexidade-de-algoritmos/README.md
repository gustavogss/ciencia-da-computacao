# COMPLEXIDADE DE ALGORITMOS :

1. A eficiência de um algoritmo é um dos principais requisitos não funcionais abordados no levantamentos de requisitos, tanto por clientes quanto pela equipe de desenvolvimento.
   
2. A eficiência do algoritmo é mensurada quando temos funcções com grande entrada de dados.
   
3. Algoritmo é qualquer procedimento computacional bem definido que toma algum valor ou conjunto de valores como entrada e produz algum valor ou conjunto de valores como saída. Um algoritmo é uma sequência de etapas computacionais que transformam a entrada na saída. Um conjunto de instruções que realizam uma tarefa.
   
4. A complexidade de um algoritmo está relacionado ao seu o tempo de execução. Quanto maior for o tamanho da dado de entrada, maior é o tempo de execução do algoritmo, e portanto maior é a sua complexidade. 
      
5. Algoritmo linear é aquele que é literalmente proporcional ao tempo de execução. A função matemática que representa uma relação linear é f(n) = n e a notação de Ordem de Complexidade para representar a taxa de crescimento do tempo de execução de um algoritmo é dada por O(n), onde o (O) faz referência a ordem de complexidade, enquanto (n) representa o número de operações.

6. Exemplo de um algoritmo linear:

```
def squared_array(numbers):
    array_of_squares = []
    for number in numbers:
        array_of_squares.append(number * number)

    return array_of_squares
```

- Esse algoritmo recebe um array de números, percorre esse array e retorna um novo com os números ao quadrado. Ou seja, ele passa por todos os elementos desse array. Isso significa que se houver 10 números na entrada de dados,por exemplo, serão realizadas 10 operações, e teremos 10 resultados como saída.
  
- Em relação à Complexidade de Tempo, temos aqui uma taxa de crescimento linear, uma vez que o aumento no tamanho do array faz crescer proporcionalmente o tempo gasto na execução do algoritmo.
   
7. A Ordem de Complexidade pode ser chamada de Complexidade Assintótica.
   
8. 