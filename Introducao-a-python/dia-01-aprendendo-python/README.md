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