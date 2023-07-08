let contador = 0;
let descTarefa = document.getElementById("inputTarefa");
let dataInicio = document.getElementById("inputTarefa2");
let dataFim = document.getElementById("inputTarefa3");
let preco = document.getElementById("inputTarefa4");
let btnAdd = document.getElementById("btn-add");
let main = document.getElementById("areaLista");




function verificarLucroMax() {
    document.getElementById("submit-button").addEventListener("click", function () {
        fetch('/calc')
            .then(response => response.json())
            .then(tarefas => {
                // Exibir o resultado no console
                console.log(tarefas);
            })
            .catch(error => {
                console.error(error);
            });
    });
}
// Adicionar o evento de clique ao botão assim que a página for carregada
document.addEventListener('DOMContentLoaded', verificarLucroMax);

function addTarefa() {
    //PEGAR O VALOR DIGITADO NO descTarefa
    let valorInput = descTarefa.value;
    let valorInput2 = dataInicio.value;
    let valorInput3 = dataFim.value;
    let valorInput4 = preco.value;


    // verificar se o valor é válido em algum dos casos
    if (valorInput != "" || valorInput2 != "" || valorInput3 != "" || valorInput4 != "") {
        ++contador;
        let novoItem = `<div id="${contador}" class="item">
    
                <div onclick="marcarTarefa(${contador})" class="item-icone">
                    <i id="icone_${contador}" class="mdi mdi-circle-outline"></i>
                </div>

                <div onclick="marcarTarefa(${contador})" class="item-nome">
                    ${valorInput}   ${valorInput2}  ${valorInput3} ${valorInput4}
                </div>
                
                <div class="item-botao">
                    <button onclick="deletar(${contador})" class="delete"><i class="mdi mdi-delete"></i> Deletar</button>
                </div>
        </div>`;

        // inserir o novo item na lista
        main.innerHTML += novoItem;

        //zerar o input
        descTarefa.value = "";
        dataInicio.value = "";
        dataFim.value = "";
        preco.value = "";




        const dados = {
            contador: contador,
            valorInput: valorInput,
            valorInput2: valorInput2,
            valorInput3: valorInput3,
            valorInput4: valorInput4
        };


        fetch("/submit", {

            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dados)  // converter o objeto "dados" em uma string JSON que será enviada no corpo da requisição.
        })
            .then(response => response.json()) // Obtém a resposta como objeto JSON
            .then(data => {
                // Manipulação dos dados recebidos
                console.log(data); // Resposta recebida do backend
            })
            .catch(error => {
                // Tratamento de erros
                console.error(error);
            });
    }
}

/*
function deletar(id) {
            var tarefa = document.getElementById(id);
            tarefa.remove();

            document.getElementById("deletar").addEventListener("click", function () {
                fetch('/delete/${id}')
                    .then(response => response.json())
                    .then(tarefas => {
                        // Exibir o resultado no console
                        console.log(tarefas);
                    })
                    .catch(error => {
                        console.error(error);
                    });
            });

        }
*/
function marcarTarefa(id) {
    var item = document.getElementById(id);
    var classe = item.getAttribute("class");
    console.log(classe);

    if (classe == "item") {
        item.classList.add("clicado");

        var icone = document.getElementById("icone_" + id);
        icone.classList.remove("mdi-circle-outline");
        icone.classList.add("mdi-check-circle");

        item.parentNode.appendChild(item);
    } else {
        item.classList.remove("clicado");

        var icone = document.getElementById("icone_" + id);
        icone.classList.remove("mdi-check-circle");
        icone.classList.add("mdi-circle-outline");
    }
}

