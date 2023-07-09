
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
    data = request.json  
    identificador= data.get('contador')
    nome = data.get('valorInput')
    dataInicio = data.get('valorInput2')
    dataFim = data.get('valorInput3')
    preco = data.get('valorInput4')

    tarefas.append(Tarefa(identificador,nome, convert_data_ms(dataInicio), convert_data_ms(dataFim), int(preco))) 
   
    return jsonify({'valorInput': nome, 'valorInput2': dataInicio, 'valorInput3': dataFim, 'valorInput4': preco})



@app.route('/calc', methods=['GET'])
def obter_tarefas():
    tarefas_realizadas = find_lucro_maximo_jobs(tarefas)
    lucro_total = 0
  # Construir uma lista de dicionários com os detalhes das tarefas
    tarefas_serializaveis = []
    for tarefa in tarefas_realizadas:
        lucro_total += tarefa.lucro
        tarefas_serializaveis.append({
            "nome": tarefa.nome,
            "inicio": convert_ms_data(tarefa.inicio),
            "fim": convert_ms_data(tarefa.fim),
            "lucro": tarefa.lucro
        })

    # Adicionar o lucro total ao dicionário
    resultado = {
        "tarefas": tarefas_serializaveis,
        "lucro_total": lucro_total
    }

    # Converter o dicionário em formato JSON
    resultado_json = jsonify(resultado)

    # Retornar o JSON
    return resultado_json


@app.route('/delete/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    for tarefa in tarefas:
        if tarefa.identificador == id:
            tarefas.remove(tarefa)
            return jsonify({'message': 'Item removido com sucesso'})
    return jsonify({'message': 'Item não encontrado'})


def convert_data_ms(dataInput):
    dataFormatada = datetime.strptime(dataInput, "%Y-%m-%d")
    dataMili = int (datetime.timestamp(dataFormatada) * 1000)  
    return dataMili



def convert_ms_data(dataInput):
    data = datetime.fromtimestamp(dataInput / 1000.0)
    formato_data = "%d/%m/%Y"  
    data_formatada = data.strftime(formato_data)
    return data_formatada

if __name__ == '__main__':
    app.run(debug=True)
    