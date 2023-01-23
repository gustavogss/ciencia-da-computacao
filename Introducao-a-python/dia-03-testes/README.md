# TESTES :

1. A biblioteca **pytest** é um framework que facilita a escrita de testes simples, mas capazes de testar funcionalidades complexas em aplicações e bibliotecas.
   
2. Instale a biblioteca **pytest** em ambiente virtual com o comando:
   
   ```
   python3 -m pip install pytest
   ```
3. Para verificar a versão do pytest dentro da máquina virtual criada:
   
   ```
   python3 -m pytest --version
   ```

4. Escrevendo o arquivo.py e o teste.py

      ```
      #codigo.py

      def is_odd(number):
         'Retorna True se um número é ímpar, senão False.'
         return number % 2 != 0
      ```
   
      ```
      #test_codigo.py

      from codigo import is_odd

      def test_is_odd_when_number_is_odd_returns_true():
      'Para um número ímpar a função deve retornar o valor True'
      assert is_odd(3) is True

      def test_is_odd_when_number_is_even_returns_false():
      'Para um número par a função deve retornar o valor False'
      assert is_odd(2) is False
      ```

      - O nome do arquivo de testes possui o prefixo test_, assim como a definição das funções de teste. Isto é necessário para que seus testes sejam descobertos pela ferramenta.
  
      - O comando **assert** - caso a expressão recebida seja verdadeira (avaliada como True), nada acontece. Porém, caso seja falsa (avaliada como False), uma exceção do tipo AssertionError é lançada. A pytest captura este erro e tenta apresentar uma comparação entre o esperado e o recebido da melhor maneira possível.
 
5. Para rodar os testes e conferir o resultado usamos o comando:
   
   ```
   python3 -m pytest
   ```
6. O Python utiliza exceções para sinalizar que ocorreram erros durante a execução de um código e que nem sempre são fatais. Podemos escrever testes que verificam que um erro deve ocorrer a partir de uma determinada entrada.
   
   ```
   # codigo.py

   def divide(a_number, other_number):
    "Retorna a divisão de a_number por other_number"
    return a_number / other_number
   ```
   ```
   #test_codigo.py

   import pytest
   from codigo import is_odd, divide

   def test_divide_when_other_number_is_zero_raises_an_exception():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
   divide(2, 0)
   ```
   - Utilizamos a função raises da pytest para verificar se a exceção ocorreu. Caso contrário, ela lança um AssertionError, indicando que o teste não passou. Podemos verificar também se o texto retornado na exceção é o esperado através do parâmetro match, que pode receber uma expressão regular. 
  
7. Test fixture (fixture) são as precondições ou estados necessários para a execução de um teste. Cada teste pode ter seu próprio cenário (contexto) ou compartilhá-lo com outros testes.

      ```
      # get_most_ordered_dish_per_costumer é uma função que retorna o prato mais pedido por uma
      # determinada pessoa cliente, considerando que os pedidos estão em uma lista.

      # get_order_frequency_per_costumer é uma função que retorna a frequência que uma determinada
      # pessoa cliente pede um determinado prato, considerando que os pedidos estão em uma lista.

      # uma fixture utilizando a biblioteca pytest
      # é definida utilizando a sintaxe abaixo

      @pytest.fixture
      def orders():
         """Nosso cenário (contexto) temos os seguintes pedidos"""
         return [
            {"customer": "maria", "order": "pizza", "day": "terça-feira"},
            {"customer": "joao", "order": "hamburger", "day": "terça-feira"},
            {"customer": "maria", "order": "pizza", "day": "quarta-feira"},
            {"customer": "maria", "order": "hamburger", "day": "quinta-feira"},
         ]

      # estamos adicionando a fixture "orders" ao teste
      # ou seja, temos um contexto onde os pedidos são os definidos anteriormente
      def test_get_most_ordered_dish_per_costumer_when_customer_is_maria(orders):
         assert get_most_ordered_dish_per_costumer(orders, "maria") == "pizza"

      # novamente adicionamos um cenário (contexto) ao teste onde os pedidos realizados são os
      # definidos na fixture
      def test_get_order_frequency_per_costumer_when_customer_is_joao_and_order_is_pizza(orders):
         assert get_order_frequency_per_costumer(orders, "joao", "pizza") == 0

      def test_get_order_frequency_per_costumer_when_customer_is_maria_and_order_is_hamburger(orders):
         assert get_order_frequency_per_costumer(orders, "maria", "hamburger") == 1
      ```

      - O @ é o decorator do Python. Com ele podemos adicionar funcionalidades aos nossos códigos, “decorando” o que uma outra função faz (no caso acima, a função pytest.fixure).
  
8. Em testes automatizados (de unidade) é desejado que cada teste não interfira no estado manipulado por outro teste, e também que recursos externos (arquivos, internet, banco de dados) não atrapalhem a sua execução. Por isso, é muito comum a utilização dos dublês para simular estes recursos externos.
   
9. Podemos substituir componentes para que retornem um determinado valor simulado ou podemos substituir os componentes por objetos falsos que registram as informações sobre sua invocação, como o número de vezes em que foram chamados ou os parâmetros com o qual foram chamados.
    
10. As técnicas de dublês podem ser: fakes, mocks, stubs e spies.

- Fakes: Objetos que possuem implementações funcionais, porém normalmente simplificadas; 
  
- Mocks: São pré programados para verificar as chamadas das funções que receberem; 
  
- Stubs: Fornecem respostas predefinidas;
  
- Spies: São como stubs, mas também armazenam informações de como foram chamados.

11. 
