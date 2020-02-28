from scipy.stats import binom

# Jogar uma moeda 5 vezes, qual a probabilidade de dar cara 3 vezes?
prob = binom.pmf(3, 5, 0.5)

# Passar por 4 sinais de 4 tempos, qual a probabilidade de pegar sinal verde
# nenhuma, 1, 2, 3 ou 4 vezes seguidas?
binom.pmf(0, 4, 0.25)
binom.pmf(1, 4, 0.25)
binom.pmf(2, 4, 0.25)
binom.pmf(3, 4, 0.25)
binom.pmf(4, 4, 0.25)

# E se forem sinais de dois tempos?
binom.pmf(4, 4, 0.5)

# Probabilidade acumulativa
binom.cdf(4, 4, 0.25)

# Concurso com 12 questões, qual a probabilidade de acertar 7 questões considerando
# que cada questão tem 4 alternativas?
binom.pmf(7, 12, 0.25) * 100

binom.pmf(12, 12, 0.25) * 100




#Temos interesse que, em 4 nascimentos, 2 sejam homens e 2 sejam mulheres. Como chamamos de sucesso nascer
#homem, temos interesse no nascimento de 2 homens ou, em linguagem matemática, X=2. Logo, o valor de k é 2
#(basta comparar a fórmula X=k com o que acabamos de escrever X=2).

#          X  n    p
#binom.pmf(0, 4, 0.25)

binom.pmf(2, 4, 0.5)

#Uma urna tem 4 bolas vermelhas (V) e 6 brancas (B). Uma bola é extraída, observada sua cor e reposta na urna. O
#experimento é repetido 5 vezes. Qual a probabilidade de observarmos exatamente 3 vezes bola vermelha?
#Inicialmente, vamos definir a variável aleatória de interesse:

#X: número de bolas vermelhas observadas (sucesso).
#Logo, a probabilidade de sucesso será p=4/10=0,4. Utilizando a fórmula apresentada, em que n=5 (número de
#retiradas) e k=3 (número de bolas vermelhas que temos interesse em observar), temos:
    
binom.pmf(3, 5, 0.4)
