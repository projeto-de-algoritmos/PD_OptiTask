# Algoritmo que utiliza o Weighted Interval Scheduling para encontrar o lucro máximo de um conjunto de tarefas
# Os pesos do algoritmo são os lucros das tarefas no nosso caso
# Classe para representar uma tarefa
class Tarefa:
    def __init__(self,identificador,nome,inicio, fim, lucro):
        self.identificador = identificador
        self.nome = nome
        self.inicio = inicio
        self.fim = fim
        self.lucro = lucro

    def to_dict(self):
        return {
            'identificador': self.identificador,
            'nome': self.nome,
            'inicio': self.inicio,
            'fim': self.fim,
            'lucro': self.lucro
        }


def find_lucro_maximo_jobs(tarefas):
    if not tarefas:
        return []

    tarefas.sort(key=lambda x: x.inicio)
    n = len(tarefas)
    trabalhos = [[] for _ in range(n)]
    lucro_maximo = [0] * n

    for i in range(n):
        for j in range(i):
            if tarefas[j].fim <= tarefas[i].inicio and lucro_maximo[i] < lucro_maximo[j]:
                trabalhos[i] = trabalhos[j][:]
                lucro_maximo[i] = lucro_maximo[j]

        trabalhos[i].append(i)
        lucro_maximo[i] += int(tarefas[i].lucro)

    index = 0
    for i in range(1, n):
        if lucro_maximo[i] > lucro_maximo[index]:
            index = i

    result = []
    for i in trabalhos[index]:
        result.append(tarefas[i])

    return result

   