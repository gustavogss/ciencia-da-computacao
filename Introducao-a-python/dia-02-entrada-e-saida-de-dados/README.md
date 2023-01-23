# ENTRADA E SAÍDA DE DADOS :

1. Os arquivos CSV e JSON, nos permitem persistir dados no Python. O JSON é normalmente utilizado para comunicação entre sistemas e o CSV é geralmente utilizado no contexto da Ciência de Dados.
   
2. Todo arquivo que é escrito com a linguagem Python e com a extensão .py é considerado um módulo
   
3. Pacotes são módulos Python que contêm outros módulos e/ou pacotes:
   
   ```
    import http  # importa o pacote http como um módulo

    from http import client  # importa o módulo client do pacote http

    from http.client import HTTP_PORT  # importa a constante HTTP_POST do módulo client do pacote http
   ```

4. O venv é um módulo já embutido na linguagem Python, que serve para isolar ambientes de projetos. Ou seja, é possível ter dois projetos rodando em dois ambientes diferentes, que podem ter versões diferentes de uma mesma biblioteca.
   
5. O comando para criação deste ambiente isolado é **python3 -m venv .vm**, sendo que .vm é o nome do ambiente isolado. Este comando deve ser executado na raiz do projeto.

- O comando para instalar o venv caso ele não venha instalado no Python é o:
  
  ```
  sudo apt install python3-venv
  ```
- Para ativar o ambiente .vm, devemos digitar o seguinte comando:

  ```
    source .vm/bin/activate
  ```
- Para conferir se o ambiente .vm, foi ativado basta digitar:

  ```
    which python3 # O resultado será o caminho para a pasta onde você criou seu ambiente virtual (pwd), acrescido de .vm/bin/python3
  ```
- Para desativar o ambiente .vm, basta digitar:

  ```
    deactivate
  ```
## Entrada e Saída:

1. Para entrada de texto, usamos o comando:
   
   ```
   input("Digite uma mensagem:")
   ```
2. Para entrada de número, usamos o comando:
   
   ```
   input(int("Digite um número:"))
   ```
3. Para entrada de valores decimais, usamos o comando:
   
   ```
   input(float("Digite sua altura:"))
   ```
4. Uma maneira de recebermos valores externos na execução de nossos programas é utilizando o módulo sys. Quando executamos um script e adicionamos parâmetros, os mesmos estarão disponíveis através de uma variável chamada sys.argv, que é preenchida sem que precisemos fazer nada. Na prática, podemos escrever o conteúdo abaixo em um arquivo e passar alguns parâmetros ao executá-lo:

    ```
    import sys

    if __name__ == "__main__":
        for argument in sys.argv:
            print("Received -> ", argument)
    ```
    - Para executar esse código, digitamos **python3 arquivo.py 2 4 "teste"**
    - Logo teremos a saída:

    ```
    Received ->  arquivo.py
    Received ->  2
    Received ->  4
    Received ->  teste
    ```
5. print() - é a principal função para a saída de dados no Python.
   - Ela pode ser chamada utlizando separadores:

    ```
    print("Maria", "João", "Miguel", "Ana", sep=", ")  # saída: Maria, João, Miguel, Ana
    ```
6. Existe um parâmetro que nos permite modificar a saída padrão para a saída de erros:
   
   ```
   import sys

    err = "Arquivo não encontrado"
    print(f"Erro aconteceu: {err}", file=sys.stderr)
    ```

## Desempacotamento de Valores:

1. É um recurso que serve para separar os valores recebidos em variáveis diferentes. Quando há uma atribuição múltipla e o valor da direita pode ser percorrido, o Python entende que deve atribuir cada um dos valores a uma variável da esquerda, seguindo a ordem:

    ```
    a, b = "cd"
    print(a)  # saída: c
    print(b)  # saída: d

    head, *tail = (1, 2, 3) # Quando um * está presente no desempacotamento, os valores são desempacotados em formato de lista.
    print(head)  # saída: 1
    print(tail)  # saída: [2, 3]
    ```

## Manipulação de arquivos

1. Podemos manipular arquivos, mas é preciso sempre fechar o arquivo após operá-lo.

- a função **open()**  é a responsável por abrir um arquivo, tornando possível sua manipulação. Seu único parâmetro obrigatório é o nome do arquivo.

2. Arquivos são abertos somente para leitura, mas podemos modificar isto passando o modo com que vamos abrir o arquivo. Com o mode="w", estamos abrindo o arquivo para escrita:

    ```
    file = open("arquivo.txt", mode="w")  # ao abrir um arquivo para escrita, um novo arquivo é criado mesmo que ele já exista, sobrescrevendo o antigo.
    ```

- Para escrevermos um conteúdo em um arquivo utilizamos a função write:

    ```
    # file = open("arquivo.txt", mode="w")

    file.write("nome idade\n")
    file.write("Maria 45\n")
    file.write("Miguel 33\n")

    file.close()
    ```
  - Só é possível escrever em um arquivo após abri-lo em um modo que permita escrita
  - O programa ao ser executado, será criado um arquivo com a extensão txt, como o nome da lista 

3. Assim como podemos redirecionar a saída do nosso programa para a saída de erros, podemos redirecionar o conteúdo digitado dentro de print para um arquivo. Ou seja, também podemos escrever em um arquivo através do print.

    ```
    #
    # file.write("Miguel 33\n")

    # Não precisa da quebra de linha, pois esse é um comportamento padrão do print
    print("Túlio 22", file=file)
    ```
4. Para escrever múltiplas linhas podemos utilizar a função writelines. Repare que a função espera que cada linha tenha seu próprio caractere de separação (\n):
   
   ``` 
    # print("Túlio 22", file=file)

    LINES = ["Alberto 35\n", "Betina 22\n", "João 42\n", "Victor 19\n"]
    file.writelines(LINES)
    ```
5. Ao abrir um arquivo para manipularmos, temos que fechá-lo **file.close()**, porque a manipulação de arquivos é feita através de buffers. Ou seja, a escrita em disco pode não ser imediata. Quando fechamos o arquivo, garantimos que tudo aquilo que ainda não está escrito seja persistido.

6. A função **read()** serve para lermos conteúdo de um arquivo:

    ```
    # escrita
    file = open("arquivo.txt", mode="w")
    file.write("Trybe S2")
    file.close() # fechando o arquivo da escrita

    # leitura
    file = open("arquivo.txt", mode="r")
    content = file.read()
    print(content)
    file.close()  # fechando o arquivo da leitura
    ```

7. Um arquivo é também um iterável, ou seja, pode ser percorrido em um laço de repetição. A cada iteração, uma nova linha é retornada:
   
   ```
    # escrita
    file = open("arquivo.txt", mode="w")
    LINES = ["Olá\n", "mundo\n", "belo\n", "do\n", "Python\n"]
    file.writelines(LINES)
    file.close()

    # leitura
    file = open("arquivo.txt", mode="r")
    for line in file:
        print(line)  # não esqueça que a quebra de linha também é um caractere da linha
    file.close()  # não podemos esquecer de fechar o arquivo
   ```
8. Podemos também ler e alterar arquivos binários, e para isso utlizamos o **mode='wb' - para escrita e o mode='wr' - para leitura**:
   
   ```
   # escrita
    file = open("arquivo.dat", mode="wb")
    file.write(b"C\xc3\xa1ssio 30")  # o prefixo b em uma string indica que seu valor está codificado em bytes
    file.close()

    # leitura
    file = open("arquivo.dat", mode="rb")
    content = file.read()
    print(content)  # saída: b'C\xc3\xa1ssio 30'
    file.close()  # não podemos esquecer de fechar o arquivo
    ```

## Lidando com exceções

1. Há pelo menos dois tipos de erros que podem ser destacados no Python: erros de sintaxe e exceções.
   
   - Erros de Sintaxe: ocorrem quando o código utiliza recursos inexistentes da linguagem que não consegue interpretá-los. É como executar print{"Olá, mundo!"} em vez de print("Olá, mundo!")
  
   - Exceções: ocorrem durante a execução e resultam em mensagem de erro:

    ```
    print(10 * (1 / 0))
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # ZeroDivisionError: division by zero

    print(4 + spam * 3)
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # NameError: name 'spam' is not defined

    print('2' + 2)
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # TypeError: can only concatenate str (not "int") to str
    ```
   
## Tipos de Erros no Python

1. AssertionError - é levantado quando uma instrução assert falha:
   
   ```
   animal1 = 'cachorro'
   animal2 = 'gato'
   assert animal1 == animal2
   ```
   ```
   # saída
   Traceback (most recent call last):
    File "type_erros.py", line 3, in <module>
    assert animal1 == animal2
    AssertionError
   ```
2. AttributeError - é executado quando fazemos uma referência que não existe:
   
   ```
   class Pessoa():
      nome='Gustavo'
   print(Pessoa.idade) #O atributo idade não existe
   ```
   ```
   Traceback (most recent call last):
   File "type_erros.py", line 7, in <module>
    print(Pessoa.idade)
   AttributeError: type object 'Pessoa' has no attribute 'idade'
   ```
3. TypeError - é lançado quando executamos tipos não compatíveis:

   ```   
   print('10' + 10) # Não podemos somar uma string com um número
   ```
   ```   
   Traceback (most recent call last):
   File "type_erros.py", line 14, in <module>
    print('10' + 10)
   TypeError: can only concatenate str (not "int") to str
   ```
4. EOFError - é levantado quando a função input() chega no fim do arquivo e não consegue lê nenhum dado
   
5. ImportError - é executado quando importa alguma biblioteca que não existe

    ```
    from collections import cdb
    ```
    ```
    Traceback (most recent call last):
    File "type_erros.py", line 25, in <module>
    from collections import cdb
    ImportError: cannot import name 'cdb' from 'collections' (/usr/lib/python3.8/collections/__init__.py)
    ```
6. ModuleNotFoundError - é executado quando o módulo é importado sem ter sido instalado:

      ```
      import scikitlearn
      ```
      ```
      Traceback (most recent call last):
        File "type_erros.py", line 29, in <module>
          import scikitlearn
      ModuleNotFoundError: No module named 'scikitlearn'
      ```
7. IndexError - é levantado quando o indice não existe

      ```
      frutas = ['banana', 'pêra']
      print(frutas[2])
      ```
      ```
      Traceback (most recent call last):
        File "type_erros.py", line 31, in <module>
          print(frutas[2])
      IndexError: list index out of range
      ```

8. KeyError - é levantado quando uma chave de mapeamento não é encontrada no conjunto de chaves existentes

      ```
      dicionario = {'nome':'Gustavo'}
      print(dicionario['idade'])
      ```
      ```
      Traceback (most recent call last):
      File "type_erros.py", line 36, in <module>
      print(dicionario['idade'])
      KeyError: 'idade'
      ```

9. NotImplementerError - é levantado quando uma função ainda não foi implementada 

### Tratamento de exceções:

1. Para tratarmos exceções no Python utilizamos o **try  except**
   
   - Se nenhuma exceção ocorrer, a cláusula except é ignorada e a execução da instrução try é finalizada.
  
   - Se ocorrer uma exceção durante a execução da cláusula try, as instruções remanescentes na cláusula são ignoradas. Se o tipo da exceção ocorrida tiver sido previsto em algum except, então essa cláusula será executada.
  
  - Se não existir nenhum tratador previsto para tal exceção, trata-se de uma exceção não tratada e a execução do programa termina com uma mensagem de erro.
  
      ```
      while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
      ```
      
## Lidando com exceções enquanto manipulamos arquivos:

1. Vamos ver agora como podemos nos prevenir de possíveis erros que ocorrem quando manipulamos arquivos. Sempre devemos fechar um arquivo e podemos, em um bloco try, fazer isso utilizando a instrução **finally** ou **else**. 
   
2. O finally é uma outra cláusula do conjunto try, cuja finalidade é permitir a implementação de ações de limpeza, que sempre devem ser executadas independentemente da ocorrência de ações. 
   
3. O else ocorre sempre que todo o try for bem sucedido.

    ```
    try:
        arquivo = open("arquivo.txt", "r")
    except OSError:
        # será executado caso haja uma exceção
        print("arquivo inexistente")
    else:
        # será executado se tudo ocorrer bem no try
        print("arquivo manipulado e fechado com sucesso")
        arquivo.close()
    finally:
        # será sempre executado, independentemente de erro
        print("Tentativa de abrir arquivo")
    ```

    - Como estamos abrindo o arquivo em modo de leitura, uma exceção será levantada caso ele não exista, executando as cláusulas except e finally. Entretanto, se alterarmos o modo para escrita, o arquivo será criado mesmo se inexistente, executando as cláusulas else e finally.
  
4. O **with** é a palavra reservada para gerenciamento de contexto. Este gerenciamento (with) é utilizado para encapsular a utilização de um recurso, garantindo que certas ações sejam tomadas independentemente se ocorreu ou não um erro naquele contexto.

- A função **open** retorna um objeto que se comporta como um gerenciador de contexto de arquivo que será responsável por abrir e fechar o mesmo. Isto significa que o arquivo possui mecanismos especiais que, quando invocados utilizando with, alocam um determinado recurso — um arquivo — e o liberam quando o bloco for finalizado

    ```
    # Criamos um contexto, limitando o escopo onde o arquivo está aberto.
    # O uso do "as" aqui é somente para atribuir o valor utilizado no contexto à variável file
    with open("arquivo.txt", "w") as file:
        file.write("Michelle 27\n")
    # como estamos fora do contexto, o arquivo foi fechado
    print(file.closed)
    ```  
## Manipulando arquivos JSON:

1. JSON é um formato textual muito utilizado para integração de sistemas. É baseado em regras JavaScript, embora seja independente de linguagem. É muito utilizado para a comunicação back-end e front-end, e comunicação com sistemas externos (gateways de pagamento) ou internos (como um sistema de autenticação
   
2. A linguagem Python já inclui um módulo para manipulação desse tipo de arquivo e seu nome é json. Seus principais métodos para manipulação são: load, loads, dump, dumps
   
3. A leitura pode ser feita diretamente do arquivo, utilizando o método **load** ao invés de **loads**. O loads carrega o JSON a partir de um texto e o load carrega o JSON a partir de um arquivo

    ```
    import json

    with open("pokemons.json") as file:
        pokemons = json.load(file)["results"]

    print(pokemons[0])  # imprime o primeiro pokemon da lista
    ```

- A escrita de arquivos no formato JSON é similar à escrita de arquivos comuns, porém temos que transformar os dados primeiro
   
4. Assim como a desserialização, que faz a transformação de texto em formato JSON para Python, a serialização (caminho inverso) possui um método equivalente para escrever em arquivos de forma direta
   
   ```
   import json

    # leitura de todos os pokemons
    with open("pokemons.json") as file:
        pokemons = json.load(file)["results"]

    # separamos somente os do tipo grama
    grass_type_pokemons = [
        pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
    ]

    # abre o arquivo para escrita
    with open("grass_pokemons.json", "w") as file:
        # escreve no arquivo já transformando em formato json a estrutura
        json.dump(grass_type_pokemons, file)
   ```

## Manipulando arquivos CSV

1. O formato CSV (Comma Separated Values) é muito comum em exportações de planilhas de dados e base de dados.
   
2. Ainda que seu nome indique que o delimitador seja a “,“ (vírgula), existem variações que utilizam “;“ (ponto e vírgula) ou até mesmo tabulações (“\t“).
   
3. O módulo csv, contém duas principais funções:

  - Um leitor (reader) que nos ajuda a ler o conteúdo, já fazendo as transformações dos valores para Python;

  - E um escritor (writer) para facilitar a escrita nesse formato.

    ```
    import csv

      with open("graduacao_unb.csv", encoding = "utf-8") as file:
          graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
          # Usando o conceito de desempacotamento
          header, *data = graduacao_reader

      print(data)
    ```

    - O leitor define como dialeto padrão excel, ou seja, o delimitador de campos será “,“ e o caractere de citação será aspas duplas ("). 
  
    - Uma forma de modificar estes padrões é definindo-os de forma diferente na criação do leitor. Além disso, o leitor irá usar o decodificador padrão do sistema para decodificar em unicode o arquivo .csv. 
  
    - Para utilizar um decodificador diferente, deve ser passado o argumento encoding com o valor do decodificador esperado. Um leitor de .csv pode ser percorrido utilizando o laço de repetição for e, a cada iteração, retorna uma nova linha já transformada em uma lista Python com seus respectivos valores.

4. Podemos fazer uma análise e verificar quantos cursos são ofertados por departamento:

    ```
    import csv

    with open("graduacao_unb.csv", encoding="utf8") as file:
        graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
        # Usando o conceito de desempacotamento
        header, *data = graduacao_reader

    group_by_department = {}
    for row in data:
        department = row[15]
        if department not in group_by_department:
            group_by_department[department] = 0
        group_by_department[department] += 1

    # Escreve o relatório em .csv
    # Abre um arquivo para escrita
    with open("department_report.csv", "w", encoding = "utf-8") as file:
        writer = csv.writer(file)

        # Escreve o cabeçalho
        headers = [
            "Departamento",
            "Total de Cursos",
        ]
        writer.writerow(headers)

        # Escreve as linhas de dados
        # Desempacotamento de valores
        for department, grades in group_by_department.items():
            # Agrupa o dado com o turno
            row = [
                department,
                grades,
            ]
            writer.writerow(row)
    ```

5. Existem ainda o leitor e o escritor baseados em dicionários. A principal vantagem é que não precisamos manipular os índices para acessar os dados das colunas. A desvantagem é o espaço ocupado em memória (que é maior que o comum), devido à estrutura de dados utilizada.

    ```
    import csv

    # lê os dados
    with open("graduacao_unb.csv", encoding = "utf-8") as file:
        graduacao_reader = csv.DictReader(file, delimiter=",", quotechar='"')

        # a linha de cabeçalhos é utilizada como chave do dicionário
        # agrupa cursos por departamento
        group_by_department = {}
        for row in graduacao_reader:
            department = row["unidade_responsavel"]
            if department not in group_by_department:
                group_by_department[department] = 0
            group_by_department[department] += 1

    # abre um arquivo para escrita
    with open("new_department_report.csv", "w", encoding = "utf-8") as file:
        # os valores a serem escritos devem ser dicionários
        headers = [
            "Departamento",
            "Total de Cursos",
        ]
        # É necessário passar o arquivo e o cabeçalho
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        # escreve as linhas de dados
        for department, grades in group_by_department.items():
            # Agrupa o dado com o turno
            row = {"Departamento": department, "Total de Cursos": grades}
            writer.writerow(row)
    ```

## Variáveis de Ambiente

1. O Python nos fornece acesso às variáveis de ambiente através do dicionário **os.environ**, ou seja, uma estrutura de dados do tipo chave-valor onde a chave é a nossa variável de ambiente e o valor é o que está contido. Para listar todas as nossas variáveis de ambiente:

    ```
    import os

    print(os.environ)
    ```
2. Por se tratar de um dicionário o os.environ possui todos os atributos e métodos associados a essa estrutura de dados, além de prover o mesmo mecanismo de acesso a um valor através da chave: **meu_dicionario["minha_chave"]**.
Podemos passar qualquer variável de ambiente existente e obter de volta o seu valor. Por exemplo, para saber quem é a atual pessoa usuária do seu computador: **os.environ["USER"]**

3.  O os.environ é um dicionário que contém as variáveis de ambiente já criadas em nosso sistema operacional. Os valores retornados por esse dicionário serão sempre do tipo string e por vezes podemos nos deparar com uma série de bugs. 
   
4. A variável DEBUG_MODE é um booleano (False), mas para a **os.environ** seria o equivalente a string "False": 
   
   ```
    if os.environ['DEBUG_MODE']:
        # DO SOMETHING IN DEBUG MODE
    else:
        # DO ANOTHER THING
   ```
- Uma string não vazia é um valor truthy e o conteúdo dentro do condicional if é o que seria executado. O mesmo poderia acontecer com valores do tipo inteiro e com outros tipos de dados. 

5. Outra opção para resgatar esses valores do nosso arquivo é através da biblioteca externa decouple. Sua instalação se dá via **pip install python-decouple==3.6**. Uma vez que a biblioteca está instalada e configurada, temos acesso simples e direto às nossas variáveis salvas em .env:

    ```
    from decouple import config

    API_USER = config("USER")
    API_KEY = config("KEY")
    DEBUG_MODE = config("DEBUG_MODE", default=False, cast=bool)
    ```

  - O método config lê o conteúdo de .env da mesma forma que fazíamos com os.environ. Basta passarmos para ele o nome da chave que estamos interessados em obter o valor. Além disso, temos uma série de atributos nomeados como o default que atribui um valor padrão à variável de ambiente caso o mesmo não seja encontrado e o cast que converte o tipo de dado de string para booleano, inteiro, entre outros.

## Visualizando dados em forma de tabela

1. Utilizando a biblioteca tabulate:

```
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
```

## Formatação

1. print(f"Orçamento:{orcamento:.0f}") - orçamento sem casas decimais
   
2. print(f"Orçamento:{orcamento:.2f}") - orçamento com 2 casas decimais
   
3. print(f"Orçamento:{orcamento:.2f}\n") - **\n** pula uma linha
   
4. int(input('Digite um numero:')) - **int()** converte a string em um número
   
5. float(input('Digite sua remunaração:')) - **float()** converte a string em um valor com casas decimais

## Desempacotamento

1. É a atribuição de variáveis de uma única vez
   
   ```
    x, y = "ab" #x=a e y=b
    x, y = y, x #x=b e y=a

    a, *b = 'gustavo' #a=g  b=['u','s','t','a','v','o']

     a, *b, c = 'gustavo' #a=g  b=['u','s','t','a','v']  c=o
   ```

## Módulos como scripts

1. O **-m** serve para rodar um módulo como script

- python3 -m antigravity - Abri página de boas vindas
- python3 -m venv virtual_enviroment - Cria um ambiente virtual com a pasta virtual_enviroment
- python3 -m calendar - Retorna um calendário do ano atual
- python3 -m calendar 3000 - Retorna um calendário do ano de 3000
- python3 -m pydoc -b - Mostra uma página com documentações  