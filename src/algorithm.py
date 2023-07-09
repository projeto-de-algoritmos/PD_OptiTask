# Programa em Python para escalonamento de tarefas ponderado usando
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



# if __name__ == '__main__':   
#     tarefas = [
#         Tarefa(1,'Job1',0, 6, 60),
#         Tarefa(2,'Job2',5, 9, 50),
#         Tarefa(3,'Job3',1, 4, 30),
#         Tarefa(4,'Job4',5, 7, 30),
#         Tarefa(5,'Job5',3, 5, 10),
#         Tarefa(6,'Job6',7, 8, 10)
#     ]

#     lucro_maximo_jobs = find_lucro_maximo_jobs(tarefas)
#     lucro_total = 0
    
# for tarefa in lucro_maximo_jobs:
#     lucro_total  += tarefa.lucro
#     print("Nome:", tarefa.nome, "Início:", tarefa.inicio, "Fim:", tarefa.fim, "Lucro:", tarefa.lucro)

   