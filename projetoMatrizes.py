# Importando bibliotecas
from colorama import init, Fore     # Biblioteca colorama, usada para dar cor ao terminal.
import os                           # Biblioteca OS, usada para limpar o terminal (ver a linha 7)
from time import sleep              # Biblioteca time, para dar pausas entre as telas
init()                              # Inicializando o colorama

# Inicializando variáveis importantes
os.system('cls')                    # Esse comando limpa o terminal
acertos = 0                         # Número inicial de acertos
pontuacao = 0                       # Pontuação
sequencia = 0                       # Sequência de acertos, usada para dar pontuação extra
vidas = 4                           # Número de questões que podem ser erradas
podio = []                          # Matriz do pódio
questoesFacil = [                   # Questões fáceis
    ["IFRN 2024) De acordo com o Texto 1, a Cúpula da Amazônia receberá os presidentes dos seguintes países: Brasil, Bolívia, Colômbia, Equador, Guiana, Peru, Suriname e Venezuela. Após a abertura do evento, foi realizado um sorteio, retirando um nome dentre esses países. A probabilidade do nome retirado, aleatoriamente, ser de um país cujo nome se inicia com a letra B foi de",
     '1/4', '2/3', '1/3', 'a'],
    
    ["Quais dos termos a seguir representa um número irracional?",
     '3,14', '2,55...', '1/2', 'b'],
    
    ["Dado a expressão b × cc = bb qual é o valor de cc?",
     '23', '22', '11', 'c'],
    
    ["Durante o almoço, Ciro tinha em seu prato 3 tipos de grãos diferentes separados, feijão, milho e ervilha. Ciro tapa o seu olho e escolha uma das 3 opções para preencher o seu garfo. qual a probabilidade de Ciro escolher milho?",
     '3/3', '1/3', '1/2', 'b'],
    
    ["Dado os conjuntos A = {1,2 e 3} e B ={-1,-2 e -3} assinale a alternativa que representa a união de A com B.",
     '{-1,-2,-3,1,2 e 3}', '{0}', '{0, 0 e 0}', 'a'],
    
    ["Qual será o resultado da expressão (1/2 + 3/4) em sua forma simplificada?", 
     '10/8', '5/4', '4/6', 'b'],

    ["Para realizar um trabalho de matemática, a sala do 2º Info. Mat. teve que criar figuras geométricas usando palitos. A primeira figura criada foram usados 3 palitos, a segunda 6 e a terceira 9 palitos. Seguindo nessa ordem, quantos palitos terá a 7ª figura criada pela sala?", 
     '27', '21', '18', 'a'],
    
    ["Numa turma do IFRN campus Pau dos Ferros existem 15 meninas e 21 meninos. Qual a proporção de meninos/meninas nesta turma?", 
     '2/1', '15/7', '7/5', 'b'],

    ["Na expressão: log(3x+7), qual a base do logaritmo?", 
     '10', 'não existe', '3x+7', 'a'],
    
    ["Dado uma matriz quadrada A3x4, qual é a sua ordem?", 
     '4 linhas e 3 colunas', '3 linhas e 4 colunas', '1 linha e 7 colunas', 'b'],
]
questoesMedio = [                   # Questões médias
    ["Dado um triângulo aleatório cujos 2 dos seus ângulos têm valores de 60 e 25 graus, qual será o valor do terceiro ângulo?",
     '5', '15', '90', 'a'],
    
    ["George, um atleta de vôlei, notou que o saque de seu adversário levava a bola a uma altura de 3 metros e que no momento ele estava a uma distância de 4 metros da sombra da bola. Qual a distância entre George e a bola?",
     '25 metros', '5 metros', '16 metros', 'b'],
    
    ["Durante um ano, um músico nordestino produz cerca de 21 músicas. Quantas músicas ele irá produzir durante 5 anos se mantiver esse ritmo?",
     '63 músicas', '105 músicas', '95 músicas', 'b'],
    
    ["Qual das seguintes formas mostra a representação certa de uma raiz quadrada em um quadrado perfeito?",
     '5^1/2', '16^1/4', '81^1/2', 'c'],
    
    ["Marcelo tem 3 números naturais distintos. Supondo que dois destes números sejam números primos ≠ 2 e o outro seja um número par, após a soma de todos qual será o resultado obtido por Marcelo?",
     'par', 'ímpar', 'outro número primo', 'a'],
    
    ["Roberta iria a um passeio de barco com sua família, ela seria a última a entrar em um dos barcos. Ela notou que sua família foi distribuída em 3 barcos da seguinte forma: 1º barco: irmão e primo; 2º barco: pais, tios e avós; 3º barco: resto dos primos. Qual a probabilidade de Roberta entrar em um barco que tenha alguém que vive na mesma casa que ela?",
     '3/2', '1/3', '2/3', 'c'],
    
    ["Qual das seguintes expressões mostra um polinômio de grau 5?",
     '5x^5+7x^2', '7x^3+4b^2', '5x^5', 'a'],
    
    ["Uma figura de borracha tinha uma área de 30cm², porém, após esquentá-la, essa figura ficou mole e expandiu sua área para 105cm². Quantas vezes sua área inicial foi expandida após esquentar?",
     '3,5x o seu valor', '3x o seu valor', '4x o seu valor', 'a'],
    
    ["Em um determinado esporte, ganha o time que fizer 3 sets antes de seu adversário. Supondo que cada set chegue até 15 pontos e que, quando empatado, ganha o time que fizer 2 pontos de diferença primeiro, e que se os times ficarem empatados no último set, ganha aquele que fizer 7 pontos primeiro, qual o máximo de pontos possíveis em uma partida? Obs: nenhum dos sets pode passar dos 18 pontos.",
     '33 pontos', '45 pontos', '165 pontos', 'c'],
    
    ["Após expandir a expressão (a+b)², qual será a expressão que surgirá como resultado?",
     'a² + b²', '2a + 2b', '2a + 2ab + 2b', 'c']
]
questoesDificil = [                 # Questões difíceis
    ["Em um posto de saúde, havia 6 pessoas na sala de espera. A primeira pessoa foi atendida em 20 minutos; o atendimento da segunda durou 16 minutos; a terceira e a quarta demoraram 13 minutos dentro do consultório cada; o atendimento da quinta foi de 10 minutos; e o da sexta pessoa durou apenas 6 minutos. O tempo médio de atendimento por paciente foi de quantos minutos?",
     '13', '14', '15', 'a'],
    
    ["Mauro irá comprar um celular novo. As condições de pagamento são as seguintes: 20% de entrada, mais 5 prestações de R$ 340,00. Se o pagamento for à vista, há um desconto de 10% sobre o valor a prazo. Mauro optou por pagar à vista. Portanto, ele desembolsou:",
     'R$ 1.912,50', 'R$ 1.970,50', 'R$ 2.040,00', 'a'],
    
    ["João está planejando construir um jardim retangular em seu quintal usando blocos de pavimentação. Ele tem um lote de blocos de pavimentação quadrados, cada um com 22 cm de lado. Para saber quantos blocos de pavimentação precisa comprar, ele terá que calcular o perímetro do jardim. Logo, calcule o perímetro do bloco",
     'P = 80cm', 'P = 88 cm', 'P = 11 cm', 'b'],
    
    ["Quantos são os anagramas da palavra PAPAGAIO?",
     '6720', '3360', '840', 'b'],
    
    ["No nascimento de três filhos de um casal, qual a probabilidade de que todos sejam do mesmo sexo?",
     '2%', '10%', '25%', 'c'],
    
    ["Dois rolos de fita de sinalização zebrada, um com 180 m, e outro com 300 m de comprimento de fita, serão divididos em partes, todas com o mesmo comprimento, o maior possível, sem desperdício, para um curso de formação dos novos agentes de trânsito contratados em determinado município. O número de partes que será obtido do rolo com o maior comprimento de fita será igual a:",
     '8', '6', '5', 'c'],
    
    ["Uma pesquisa realizada entre todos os estudantes de uma escola constatou que 50% deles gostam de matemática, 40% gostam de ciências e 20% gostam de ambas as disciplinas. Escolhendo-se um estudante desta escola ao acaso, a probabilidade de que ele goste de pelo menos uma das disciplinas é:", 
     'Maior que 79%', 'Maior que 69% e menor que 79%', 'Maior que 59% e menor que 69%', 'b'],
    
    ["Uma caixa contém 50 cartões numerados de 1 a 50. Sorteando-se um cartão ao acaso, a probabilidade de o número no cartão ser um múltiplo de 5 é:",
     'Maior que 24%', 'Maior que 21% e menor que 24%', 'Maior que 18% e menor que 21%', 'c'],
    
    ["Vinte pessoas resolveram alugar um barco por R$ 200,00, quantia que seria dividida igualmente entre todos. No dia do passeio algumas pessoas desistiram. Por causa disso, cada participante do passeio teve que pagar R$ 15,00 a mais. Quantas pessoas desistiram do passeio?",
     '10', '11', '12', 'c'],
    
    ["Regina, Paulo e Iracema tentam adivinhar quantas bolas estão dentro de uma caixa fechada. Eles já sabem que este número é maior que 100 e menor que 140. Eles fazem as seguintes afirmações: • Regina: Na caixa há mais de 100 bolas e menos de 120 bolas. • Paulo: Na caixa há mais de 105 bolas e menos de 130 bolas. • Iracema: Na caixa há mais de 120 bolas e menos de 140 bolas. Sabe-se que apenas uma dessas afirmações é correta. Quantos são os possíveis valores para o número de bolas dentro da caixa?",
     '1', '5', '16', 'c']
]
questoes = [questoesFacil,questoesMedio,questoesDificil]

while True:                                                     # Iniciando o loop do jogo
    # Tela inicial
    print(Fore.GREEN + "====================================================")
    print(Fore.RED + "-= Seja bem vindo ao questionário de matemática! =-" + Fore.RESET)
    print(Fore.GREEN + "====================================================")

    # Recebendo o nome do jogador e a dificuldade
    nome = input("Insira seu nome\n-> ")
    dificuldade = int(input(f"Olá {nome}. Insira o nível de dificuldade, (1, 2 ou 3)\n-> "))

    # Fluxo principal do jogo
    for questao in questoes[dificuldade-1]:
        if vidas >= 1: 
            # Mostrando a pergunta e as alternativas
            indexQuestao = questoes[dificuldade-1].index(questao)    # Índice da questão atual
            os.system('cls')                                         # Limpa a tela
            print(Fore.MAGENTA + f"QUESTÃO {indexQuestao + 1} =================")
            print(questao[0])                                        # Enunciado da questão
            print(f"a) {questao[1]}")                                # Alternativas a, b e c
            print(f"b) {questao[2]}")
            print(f"c) {questao[3]}")

            # Recebendo a resposta
            resposta = input("\nInsira a alternativa: ")            # Recebendo a resposta

            # Resultado: resposta correta
            if resposta.lower() == questao[4]:                      
                resultado = f"Parabéns! A resposta certa era {questao[4]})!"
                cor = Fore.GREEN                                    # Variável da cor da mensagem de resultado
                pontuacao += 50 * dificuldade + 100 * sequencia     # Soma na pontuação
                sequencia += 0.10                                   # Soma na sequência
                acertos += 1                                        # Soma na quantidade de acertos

            # Resultado: Resposta errada
            else:
                resultado = f"Que pena, a resposta era {questao[4]})!"
                cor = Fore.RED                                      # Variável da cor da mensagem de resultado
                sequencia = 0                                       # Reseta a sequência de acertos
                vidas -= 1                                          # Subtrai uma vida

            # Mostrando a mensagem de resultado
            print(cor + "=================================================")
            print(cor + resultado)                                  # Printa o resultado na respectiva cor
            print(f"Pontos: {pontuacao}")                           # Printa os pontos
            print(f"Vidas: {vidas}")                                # Printa as vidas
            print(cor + "=================================================")
            sleep(3)
        else:
            break

    # Terminando o quiz
    os.system('cls')
    print(Fore.GREEN + "====================================================")
    print(Fore.RED +   "                -= Jogo terminado =-                " + Fore.RESET)             # Criando um resumo da partida
    print(Fore.GREEN + "====================================================")
    print(f"Nome do jogador: {nome}")                                                                   # Nome do jogador
    print(f"Dificuldade: {dificuldade}")                                                                # Dificudade jogada
    print(f"Acertos: {acertos}")                                                                        # Acertos
    print(f"Vidas: {vidas}")                                                                            # Vidas
    print(f"Sequência de acertos: {sequencia * 10}")                                                    # Streak de pontos quando o jogo terminar
    print(f"Pontuação: {pontuacao} + {100 * vidas} (Pontos das vidas) => {pontuacao + 100 * vidas}")    # Pontuação
    print(f"Erros/Não respondidas: {10-acertos}")                                                       # Questões erradas
    pontuacao = pontuacao + 100 * vidas                                                                 # Soma uma quantidade de pontos extras pelas vidas restantes
    jogador = [{nome}, {pontuacao}]
    podio.append(jogador)
    respota = input()

    # Mostrando o pódio
    os.system('cls')
    print(Fore.GREEN + "====================================================")
    print(Fore.RED +   "                -= Pódio de jogos =-                " + Fore.RESET)             # Mostra o pódio
    print(Fore.GREEN + "====================================================")
    for i in podio:
        print(f"{i[0]} -> {i[1]} pontos.")
    resposta = input()
    os.system('cls')
