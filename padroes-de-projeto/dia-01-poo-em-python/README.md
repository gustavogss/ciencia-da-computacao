# POO EM PYTHON :

1. Programação Orientada a Objetos (POO) - é um paradigma de programação, ou seja, uma estrutura de organização. Com a POO podemos aproveitar bastante código, isolar partes do sistema, escalar aplicações, facilidade em criar sistemas complexos.
   
2. Objeto é uma instância da classe.
   
3. Atributos são as variáveis. A valoração dos atributos é feita no objeto criado a partir da classe e não na classe.
   
4. Resumindo: A classe define atributos e objetos os valoram.
   
5. A classe define os atributos e métodos(comportamento) dos objetos.
   
6. Os métodos são ações que um objeto ou classe podem realizar, ou seja, funções.
   
7. Uma classe costuma definir os métodos e os objetos os chamam (mas em alguns casos os métodos podem ser chamados a partir da classe).
   
8. Os métodos podem manipular os atributos.
   
9.  Depois da classe modelada com todos os seus atributos, criaremos o construtor da classe. O construtor é um método especial que roda automaticamente quando a gente cria (instancia) o objeto. 
    
10. Em python o construtor é implementado de duas formas para cada nova classe criada, mas você pode implementá-los novamente, ou seja, sobrescrevê-los:
    - __new__ (construtor)
    - __init__ (inicializador)
  
11. Apesar do método __init__ ser “apenas” o inicializador, é comum ver referências a ele como o construtor. Isso acontece pois são raras as vezes que precisamos alterar o __new__ para customizar nossas classes:

```
class Liquidificador:
    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.cor = cor
        self._potencia = potencia
        self._tensao = tensao
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__corrente_atual_no_motor = 0
```
  - self: representa a instância do objeto, ou seja, tem acesso ao objeto na memória. Em outras linguagens é conhecido pelo this.
  
  - Com o método __init__ inicializamos os atributos do objeto apenas atribuindo um valor a cada nova chave.
   
  - Para criar nossos primeiros objetos:

```
meu_liquidificador = Liquidificador("Azul", 200, 127, 200)
seu_liquidificador = Liquidificador(cor="Vermelho", potencia=250, tensao=220, preco=100
)
```

12. O encapsulamento é um dos pilares da orientação a objetos. Por meio dele, é possível simplificar bastante a implementação da abstração. Sendo assim nossos atributos e métodos são segmentados 3 categorias:
    
    - Públicos: podem ser acessados livremente por qualquer parte da aplicação
    - Protegidos: podem ser acessados apenas pela classe que os definem e, quando há herança envolvida, também pelas classes “abaixo” na hierarquia
    - Privados: podem ser acessados apenas pela classe que os definem
  
13. Em Python não temos palavras reservadas como public, private e protected para declarar um atributo ou método como público, privado ou protegido. Existe uma convenção de nomenclatura para definir a acessibilidade de cada recurso:
      
    - Nomes iniciados com _ são considerados protegidos: **_tensao**
    - Nomes inciados com __ são considerados privados: **__ligado**
    - Os demais nomes são considerados públicos
  
14. Como podemos proteger o atributo ligado, de forma que fique simples e seguro alterá-lo?  **com os métodos**.
    - Podemos criar os métodos ligar e desligar e daremos poderes para que eles consigam manipular os atributos

```
class Liquidificador:
    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.cor = cor
        self._potencia = potencia
        self._tensao = tensao
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__corrente_atual_no_motor = 0

    def ligar(self, velocidade):
        if velocidade > self.__velocidade_maxima or velocidade < 0:
            raise ValueError(
                f"Velocidade deve estar entre 0 e {self.__velocidade_maxima}"
            )

        self.__velocidade = velocidade
        self.__corrente_atual_no_motor = (
            (self._potencia / self._tensao) / self.__velocidade_maxima
        ) * velocidade
        self.__ligado = True

    def desligar(self):
        self.__ligado = False
        self.__velocidade = 0

    def esta_ligado(self):
        return self.__ligado
```

15. No python por padrão os atributos e métodos são públicos.
    
16. A abstração de dados oculta os detalhes da implementação e mostra apenas a funcionalidade para quem acessa os métodos, a fim de reduzir a complexidade do código.
    
17. Getters e Setters: são métodos que serverm para acessar e alterar atributos privados de forma indireta. Setter - altera um valor, enquanto o método Getter recupera um valor:

```
class Liquidificador:
    def get_cor(self):
        return self.__cor.upper()

    def set_cor(self, nova_cor):
        if nova_cor.lower() == "turquesa":
            raise ValueError("Não existe liquidificador turquesa")

        self.__cor = nova_cor

    def __init__(self, cor, potencia, tensao, preco):
        # Observe que usamos o setter para já validarmos o primeiro valor
        self.set_cor(cor)

        # Demais variáveis omitidas para este exemplo


liquidificador = Liquidificador("Azul", "110", "127", "200")

# print(f"A cor atual é {liquidificador.__cor}")
# AttributeError: 'Liquidificador' object has no attribute '__cor'

print(f"A cor atual é {liquidificador.get_cor()}")
# A cor atual é AZUL
liquidificador.set_cor("Preto")
print(f"Após pintarmos, a nova cor é {liquidificador.get_cor()}")
# Após pintarmos, a nova cor é PRETO

```

18. O acesso ao atributo privado liquidificador.__cor gera um erro, mas chamar o método get_cor() funciona perfeitamente. O comportamento é similar para o acesso: liquidificador.__cor = "alguma cor" gera um erro, mas liquidificador.set_cor("alguma cor") não (desde que a cor não seja turquesa).
    
19. 