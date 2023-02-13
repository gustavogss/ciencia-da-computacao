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

1. É representado pela notação O(log n), um algoritmo logarítmico tem uma alteração na taxa de execução que, geralmente, reduz pela metade o tempo de finalização das iterações ao reduzir pela metade o tamanho do input a cada iteração.
   
2. Suponha que temos um algoritmo cuja entrada n é igual a 4, se tivermos um algoritmo O(log n) a ser executado com essa entrada, teremos que fazer apenas 2 operações para executá-lo, pois log₂n (lê-se: “log de n na base 2”) é igual a 2. Se a nossa entrada fosse o dobro, ou seja, 8 teríamos que realizar apenas 3 operações para chegar ao fim da execução. Ao dobrar o valor da entrada novamente, com n igual a 16, teríamos que realizar apenas 4 operações (log₂n é igual a 4) e assim sucessivamente.
   
3. O número de operações para executar o algoritmo logarítmico tem uma relação inversa ao tamanho da entrada: quanto maior ela é, menor o número de operações e, consequentemente, menor o tempo para a execução do algoritmo!

4. Como exemplo de um algoritmo de complexidade O(log n), podemos citar: um algoritmo de lista telefônica. Temos uma lista de nomes de tamanho n, ordenada em ordem alfabética, e um nome T; devemos encontrar o número de telefone da pessoa passada na entrada:
   
- Buscar na página (ou posição) da lista que tenha nomes começando com a letra T;
- Escolher uma página aleatória da lista para abrir;
- Percebemos que caímos na posição da letra M;
- Como M < T, na ordem alfabética, então, devemos avançar algumas posições para encontrar o T;
- Então, escolhemos uma página que está mais adiante;
- Percebemos que caímos na posição da letra V;
- Como V > T, na ordem alfabética, então devemos voltar alguns posições;
- Vamos repetimos esse processo até encontrarmos o nome desejado.
  
5. Existe uma outra forma de fazermos essa busca por um nome sequencialmente na lista, mas é uma forma muito mais trabalhosa percorrendo página por página, teríamos que realizar várias operações.
   
6. Exemplo de um algorito de complexidade logaritímica:
   
    ```
   # A estrutura deve estar ordenada para que a busca binária funcione
    def binary_search(numbers, target):
      # definir os índices
         start = 0
        end = len(numbers) - 1

        while start <= end: # os índices podem ser no máximo iguais, o início não pode ultrapassar o fim
        mid = (start + end) // 2 # encontro o meio

            if numbers[mid] == target: # se o elemento do meio for o alvo, devolve a posição do meio
                 return mid
        
            if target < numbers[mid]: # se o elemento for menor, atualiza o índice do fim
            end = mid - 1
            else: # caso contrário, atualiza o índice do inicio
            start = mid + 1
    
        return -1 # Não encontrou? Retorna -1

    numbers = [2, 3, 4, 10, 40]
    target = 40

    result = binary_search(numbers, target)
    print(f"Elemento encontrado na posição: {result}")

    ```

- A cada iteração, o algoritmo de busca binária corta o problema pela metade:

- Primeiro ele “corta” a lista em dois e pega o elemento do meio.
- Depois ele “caminha” para o lado no elemento que procura esta e “corta” este lado novamente pela metade.

7. Um logaritmo em base 2 representa o número de vezes que um valor deve ser dividido pela metade para obter 1.

8. Um algoritmo logarítmico tem uma performance muito superior em relação a um linear, porque divide as operações pela metade.
   
9.  A busca binária tem complexidade O(log n), uma vez que reduz pela metade o número de elementos que deverá percorrer a cada nova iteração. Todavia, ela só deve ser utilizada quando lidamos com **arrays que já se encontram ordenados**, este é o caso do nosso array2. Uma vez que a busca binária precisará ser executada n-vezes para cada elemento em array1, partimos da operação O(n) * O(log n), que resulta em O(n log n). Uma possível representação abstrata do problema é a seguinte:

```
def do_something(array1, array2):
    for number in array1: # O (n)
        binary_search(array2, number) # O (log n)
```

## Complexidade Exponencial e Fatorial:

1. Essas complexidades caracterizam algoritmos que, para aumentos pequenos no tamanho da entrada, aumentam enormemente o número de operações a serem realizadas para serem executados e, consequentemente, seu tempo de execução.
   
   - Exponencial: 2ⁿ (O(2ⁿ))

   - Fatorial: n! (O(n!))
  
2. No caso de um algoritmo com Ordem de Complexidade Exponencial, para uma entrada de dados n que possui vinte elementos, o algoritmo realizará aproximadamente um milhão (ou 2²⁰) de operações. Para o caso fatorial, os mesmos vinte elementos rendem 24 quatrilhões de operações! (O número exato é: 2432902008176640000 operações 😨).
   
## Analisando Algoritmos:

```
def calculations(n):
    number1 = 0
    for n1 in range(n):
        number1 += n1

    number2 = 0
    for n1 in range(n):
       for n2 in range(n):
            number2 += n1 + n2

    number3 = 0
    for n1 in range(n):
       for n2 in range(n):
           for n3 in range(n):
               number3 += n1 + n2 + n3

    return number1, number2, number3

n1, n2, n3 = calculations(100)
print(f'{n1}, {n2}, {n3}')
```

- Esse algoritmo tem três estruturas de repetição: uma linear, uma quadrática e uma cúbica. Qual é a Ordem de Complexidade dele? 
Seria O(n + n² + n³), lembrando que se os loops estão aninhados você os multiplica, e se estão paralelos você os soma. 

- Para calcular a análise de complexidade dessa algoritmo, basta pegar a estrutura de maior ordem de complexidade (o pior caso) e desconsiderar os múltiplos: O(n³)
  
## Melhor caso, pior caso e caso médio:

1. Isso quer dizer: A depender da minha entrada, o meu algoritmo pode executar em O(1) ou O(n)
   
2. Analisando o algoritmo:

```
def linear_search(numbers, target):
    n = len(numbers) # N será a quantidade de elementos da lista
    for index in range(0, n): # vamos iterar a lista completa
        if numbers[index] == target: # se encontrar o elemento alvo, retorne a posição
            return index

    return -1 # Não encontrou? Retorne -1


print(linear_search([1, 2, 3], 2))  # saída: 1
print(linear_search([1, 2, 3], 4))  # saída: -1 
```

- Nesse caso, mesmo para uma entrada infinita, nossa complexidade será O(1). Esse é o melhor caso desse algoritmo. De forma análoga, o pior caso é o número ser o último elemento do array, ou seja O(n).

- O caso médio aqui seria algo como O(n * 1/2), por exemplo. Nesse caso, o número que procuramos está no meio da lista. Mas, para entradas muito grandes, aprendemos a desprezar os números menos relevantes da soma, então, podemos simplificar e dizer que o caso médio é O(n) também.

3. Diferentes algoritmos têm diferentes cenários de melhor caso, pior caso e caso médio
   
4. Problemas que não têm solução conhecida em tempo polinomial, e que podem ser resolvidos apenas com força bruta, com complexidades exponencial ou fatorial, são chamados NP Completo.

## Quais as complexidades dos algoritmos?

- Constantes: O(1);
- Logarítmicos: O(log n);
- Linear: O(n);
- Quadráticos: O(n²);
- Cúbicos: O(n³);
- Exponencial: O(2ⁿ);
- Fatorial: O(n!).

