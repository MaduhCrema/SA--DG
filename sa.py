"""POPULAÇÃO INICIAL POR ARREPENDIMENTO"""
#do maior valor de arrependimento para o menor, pega o menor valor da coluna da tarefa
#atribui a tarefa para a linha que esta, que vai ser o trabalhador
#faz isso ate atribuir todas as tarefa
#agora realiza trocas permitidas de vizinhos 3 vezes
n_linhas = input("Qual o número de funcionário/linhas?")
n_colunas = input("QUal o númeor de tarefas/colunas?")
TabelaHoras = []
TabelaCusto = []
TabelaArr = []
#tem a tabela de horas consumidas por tarefa
for i in range(int(n_linhas)):
    linha = []
    for j in range(int(n_colunas)):
        valor = input("Quantas horas tem a tarefa " + str(j) + " para o funcionário " + str(i) + "? ")
        linha.append(valor)
        
    TabelaHoras.append(linha)
#tem a tabela de custo por tarefa
for i in range(int(n_linhas)):
    linha = []
    for j in range(int(n_colunas)):
        valor = input("Quanto custa a tarefa " + str(j) + " para o funcionário " + str(i) + "? ")
        linha.append(int(valor))
        
    TabelaCusto.append(linha)

#subtrai os dois menores valores da tabela de horas, de todas as tarefas
for i in range(int(n_linhas)):
    menor = TabelaHoras[i][0]
    for j in range(int(n_colunas)):   
    
"""TEMPERATURA INICIAL - FAZ 3 VIZINHOS E A MEDIA SIMPLES"""
"""Escolher qual conta de resfriamento alfa/beta e determinar valor da variação"""
"""DEFINE PI COMO SOLUÇÃO INICAL E SOLUÇAO GLOBAL"""
"""DEFINE  O FITNESS/CUSTO DA SG/SI"""
"""DEFINE QUANTAS VEZES SERA FEITO O WHILE DAS INTERAÇÕES DOS VIZINHOS(SAMAX)"""
"""FAZ O DELTA = VI+1 - VI = SE DELTA < 0 SI = VIZINHO ATUAL"""
"""SE FITNESS DO VIZINHO ATUAL É MELHOR QUE SG ENTAO SG = VIZINHO ATUAL"""
"""ELSE RANDOM X(0,1), SE X < QUE P(E**(-DELTA/TEMPERATURA)) ENTÃO SI = VIZINHO ATUAL SE NÃO NADA OCORRE"""
"""FAZ ISSO ATE SAMAX ACABAR"""
"""FAZ RESFRIAMENTO DO ALFA/BETA E ATUALIZA TEMPERATURA"""
"""I=0"""
"""ACABA QUANDO A TEMPERATURA CHEGAR A ZERO"""
"""E RETORNA A SOLUÇÃO GLOBAL"""