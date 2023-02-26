# ARQUITETURA DE COMPUTADORES :

## Modelo de Von Neumann:

1. Define um computador como uma máquina que possui dois elementos principais: **uma memória principal (como a memória RAM)**, onde podemos registrar e ler instruções e dados, e um **processador (CPU)**, responsável por buscar tais informações, realizar os cálculos e armazenar os resultados novamente na memória.
   
## Lógica binária:

1. Os computadores processam informações baseado no sistema binário formado por **0** e **1**. Esses bits é a menor unidade de um sistema digital.
   
2. Byte equivale a 8 bits e é capaz de armazenar um valor decimal entre 0 e 255 (0000 0000 e 1111 1111).
   
3. A presença de tensão ou corrente elétrica pode ser considerada como verdadeiro, 1, e a ausência como falso, 0;
   
4. Os dispositivos que podem se comportar como chaves eletrônicas são os transistores, onde a tensão ou corrente na entrada resulta na presença ou ausência de uma tensão ou corrente na saída
   
5. Transistores podem ser agrupados de maneira a formarem as portas lógicas NOT, AND, OR, XOR. Estas portas lógicas apresentam, para uma mesma combinação de valores de entrada (conjunto de 0s e 1s), a mesma saída. As portas lógicas seguem a mesma ideia das condicionais utilizadas nas linguagens de programação.
   
## Memória Principal - RAM:

1. A memória é um dispositivo ou sistema que é usado para armazenar informações para uso imediato em um computador ou hardware de computador, ou, ainda, dispositivos eletrônicos digitais.
   
2. Cada célula da memória principal é capaz de armazenar uma informação (ou um fragmento de uma) e, para localizá-las, são utilizados seus endereços, os chamados ADDRESSES ou ADDR.
   
3. A capacidade total da memória é dada pela quantidade de suas células multiplicada pela capacidade de armazenamento de cada uma. Por exemplo, uma memória com 1024 células de 8 bits (1 byte) tem a capacidade de armazenar 1024 bytes (8192 bits), ou 1KB.
   
## Processador - CPU:

1. A CPU, ou unidade central de processamento, funciona em conjunto com a memória principal, lendo e executando as instruções e dados armazenados nela e gravando o resultado de tais processamentos.
   
2. ULA (unidade lógico-aritmética) - é o componente responsável por realizar operações lógicas (como as realizadas pelas portas lógicas AND, OR, entre outras operações lógicas) e aritméticas (como somas, subtrações, multiplicações).
   
3. A Unidade de Controle é responsável por extrair dados da memória, decodificá-los e executá-los, consultando a ULA quando necessário.
   
4. Registradores - são células internas de memória que possui o processador. Armezenam os dados lidos na memória que está sendo usado no processamento. 

5. Tudo no computador é tratado como dados e instruções, sempre utilizando números através da representação binária.

## Operações por segundo:

1. Para gerenciar todas as atividades e a comunicação entre os componentes do computador, existe um componente eletrônico que gera um sinal de “clock”. Esse sinal é uma alternância entre tensões altas e baixas a cada fração de tempo, seguindo a mesma ideia de representação de 0 e 1.
   
2. A frequência do clock é medida em hertz (Hz), ciclos por segundo. Ou seja, o número de operações básicas capazes de serem executadas em 1 segundo. O período de um clock é o tempo entre uma operação e outra
   
## Barramentos:

1. O processador está constantemente buscando por instruções na memória e dados a serem processados e devolvendo os resultados desses processamentos para a memória. E isso é feito por duas operações básicas: load e store.
   
2. A load - é a leitura da memória para carregar quais são as instruções a serem executadas, os dados são lidos e gravados em registradores do processador. 
   
3. A store - é o processo quando o processador precisa armazenar dados na memória como os resultados dos processamentos e das operações que ele realizou durante uma operação. 
   
4. Essas comunicações dos componentes são realizadas a partir de “vias” que ligam os dois componentes, os barramentos, que são conjuntos de fios. Esses componentes utilizam números binários representados por grandezas elétricas (tensão/corrente). Dessa forma, os barramentos conseguem comunicá-los transmitindo essas grandezas.
   
5. Basicamente a memória principal é ligada a CPU por 3 dessas vias:

- Endereço (ADDR): Indica o endereço da célula de memória para aquela operação;

- Dados (DATA): Transfere a informação da memória para a CPU e vice-versa.

- Controle (CTRL): Indica a “direção” dos dados para a operação, ou seja, se os dados serão transferidos da CPU para a memória (escrita) ou da memória para a CPU (leitura).

## Tipos de Memória:

1. Temos 02 tipos de memória: Memórias primárias e Memórias secundárias:

- Memórias primárias são onde os dados e programas em execução são armazenados de maneira temporária para serem processadas pela CPU. São memórias de acesso rápido, com armazenamento de um menor volume de dados, que em geral, não conseguem guardar a informação quando são desligados.

- Memórias secundárias são onde os dados (arquivos) são armazenados. Possuem um acesso mais lento, mas são capazes de armazenar permanentemente grandes volumes de dados.

2. A CPU antes de processar uma instrução, busca as informações da memória principal para seus registradores internos, que usará para realizar as operações. Porém, esse espaço dos registradores internos é bem pequeno, sendo capaz de armazenar apenas o dado para aquela operação que está sendo executada no momento (alguns bytes). Por isso, a CPU precisa constantemente trocar dados de seus registradores com a memória RAM. 
   
3. A CPU acessa um dado em seus registradores quase que instantaneamente, em apenas um ciclo. Já para buscar um dado da memória esse tempo é um pouco maior: em computadores modernos, essa operação pode levar algumas centenas de ciclos, o que equivale a 1 microssegundo, o que parece bem rápido, porém, para a quantidade de leituras que são feitas para as execuções esse tempo se torna “uma eternidade”!
   
4. Hierarquia de memórias - os dados que são acessados com mais frequência ficam armazenados em memórias de acesso mais rápido. Enquanto que os dados acessados com menos frequência são armazenados em memórias mais baratas e lentas como, por exemplo, nossos arquivos no HD.
   
5. Registradores - são utilizados para armazenar um volume pequeno de dados, possuindo altíssima velocidade, e alto custo. São as memórias mais rápidas.

6. Memória Cache (L1, L2 e L3) - são componentes de acesso mais rápido do que a memória principal (sendo o L1 o mais rápido, em seguida o L2 e depois o L3) e são integrados à CPU. As memórias cache são utilizadas para armazenar alguns dados de maneira estratégica, como os dados que são lidos com maior frequência na RAM. Dessa forma, ao terem os dados encontrados nesses dispositivos, não é necessário buscá-los na memória principal, aumentando a performance do computador, tendo em vista que as chamadas a eles são centenas de vezes mais rápidas do que para a RAM.

7. Memória principal (RAM e ROM) - são memórias utilizadas para guardar configurações mais básicas do sistema como, por exemplo, os dados para inicializar alguns componentes do computador. A ROM (Read-Only Memory), é uma memória somente de leitura, um tipo de memória que não permite a escrita de dados, porém seus dados não são perdidos quando ela é desligada.   
   
8. Memória secundária ou de massa (HDs, SSDs, CD/DVDs, pendrives ) - são memórias mais lentas por fazerem a gravação física das informações nos dispositivos, porém não perdem informações quando desligadas e são capazes de armazenar grande volume de dados.
   
9.  As memórias tem dois tradeoffs a se considerar:

- Velocidade versus volatilidade: memórias de escrita e leitura mais rápidas tendem a ser voláteis, ou seja, quando o computador é desligado os dados da memória são apagados! Nos HDs (não voláteis) isso não acontece. Na memória RAM (volátil) sim.

- Velocidade versus capacidade: memórias mais rápidas costumam ser mais caras, e por isso costumam ser comercializadas com capacidades menores. Um pente de 8GB de RAM custa aproximadamente o mesmo que um SSD de 240GB ou que um HD de 1TB.

## Sistema Operacional (SO):

1. Os sistemas operacionais abstraem os complexos processos de interação com o hardware.  Realizam a gerência do hardware e sua interação com os softwares, controlando os processos, arquivos, memória, rede e os dispositivos conectados ao computador.

2. Trabalha como um intermediário, fazendo com que software e hardware interajam corretamente, garantindo que todas as partes trabalhem juntas como um “time” e agindo como um líder responsável por manter a harmonia entre sistemas de memória, arquivos, processos, dispositivos.
   
3. A memória é gerenciada pelo SO que realiza a alocação, ou seja, a troca de dados com o processador, a memória principal e a memória secundária, buscando por espaços vazios na memória e os preenchendo com dados para o funcionamento de programas e comandos.
   
4. O SO também decide como será realizada a distribuição dos diversos processos para serem executados pelo “cérebro” do computador, a CPU. A partir daí, ele acompanha os estados da execução desses processos realizando os devidos tratamentos, como voltar ou remover o processo da fila de processamentos.
   
5. Para exibir no terminal todos os processos que estão sendo gerenciados nesse momento pelo seu SO, basta digitarmos o comando:

    ```
    ps auxww
    ```
    - O comando ps funciona como se fosse uma fotografia dos processos no momento que você o executa

6. Para mostrar os processos em tempo real, basta digitar o comando no seu terminal:

    ```
    top
    ```

- O cabeçalho do comando já exibe os totais por status dos processos em sua máquina. Em seguida temos algumas médias do uso dos recursos e depois temos a listagem dos processos.

7. Para ver como os recursos da sua máquina estão sendo explorados e como a quantidade de processos constantemente muda de estado, utilizamos o comando:

```
htop
```
8. Arquivos - O SO também controla os arquivos do computador, sejam eles arquivos de dados, de programas ou aplicativos instalados. Através da interface do SO, conseguimos navegar entre diretórios armazenados nos diversos dispositivos de memória secundária do nosso computador, seja o HD, um pendrive ou nosso celular que esteja conectado em nossa máquina, sendo possível abrir, criar, deletar, copiar e editar arquivos.

- É responsável também por gerenciar o sistema de permissões desses arquivos, controlando os diversos tipos de acesso, por exemplo, impedindo que um usuário comum execute um comando que precisa de permissão de super usuário.

9. Scheduling (agendador de tarefas ou escalonamento de processos) - é uma atividade organizacional feita pelo escalonador (scheduler) da CPU ou de um sistema distribuído, possibilitando executar os processos mais viáveis e concorrentes, priorizando determinados tipos de processos, como os de I/O Bound e os CPU Bound. 

- É um processo que deve ser executado quando ocorre uma mudança de contexto (troca de processo), ao passo que ele escolhe o processo que será executado pela CPU, sendo o escalonamento realizado com o auxílio do hardware. 





