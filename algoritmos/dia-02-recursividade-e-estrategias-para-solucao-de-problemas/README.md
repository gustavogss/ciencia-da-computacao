# RECURSIVIDADE E ESTRATÉGIAS PARA SOLUÇÃO DE PROBLEMAS :

1. Com a recursividade, conseguimos solucionar alguns problemas de forma mais simplificada e harmoniosa, diminuindo assim a complexidade de escrita do código. É utilizada em situações nas quais o código fica com complexidade baixa, se comparado ao código da solução iterativa, para o mesmo problema.

2. Recursividade - é o processo que usamos quando uma função chama a si mesma.
   
3. Principios da Recursividade:
   - A função deve chamar a si mesma;
   - Sempre temos uma condição de parada;
   - O algoritmo recursivo sempre deve andar em direção ao caso base.

4. A recursão é utilizada para deixar a resposta mais clara.
   
5. O algoritmo recursivo tem duas partes:
   - O caso base: quando a função deve parar;
   - O caso recursivo: quando a função chama a si mesma.

6. A função fatorial f! é uma recursiva, porque chama a sim mesmo.
   
## A pilha de chamadas:

1. E uma pilha temos duas ações: Inserir(push) e Retirar(pop). E todas essas ações são realizadas no topo da pilha.
   
2.  Pilha de chamadas ou call stack - registra a execução das funções, ou seja, qual está sendo executada, em que ponto ela deve retornar, qual é a proxima a ser chamada.
   
## Iterativo x Recursivo

1.  É possível ter funções tanto recursivas, quanto iterativas para o mesmo problema.
   
- Escolher entre uma solução recursiva ou iterativa depende muito do que estamos buscando;
  
- Escolher uma solução recursiva não significa ganho de performance, muito pelo contrário, grande parte das vezes, a solução iterativa será mais performática.

- Escolher a solução recursiva terá um ganho na diminuição de complexidade do código do seu projeto. Aqui, complexidade significa legibilidade. Ou seja, nosso código fica mais simples, mais harmonioso, quando utilizamos a recursividade. 

## Análise de algoritmos recursivos

1. Para que consigamos realizar a análise de algoritmos recursivos, iremos fazer o uso da Árvore de Recorrência! E essa árvore - É um modo de analisarmos o custo do algoritmo

```
def fibonacci(num):  # nome da função e parâmetro
    if (num <= 1):  # condição de parada
        return num
    else:
        return fibonacci(num - 2) + fibonacci(num - 1)  # chamada de si mesma com um novo valor
```

## Principais cuidados ao usar recursão

1. Quando um loop recursivo é muito grande, ele fará muitas chamadas, e podemos ter um stack overflow ou estouro de pilha, podendo ficar sem memória para continuar com a execução do programa.
   
2. Para evitar um estouro de pilha, devemos implementar a condição de parada na função.
   
3. Apesar de funções recursivas serem mais harmoniosas e fáceis de implementar, elas costumam ser menos eficientes que do que as iterativas, por causa do overhead de empilhar e desempilhar chamadas de funções.

## Estratégias para solução de problemas

1. **Iterativa** - A solução iterativa é caracterizada pela repetição de uma determinada operação, procurando resolver algum problema encontrando sucessivas aproximações, a partir de uma suposição inicial.

- A ideia nesse tipo de processo é repetir um determinado cálculo várias vezes, obtendo-se a cada repetição, ou iteração, um resultado mais preciso que aquele obtido na iteração anterior.
  
- A cada iteração, utiliza-se o resultado da anterior como parâmetro de entrada para o cálculo seguinte. O resultado é uma sequência de valores aproximados, não exatos, mas que estão dentro de uma faixa de erro aceitável.
  
2. **Força bruta** - A força bruta, também conhecida como tentativa e erro ou busca exaustiva, é a estratégia mais trivial e intuitiva para solução de problemas. Ela consiste basicamente em enumerar todas as combinações possíveis para uma solução e avaliar se satisfazem o problema.

- Em alguns casos, a força bruta possui desempenho geralmente ruim.

- Um método baseado em tentativa e erro testaria todas as combinações entre elementos checando:

- Se a solução é viável;

- Se a solução possui valor melhor que outra encontrada anteriormente.

- Para conseguir definir qual seria a melhor solução, todas devem ser enumeradas e registradas, e, ao final, os caminhos que não chegaram a um solução final, devem ser retirados.

3. **Dividir e conquistar** - consiste em dividir o problema em partes menores, encontrar soluções para as partes, e só então combinar as soluções obtidas em uma solução global.

- Usar essa estratégia para resolver problemas, nos quais os subproblemas são versões menores do problema original, geralmente leva à soluções eficientes e harmoniosas, especialmente quando é utilizado a recursividade.
  
- A estratégia emprega modularização de programas e frequentemente conduz a um algoritmo simples e eficiente. Esta técnica é bastante utilizada em desenvolvimento de algoritmos paralelos, onde os subproblemas são tipicamente independentes um dos outros, podendo assim serem resolvidos separadamente.
  
4. A técnica de Divisão e Conquista consistem em três passos:

- Divisão: dividir a instância do problema original em duas ou mais instâncias menores, considerando-as como subproblemas;

- Conquista: resolver cada subproblema recursivamente;

- Combinação: combinar as soluções encontradas em cada subproblema, compondo uma solução para o problema original.

5. Um exemplo para ilustrar o uso dessa técnica é o algoritmo de ordenação de um vetor por intercalação, ou, como é chamado, MergeSort. Sua representação pode ser feita por meio de uma árvore binária.
