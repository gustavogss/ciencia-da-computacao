# PADRÕES - DECORATOR, OBSERVER E FACTORY :

1. Code smells -  são indícios de futuros problema.
   
2. Padrões de Projeto e templates de solução - são templates de código que nos ajudam diretamente na solução de nossos problemas sem a necessidade de reinventarmos a roda, pois escolhendo o padrão adequado teremos certeza que nosso código vai evoluir para uma arquitetura conhecida e testada por milhares de outras pessoas programadoras.
   
3. O Padrão Factory - é possível criar os cenários de teste 
   
4. **Padrão Decorator**: é um padrão de projeto estrutural que permite adicionar novos comportamentos e responsabilidades aos objetos de forma flexível. Para usa-lo usamos o @ antes dos métodos no Python.

```
class CalculadoraDecorada:
    def __init__(self, calculadora):
        self.calculadora = calculadora

    def converterNumero(self, numero):
        if not isinstance(numero, str):
            return numero

        # Neste cenário, em vez de fazermos IF e else... podemos usar o dicionário
        # conseguimos acessar obter o valor a partir da chave
        return {
            "um": 1, "dois": 2, "três": 3, "quatro": 4, "cinco": 5,
            "seis": 6, "sete": 7, "oito": 8, "nove": 9, "dez": 10,
        }.get(numero)

    def soma(self, x, y):
        return self.calculadora.soma(
            self.converterNumero(x), self.converterNumero(y)
        )

```
- Para ustilizar essa calculadora:

```
if __name__ == "__main__":
    calculadora = Calculadora()
    print("10 + 20 =")
    calculadora.soma(10, 20)

    calculadoraDecorada = CalculadoraDecorada(calculadora)
    print("'oito' + 'dois' =", calculadoraDecorada.soma("oito", "dois"))

```
5. **Padrão Observer** - é um padrão comportamental, pois o foco é as responsabilidades dos objetos. Uma classe observadora se responsabiliza por monitorar outro objeto. Assim, quando ocorrer alguma alteração ou eventos no objeto monitorado, o observador vai notificar os demais objetos do sistema. O React Redux pode ser considerado uma implementação do padrão Observer.

- Criando a classe Perfil, ao adicionar um novo post (adicionar_post()), exibirá o mesmo (mostrar_post) e notificará todas as pessoas seguidoras ( notificar_todos) pelos sistemas (__sistemas de notificação) que possui. O método adicionar_sistema_de_notificacao() permitirá que o cadastro de novos sistemas seja feito de forma dinâmica:

```
class Perfil:
    def __init__(self):
        self.__sistemas_de_notificacao = []
        self.__new_post = None

    def adicionar_sistema_de_notificacao(self, sistema):
        self.__sistemas_de_notificacao.append(sistema)

    def notificar_todos(self):
        for sistema in self.__sistemas_de_notificacao:
            sistema.notificar()

    def adicionar_post(self, post):
        self.__new_post = post
        self.mostrar_post()
        self.notificar_todos()

    def mostrar_post(self):
        print(f"\nPost: {self.__new_post}\n")
```
   
6. 

