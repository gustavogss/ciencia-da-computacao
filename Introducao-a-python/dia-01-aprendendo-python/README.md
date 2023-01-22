# APRENDENDO PYTHON :

1. Python é uma linguagem de programação simples, legível, de alto nível, multiplataforma e orientada a objetos. Já vem nativa no linux e Mac. 
   
2. Serve para:
    - criação de aplicações web;
    - automação de tarefas repetitivas;
    - aplicativos desktop;
    - aplicações para dispositivos móveis (não é muito recomendado).
  
3. O Python traz consigo um conjunto de bibliotecas úteis para diversas tarefas, como manipulação de dados no formato JSON e CSV. Também possui um servidor web simples, ferramenta para emails e muito mais!
   
4. REPL (Read-Eval-Print Loop) é o terminal do Python, ativado quando o comando ** python3 ** é digitado, ou seja é o loop de leitura-avaliação-impressão ou terminal interativo. Ele recebe uma entrada, avalia sua execução e imprime o resultado.
   
5. PEP 8 ou Python Enhancement Proposal 8 - é um documento escrito pela comunidade pythônica para aprimorar e padronizar a legibilidade dos códigos em python.
   
## Como usar a imagem do Python no Docker?

1.  Vamos usar o REPL do Python dentro do Docker

    - Baixe a imagem do python:

    ```
    # Baixe a última versão do python
    docker pull python

    # Baixe uma versão específica
    docker pull python:tag
    ```

2. Para executar o REPL a partir da imagem baixada:

```
docker run -it --rm python

ou 

docker run -it --rm python:tag
```

3. Para executar um script Python usando a imagem de Python do Docker diretamente:
   
   ```
   docker run -it --rm --name nome-do-seu-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python seu-arquivo.py
   ```
4. Para incrementar ou decrementar algum valor no python usamos a expressão 

    ```
    count +=1
    counter = counter + 1
    ou
    count -=1
    counter = counter - 1
    ```

 - Essa expressão não é aceita no python:

    ```
    count++
    ou 
    count--
    ```

5. Operadores de comparação no python and e or:
   
   ```
   True and False
   True or False
   ```
6. A expressão ** 3 // 2 ** desconsidera as casas decimais e retorna apenas os valores inteiros 1 
   
7. Para comentar o código no python usamos a #
   
8. Em python a expressão ** '1' == 1 ** , retorna False, porque são valores de tipos diferentes e nenhuma conversão é realizada
   
9. Operadores de comparação no python: **and** e **or** 
    
    ```
    temperatura < 25 and temperatura > 18

    idade <= 5 or idade >= 65
    ```

### Tipos de Dados embutidos

1. Os valores booleanos **True** e **False** pertencem ao tipo embutido bool
   
2. O método **type(operando)** serve para verificar qual é o tipo do elemento.
   
3. O método **help(comando)** nos dá a lista de comandos no Python
   
   ```
    help(list)
   ```
   
4. O comando help() também pode ser utilizado em cláusulas if ou for, desde que colocado entre aspas e para sair de dentro do comando, basta apertar a tecla q
   
   ```
    help("if")
   ```
5. Outras estruturas de dados:
- sequência(list, tuple, range);
- conjuntos(set, frozenset);
- mapeamento(dict);
- sequências binárias(bytes, bytearray, memoryview)
  
### Listas (list): entidades relacionadas

1. Uma lista ou um array é uma sequência mutável e ordenada de elementos. Ela pode armazenar elementos heterogêneos, ter seu tamanho variável e crescer à medida que itens são adicionados.
   
2. O método append serve para adicionar elementos na lista
   
   ```
    frutas = ['banana', 'maça']
    frutas.append('uva')
   ```
3. O método remove serve para remover elementos na lista
   
   ```
    frutas = ['banana', 'maça']
    frutas.remove('uva')
   ```
4. A herança funciona em uma lista com o método **extends**
   
   ```
    frutas2.extends(frutas)
    ou
    frutas2.extends(['pêra', 'abacaxi'])
   ```
5. Outros métodos:

```
frutas.index("maçã")  #retorna o índice onde a fruta está localizada, neste caso, 1
```

```
frutas.sort()  #ordena a lista de frutas
```

6. all() - verifica se na lista tem todas as strings preenchidas ou numeros diferentes de zero 0:

```
alunos1 = ["joão", "pedro"]
alunos2 = ["joão", " "]
alunos3 = ["joão", ""]

all(aluno1) # retorna True
all(aluno2) # retorna True, porque o último elemento tem um espaço e portanto não está vazio
all(aluno3) # retorna False, porque o último elemento está vazio
```
```
numeros1 = [1,2,3]
numeros2 = [1,0,2]

all(numeros1) # retorna true
all(numeros2) # retorna false, porque tem um elemento com valor 0 na lista
```

7. any() - retorna true se qualquer um dos elementos for true, ou seja, se a string estiver preenchida ou se o numero for diferente de 0

8. len() - função que retorna o número de itens

```
numeros = [0,2,6]

len(numeros) # 3
```
   
9.  max() - função que retorna o maior item

```
numeros = [0,2,6]

max(numeros) # 6
```

10. min() - função que retorna o menor item

```
numeros = [0,2,6]

min(numeros) # 0
```

### Tuplas (tuple): uma única entidade

1. São semelhantes as listas[], porém com o uso de (). Também não podem ser modificadas durante a execução do programa
   
   ```
   user = ('Will', 'Marcondes', 42)  #elementos são definidos separados por vírgula, envolvidos por parênteses
   ```
   ``` 
    user[0]  # acesso também por índices
    ```
    ```
    user.append(('Marcos', 'Apollo', 38)) #[('Will', 'Marcondes', 42),('Marcos', 'Apollo', 38)] - temos uma lista de tuplas
   ```
    - A tupla pode ser usada como chave do dicionário por ser imutável

   ### Dicionários (dict): associação de chave e valor

   1. Estrutura que associa uma chave a um determinado valor. Um objeto no javascript.
   
   ```
   people_by_id = {
    1: "Maria", 
    2: "Fernanda", 
    3: "Felipe"
    }      
   ```
    - elementos no formato "chave: valor" separados por vírgula, envolvidos por chaves
   
   - elementos são acessados por suas chaves
  
   ```
    people_by_id[1]  # saída: Maria
   ```
   - elementos podem ser removidos com a palavra chave del
    
   ```
   del people_by_id[1]
   ```

   ### Conjuntos (set): para fazer operações entre conjuntos

   2. Coleção de elementos únicos e não ordenados. Implementam operações de união, intersecção e outras. São implementados por meio de {}

    ```
    permissions = {"member", "group"}  # elementos separados por vírgula, envolvidos por chaves

    permissions.add("root")  # adiciona um novo elemento ao conjunto

    permissions.add("member")  # como o elemento já existe, nenhum novo item é adicionado ao conjunto

    permissions.union({"user"})  # retorna um conjunto resultado da união

    permissions.intersection({"user", "member"})  # retorna um conjunto resultante da intersecção dos conjuntos

    permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos
    ```

    ### Conjuntos imutáveis (frozenset):

   3. É uma variação dos conjuntos, porém imutável, ou seja, seus elementos não podem ser modificados durante a execução do programa.
   
   ```
    permissions = frozenset(["member", "group"])  # assim como o set, qualquer estrutura iterável pode ser utilizada para criar um frozenset

    permissions.union({"user"})  # novos conjuntos imutáveis podem ser criados à partir do original, mas o mesmo não pode ser modificado

    permissions.intersection({"user", "member"})  # retorna um conjunto resultante da intersecção dos conjuntos

    permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos
   ```

     ### Range (range)
   
    1. Estrutura capaz de gerar uma sequência numérica de um valor inicial até um valor final, modificando seu valor de acordo com o passo (step) definido.  em que start e step podem ser omitidos, possuindo valores iniciais iguais a 0 e 1 respectivamente.
   
    - Seus valores são criados à medida que esta sequência é percorrida.
   
   ```
   - vamos converter o range em uma lista para ajudar na visualização

   - definimos somente o valor de parada
    list(range(5))  # saída: [0, 1, 2, 3, 4]

   - definimos o valor inicial e o de parada
    list(range(1, 6))  # saída: [1, 2, 3, 4, 5]

   - definimos valor inicial, de parada e modificamos o passo para 2
    list(range(1, 11, 2))  # saída: [1, 3, 5, 7, 9]

   - podemos utilizar valores negativos para as entradas também
    list(range(10, 0, -1))  # saída: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
   ```

   ## Estrutura de Repetição For:

   1. For é um dos comandos usado para percorrer uma lista no Python:

   ```
   restaurants = [
       {"name": "Restaurante A", "nota": 4.5},
       {"name": "Restaurante B", "nota": 3.0},
       {"name": "Restaurante C", "nota": 4.2},
       {"name": "Restaurante D", "nota": 2.3},
]
   for restaurant in restaurants:
      if restaurant['nota'] > 3:
         filter_restaurant.append(restaurant)
      print(filter_restaurant)
   ```
   - O programa vai varrer toda a lista de restaurants e imprimir aqueles restaurants que tiverem a nota maior que 3. 

   - Para cada repetição do nosso laço, um novo elemento da estrutura iterável é atribuído a variável de iteração.

   2. Em alguns casos, podemos ainda querer percorrer uma sequência numérica, e para isto iteramos sobre a estrutura de dados range:

   ```
   for index in range(5):
       print(index)
   ```

   3. Além de listas, várias outras estruturas são iteráveis, como strings (str), tuplas (tuple), conjuntos (set), dicionários (dict) e até mesmo arquivos. 

   ### Compreensão de lista (list comprehension)

   1. É uma maneira concisa de criação que executa uma operação em cada item da lista já existente

   2. Quando uma nova lista é criada como resultado de uma iteração, podemos simplificar utilizando compreensão de listas:

   ```
   min_rating = 3.0
   filtered_restaurants = [restaurant
                         for restaurant in restaurants
                         if restaurant["nota"] > min_rating]
   print(filtered_restaurants)  
   ```

   3. Cria uma nova lista de strings com os nomes que contém a letra ‘a’:

   ```
   names_list = ['Duda', 'Rafa', 'Cris', 'Yuri']
   new_names_list = [name for name in names_list if 'a' in name]

   print(new_names_list)
   ```

   4. Uma compreensão de listas para criar uma lista com o quadrado dos números entre 1 e 10:

   ```
   quadrados = [x*x for x in range(11)]
   print(quadrados)
   ```

   ## Estrutura de Repetição While:

   1. A lista será percorrida até uma condição ser atendida. Veja o exemplo para uma sequência Fibonacci:

   ```
   n = 10
   last, next = 0, 1
   while last < n:
      print(last)
      last, next = next, last + next
   ```

   ## Estrutura de Repetição enumerate:

   1. Quando se quer que uma variável mude em cada iteração do loop. Ao invés de criar e incrementar uma variável, podemos usar enumerate() do Python para obter um contador e o valor do iterável ao mesmo tempo:

   ```
   languages = ['Python', 'Java', 'JavaScript']

   enumerate_prime = enumerate(languages)

   - converte um objeto enumerate em uma lista
   print(list(enumerate_prime))

    - Saída: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]
   ```

   2.  Desestruturando (unpack) os itens da lista ou tupla:

   ```
   languages = ['Python', 'Java', 'JavaScript']

      for index, language in enumerate(['Python', 'Java']):
      print(f'{index} - {language}')

      - Saída:
      0 - Python
      1 - Java
   ```

## Funções

1. As funções são definidas através da palavra reservada def, seguida por um nome e os parâmetros entre parênteses.

2.  Todo bloco de código em Python, o caractere : define o início do bloco, e a indentação define seu fim.

3. Os parâmetros podem ser passados de forma:

- posicional: são aqueles definidos por meio da posição em que cada um é passado;
- nomeada: são definidos por meio de seus nomes.

```
def soma(x, y):
    return x + y

soma(2, 2)  # os parâmetros aqui são posicionais

soma(x=2, y=2)  # aqui estamos nomeando os parâmetros
```

4. Os parâmetros também podem ser variádicos, ou seja, variam em sua quantidade. Parâmetros posicionais variádicos são acessados como uma tupla no interior de uma função, e parâmetros nomeados variádicos como um dicionário:

```
def concat(*strings):
    # Equivalente a um ", ".join(strings), que concatena os elementos de um iterável em uma string utilizando um separador

    # Nesse caso a string resultante estaria separada por vírgula

    final_string = ""
    for string in strings:
        final_string += string
        if not string == strings[-1]:
            final_string += ', '
    return final_string

# pode ser chamado com 2 parâmetros

concat("Carlos", "Cristina")  # saída: "Carlos, Cristina"

# pode ser chamado com um número n de parâmetros

concat("Carlos", "Cristina", "Maria")  # saída: "Carlos, Cristina, Maria"

# dict é uma função que já vem embutida no python

dict(nome="Felipe", sobrenome="Silva", idade=25)  # cria um dicionário utilizando as chaves passadas

dict(nome="Ana", sobrenome="Souza", idade=21, turma=1)  # o número de parâmetros passados para a função pode variar
```

5. As variáveis definidas dentro das funções tem escopo local. Porém, quando uma função não encontra um nome no escopo local, ela irá procurar no espaço de nomes global.

6. Em alguns casos, podemos querer limitar um parâmetro em nomeado ou posicional para evitar ambiguidades e/ou aumentar legibilidade

```
len([1, 2, 3, 4])  # função len não aceita argumentos nomeados

len(obj=[1, 2, 3, 4])  # este código irá falhar

print("Coin", "Rodrigo", ", ")  # imprime Coin Rodrigo ,

print("Coin", "Rodrigo", sep=", ")  # nomeando o terceiro parâmetro, agora temos a saída: Coin, Rodrigo
``` 

## Arquivos em Python:

1. Todo arquivo com extensão .py, e é um módulo. Os Módulos são declarados utilizando snake case, ou seja, com nomes minúsculos e quando possuírem mais de uma palavra, devem ser separadas por underscore (_)

## Docstring?

1. As docstrings ''' ou """ no Python são os literais de string que aparecem logo após a definição de uma função, método, classe ou módulo:

```
def quadrado(n):
    '''Recebe um número n, retorna o quadrado de n''' # Literal de string
    return n**2
```

2. São usados para documentar o código e podemos acessar essas docstrings usando o atributo __doc__

```
def quadrado(n):
    '''Recebe um número n, retorna o quadrado de n''' # Literal de string
    return n**2
print(quadrado.__doc__)

# Saída
Recebe um número n, retorna o quadrado de n
```

3. Docstrings para a função print() integrada:

```
print(print.__doc__)

# Saída
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Imprime os valores em um fluxo, or em sys.stdout por padrão.
Argumentos de palavras-chave opcionais:
file: um objeto semelhante a um arquivo (fluxo); o padrão é o sys.stdout atual.
sep: string inserida entre valores, o padrão é o espaço.
end: string anexada após o último valor, o padrão é uma nova linha.
flush: se deve forçar a descarga do fluxo.
```



