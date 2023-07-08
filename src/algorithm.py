# Programa em Python para escalonamento de tarefas ponderado usando
# Programação Dinâmica e Busca Binária

# Classe para representar uma tarefa
class Tarefa:
    def __init__(self,ident, nome, inicio, fim, lucro):
        self.ident = ident
        self.nome = nome
        self.inicio = inicio
        self.fim = fim
        self.lucro = lucro

    def to_dict(self):
        return {
            'ident': self.ident,
            'nome': self.nome,
            'inicio': self.inicio,
            'fim': self.fim,
            'lucro': self.lucro
        }


# Função de busca binária baseada em busca binária para encontrar a última tarefa
# (antes da tarefa atual) que não conflita com a tarefa atual.
# "index" é o índice da tarefa atual. Esta função
# retorna -1 se todas as tarefas antes do índice conflitarem com ela.
# O array tarefas[] é ordenado em ordem crescente de tempo de término.
def buscaBinaria(tarefa, indice_inicial):

    # Inicializa 'lo' e 'hi' para a busca binária
    lo = 0
    hi = indice_inicial - 1

    # Realiza a busca binária iterativamente
    while lo <= hi:
        meio = (lo + hi) // 2
        if tarefa[meio].fim <= tarefa[indice_inicial].inicio:
            if tarefa[meio + 1].fim <= tarefa[indice_inicial].inicio:
                lo = meio + 1
            else:
                return meio
        else:
            hi = meio - 1
    return -1


# A função principal que retorna o lucro máximo possível
# a partir de um array de tarefas dado
def escalonamento(tarefas):

    # Ordena as tarefas de acordo com o tempo de término
    tarefas = sorted(tarefas, key=lambda t: t.fim)

    # Cria um array para armazenar as soluções dos subproblemas. table[i]
    # armazena o lucro para as tarefas até tarefas[i] (incluindo tarefas[i])
    n = len(tarefas)
    tabela = [0 for _ in range(n)]

    tabela[0] = tarefas[0].lucro

    # Preenche as entradas na tabela[] usando a propriedade recursiva
    for i in range(1, n):

        # Encontra o lucro incluindo a tarefa atual
        lucro_incl = tarefas[i].lucro
        l = buscaBinaria(tarefas, i)
        if l != -1:
            lucro_incl += tabela[l]

        # Armazena o máximo entre a inclusão e a exclusão
        tabela[i] = max(lucro_incl, tabela[i - 1])

    # Encontra as tarefas que devem ser realizadas
    tarefas_realizadas = []
    indice = n - 1
    while indice >= 0:
        if indice == 0:
            tarefas_realizadas.append(tarefas[indice])
            break
        elif tabela[indice] != tabela[indice - 1]:
            tarefas_realizadas.append(tarefas[indice])
            indice = buscaBinaria(tarefas, indice)
        else:
            indice -= 1

    tarefas_realizadas.reverse()

    return tabela[n - 1], tarefas_realizadas


# Código de teste para a função acima
#tarefas = [Tarefa("Tarefa 1", 1, 2, 50), Tarefa("Tarefa 2", 3, 5, 20),
#           Tarefa("Tarefa 3", 6, 19, 100), Tarefa("Tarefa 4", 2, 100, 200)]

#tarefas=[Tarefa("Tarefa 1", 1688698800000, 1688785200000, 50), Tarefa("Tarefa 2",  1688871600000, 1689217200000, 20),
#         Tarefa("Tarefa 3", 1689303600000 , 1689908400000, 100), Tarefa("Tarefa 4",1688785200000 , 1691204400000, 200)]

#lucro_otimo, tarefas_realizadas = escalonamento(tarefas)

#print("Lucro ótimo é:", lucro_otimo)
#print("Tarefas a serem realizadas:")
#for tarefa in tarefas_realizadas:
#    print("Nome:", tarefa.nome, "Início:", tarefa.inicio, "Fim:", tarefa.fim, "Lucro:", tarefa.lucro)
