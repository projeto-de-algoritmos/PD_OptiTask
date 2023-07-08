
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from algorithm import  Tarefa, find_lucro_maximo_jobs

tarefas=[] 

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def process_data():
    data = request.json  # Obtendo os dados JSON do corpo da requisição
    cont= data.get('contador')
    texto1 = data.get('valorInput')
    data1 = data.get('valorInput2')
    data2 = data.get('valorInput3')
    texto2 = data.get('valorInput4')

    tarefas.append(Tarefa(cont,texto1, convert_data_ms(data1), convert_data_ms(data2), int(texto2))) # Adiciona a tarefa na lista de tarefas

    #tarefas.append(Tarefa(cont,texto1, data1, data2, texto2)) # Adiciona a tarefa na lista de tarefas
    
   
    for t in tarefas:  # teste
        print('Nome da tarefa ' ,t.ident, t.nome, t.inicio, t.fim, t.lucro) # Imprime a lista de tarefas

    return jsonify({'valorInput': texto1, 'valorInput2': data1, 'valorInput3': data2, 'valorInput4': texto2})




@app.route('/calc', methods=['GET'])
def obter_tarefas():
    tarefas_realizadas = find_lucro_maximo_jobs(tarefas)
    lucro_total = 0
    # print("Lucro ótimo é:", lucro_otimo)
    print("Tarefas a serem realizadas:")
    for tarefa in tarefas_realizadas:
        lucro_total += tarefa.lucro
        print("Nome:", tarefa.nome, "Início:", tarefa.inicio, "Fim:", tarefa.fim, "Lucro:", tarefa.lucro)
    print(f'Lucro total é {lucro_total} !')
    # Converter a lista de tarefas em uma lista de dicionários
    tarefas_serializaveis = [tarefa.to_dict() for tarefa in tarefas_realizadas]

    # Retornar a lista de tarefas em formato JSON
    return jsonify(tarefas=tarefas_serializaveis)


'''
@app.route('/delete/<int:id>', methods=['GET'])
def deleter_tarefa(id):
    for tarefa in tarefas:
        if tarefa.ident == id:
            tarefas.remove(tarefa)
            return jsonify({'message': 'Item removido com sucesso'})
    return jsonify({'message': 'Item não encontrado'})

    print("Tarefas:")
    for i in tarefas:
       print("Nome:", i.nome, "Início:", i.inicio, "Fim:", i.fim, "Lucro:", i.lucro)
    # Retornar a lista de tarefas em formato JSON
    #return jsonify(tarefas=tarefas_serializaveis, lucro_otimo=lucro_otimo)


'''


def convert_data_ms(dataInput):
     # Formata a data do formulário em um objeto datetime
    data_f = datetime.strptime(dataInput, "%Y-%m-%d")
    dataMili = int (datetime.timestamp(data_f) * 1000)  # Converte a data para milissegundos
    print( dataMili)
    return dataMili


if __name__ == '__main__':
    app.run(debug=True)
    