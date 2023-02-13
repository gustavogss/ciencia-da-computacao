# COMPLEXIDADE DE ALGORITMOS :

1. A eficiência de um algoritmo é um dos principais requisitos não funcionais abordados no levantamentos de requisitos, tanto por clientes quanto pela equipe de desenvolvimento.
   
2. A eficiência do algoritmo é mensurada quando temos funcções com grande entrada de dados.
   
3. Algoritmo é qualquer procedimento computacional bem definido que toma algum valor ou conjunto de valores como entrada e produz algum valor ou conjunto de valores como saída. Um algoritmo é uma sequência de etapas computacionais que transformam a entrada na saída. Um conjunto de instruções que realizam uma tarefa.
   
4. A complexidade de um algoritmo está relacionado ao seu o tempo de execução. Quanto maior for o tamanho da dado de entrada, maior é o tempo de execução do algoritmo, e portanto maior é a sua complexidade. A Ordem de Complexidade pode ser chamada de Complexidade Assintótica

## Complexidade Linear:

1. Algoritmo linear é aquele que é literalmente proporcional ao tempo de execução. A função matemática que representa uma relação linear é f(n) = n e a notação de Ordem de Complexidade para representar a taxa de crescimento do tempo de execução de um algoritmo é dada por O(n), onde o (O) faz referência a ordem de complexidade, enquanto (n) representa o número de operações. 

2. Exemplo de um algoritmo linear:

```
def squared_array(numbers):
    array_of_squares = []
    for number in numbers:
        array_of_squares.append(number * number)

    return array_of_squares
```

- Esse algoritmo recebe um array de números, percorre esse array e retorna um novo com os números ao quadrado. Ou seja, ele passa por todos os elementos desse array. Isso significa que se houver 10 números na entrada de dados,por exemplo, serão realizadas 10 operações, e teremos 10 resultados como saída.
  
- Em relação à Complexidade de Tempo, temos aqui uma taxa de crescimento linear, uma vez que o aumento no tamanho do array faz crescer proporcionalmente o tempo gasto na execução do algoritmo.
  
- Aqui a complexidade de espaço é dada por O(n), porque a saída cresce proporcionalmente a entrada de dados
   
3. Quando calculamos a complexidade de espaço não levamos em consideração o espaço ocupado pela entrada, uma vez que o tamanho da entrada não é algo que podemos, com nosso algoritmo, influenciar. Se falamos em ordem de complexidade sem especificar se é de tempo ou de memória, assuma que é de tempo!

4. Dado o algoritmo linear de complexidade O(n), o seu tempo de espaço é constante na ordem de 0(1), porque o número de entradas é diferente do número de saídas, apenas temos um resultado que é a soma dos números:

```
def sum_array(numbers):
    sum = 0
    for number in numbers:
        sum += number

    return sum
```
   
## Complexidade Quadrática:

1.  Dependendo da forma como um algoritmo é escrito, seu tempo de execução vai ser alterado de acordo com diferentes taxas de crescimento. O tempo de execução dos algoritmos cresce a taxas diferentes.

```
# Os arrays têm sempre o mesmo tamanho
def multiply_arrays(array1, array2):
    result = []
    for number1 in array1:
        for number2 in array2:
            result.append(number1 + number2)

    return result
```

- No algoritmo acima, são recebidos dois arrays de tamanhos iguais e é retornado um novo array, cujos elementos são resultado da soma de cada um dos elementos do array1 com todos os elementos do array2.

- Para cada número do array1 ser somado com todos os números contidos no array2, é necessário que o segundo seja percorrido por inteiro. E isso significa que para array1 e array2 com duas posições, serão necessárias 4 iterações (ou operações), para o algoritmo concluir sua execução. Se cada uma das entradas tiver 3 elementos, serão necessárias 9 operações para a conclusão da execução e assim sucessivamente. Então concluimos que esse algoritmo é de complexidade O(n²), porque sua saída sempre será a entrada ao quadrado. Portanto é uma algoritmo de complexidade quadrática.

## Complexidade Cúbica:

1. Um algoritmo com 3 loops, terá complexidade O(n³), porque terá que realizar 03 operações de varredura, e assim sucessivamente.
   
2. O tempo de execução de um algoritmo cúbico cresce muito mais para uma entrada, muito menor que a do algoritmo linear

## Resumindo:

1. A Ordem de Complexidade diz respeito à taxa de crescimento do tempo de execução (ou espaço de memória ocupado) de um algoritmo, na medida em que aumentamos o tamanho da sua entrada;

2. Uma complexidade é O(1) (constante) é quando o tempo de execução do algoritmo independe do tamanho da entrada;

3. Uma complexidade é O(n) (linear) é quando a taxa de crescimento em seu tempo de execução é linear: se aumentamos a entrada em 2 vezes, aumentamos o tempo de execução em 2 vezes;

4. Uma complexidade é O(n²) (quadrática) é quando a taxa de crescimento do tempo de execução do algoritmo é quadrática: se aumentamos a entrada em 2 vezes, aumentamos o tempo de execução em 4 (ou 2²) vezes;

5. Uma complexidade é O(n³) (cúbica) é quando a taxa de crescimento do tempo de execução do algoritmo é cúbica: se aumentamos a entrada em 2 vezes, aumentamos o tempo de execução em 8 (2³) vezes.

## Complexidade Logaritma:

1. 