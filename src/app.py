
import datetime
from flask import Flask, render_template, request, jsonify
from algorithm import  *

tarefas=[] 

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def process_data():
    data = request.json  # Obtendo os dados JSON do corpo da requisição
    texto1 = data.get('valorInput')
    data1 = data.get('valorInput2')
    data2 = data.get('valorInput3')
    texto2 = data.get('valorInput4')

    tarefas.append(Tarefa(texto1, data1, data2, texto2))

    for t in tarefas:  # teste
        print('Nome da tarefa ' ,t.nome, t.inicio, t.fim, t.lucro) # Imprime a lista de tarefas

    return jsonify({'valorInput': texto1, 'valorInput2': data1, 'valorInput3': data2, 'valorInput4': texto2})

    
if __name__ == '__main__':
    app.run(debug=True)
    