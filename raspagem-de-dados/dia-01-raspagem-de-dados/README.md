# RASPAGEM DE DADOS :

1. Raspagem de dados -  é uma técnica computacional para extrair dados provenientes de um serviço ou aplicação, estruturando-os em bancos de dados, planilhas ou outros formatos. Pode ser usado para comparar preços de produtos com a concorrência; automatização de processos maçantes; recuperação de documentos em sites jurídicos; analisar perfis de redes sociais; recuperar dados públicos do governo; entre outros.
   
2. Passos aplicados nesta técnica são: realização de requisições, análise das respostas e extração dos dados, navegação do conteúdo, limpeza e armazenamento dos dados.
   
3. A comunicação com servidores HTTP e HTTPS se dá através de requisições, nas quais utilizamos o verbo para indicar que tipo de ação deve ser tomada para um dado recurso. Devemos informar na requisição em qual recurso estamos atuando e no cabeçalho passamos algumas informações que podem ser importantes, como o tipo de resposta aceita ou o tipo de conteúdo sendo enviado
   
4. O Python possui um pacote para lidar com o protocolo HTTP e HTTPs que é o **requests** . E para instalar essa lib dentro de um ambiente virtual digitamos o seguinte comando:
   
   ```
   python3 -m venv .venv && source .venv/bin/activate
   python3 -m pip install requests
   ```
5. Arquivo python para consulta:
   
   ```
   import requests


    # Requisição do tipo GET
    response = requests.get("https://www.betrybe.com/")
    print(response.status_code)  # código de status
    print(response.headers["Content-Type"])  # conteúdo no formato html

    # Conteúdo recebido da requisição
    print(response.text)

    # Bytes recebidos como resposta
    print(response.content)

    # Requisição do tipo post
    response = requests.post("http://httpbin.org/post", data="some content")
    print(response.text)

    # Requisição enviando cabeçalho (header)
    response = requests.get("http://httpbin.org/get", headers={"Accept": "application/json"})
    print(response.text)

    # Requisição a recurso binário
    response = requests.get("http://httpbin.org/image/png")
    print(response.content)

    # Recurso JSON
    response = requests.get("http://httpbin.org/get")
    # Equivalente ao json.loads(response.content)
    print(response.json())

    # Podemos também pedir que a resposta lance uma exceção caso o status não seja OK
    response = requests.get("http://httpbin.org/status/404")
    response.raise_for_status()
   ```
## Alguns problemas

1. Caso seja feito requesições demais, a página pode travar para você. Nesse caso é importante colocar um tempo entre cada requisição:
   
   ```
   import requests

   for _ in range(15): # loop de requisições
        response = requests.get("http://www.cloudflare.com/rate-limit-test/")
        print(response.status_code) 
        time.sleep(5) # tempo de 5 segundos para cada requisição
   ```
2. Ás vezes pedimos um recurso ao servidor, mas caso o nosso tráfego de rede esteja lento ou exista um problema interno do servidor, nossa resposta pode demorar ou até mesmo ficar travada indefinidamente. Podemos definir um tempo limite (timeout) para que, após este tempo, possamos tomar alguma atitude, como por exemplo, realizar uma nova tentativa. Podemos tratar essa exceção da seguinte forma:
   
   ```
    import requests

    try:
        # recurso demora muito a responder
        response = requests.get("http://httpbin.org/delay/10", timeout=2)
    except requests.Timeout:
        # vamos fazer uma nova requisição
        response = requests.get("http://httpbin.org/delay/1", timeout=5)
    finally:
        print(response.status_code)

   ```

3. Analisando respostas:

- parsel - é a biblioteca que serve para ler o contéudo vindo de uma requisição.
  
- Para instalar o parsel:
  
```
python3 -m pip install parsel
```

4. 
   
