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
