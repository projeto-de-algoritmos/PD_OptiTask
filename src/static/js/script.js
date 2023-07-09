let contador = 0;
let descTarefa = document.getElementById("inputTarefa");
let dataInicio = document.getElementById("inputTarefa2");
let dataFim = document.getElementById("inputTarefa3");
let preco = document.getElementById("inputTarefa4");
let btnAdd = document.getElementById("btn-add");
let main = document.getElementById("areaLista");
let lucroMaximoElement = document.createElement("div");


function verificarLucroMax() {
    document.getElementById("submit-button").addEventListener("click", function () {
        fetch('/calc')
            .then(response => response.json())
            .then(data => {
                const cardsContainer = document.getElementById("resultado"); // Criar um card para cada elemento do JSON recebido
                cardsContainer.innerHTML = ''; 
                lucroMaximoElement.innerHTML = ''; 
                lucroMaximoElement.classList.add("lucro-maximo");
                lucroMaximoElement.textContent = `Lucro máximo: ${data.lucro_total}`;
                cardsContainer.appendChild(lucroMaximoElement);

                data.tarefas.forEach(tarefa => {

                    const card = document.createElement("div");
                    card.classList.add("card");
                    card.innerHTML = ` 
                    <h3>${tarefa.nome}</h3>
                    <p>Início: ${tarefa.inicio}</p>
                    <p>Fim: ${tarefa.fim}</p>
                    <p>Lucro: ${tarefa.lucro}</p>
                `;
                    cardsContainer.appendChild(card);
                });

            })
            .catch(error => {
                console.error(error);
            });
    });
}

//Converte formato da data para o usuario
function convertDateFormat(dateString) {
    var dateParts = dateString.split("-");
    var year = dateParts[0];
    var month = dateParts[1];
    var day = dateParts[2];
    var formattedDate = day + "/" + month + "/" + year;
    return formattedDate;
  }
  
// Adicionar o evento de clique ao botão assim que a página for carregada
document.addEventListener('DOMContentLoaded', verificarLucroMax);

function addTarefa() {
    const cardsContainer = document.getElementById("resultado");
    cardsContainer.innerHTML = ''; 
    lucroMaximoElement.innerHTML = ''; 

    let valorInput = descTarefa.value;
    let valorInput2 =  dataInicio.value;
    let valorInput3 =  dataFim.value;
    let valorInput4 = preco.value;
    
    
    // verificar se o valor é válido em algum dos casos
    if (valorInput != "" || valorInput2 != "" || valorInput3 != "" || valorInput4 != "") {
        ++contador;
        let novoItem = `<div id="${contador}" class="item">
    
                <div onclick="marcarTarefa(${contador})" class="item-icone">
                    <i id="icone_${contador}" class="mdi mdi-circle-outline"></i>
                </div>

                <div onclick="marcarTarefa(${contador})" class="item-nome">
                  Tarefa: <span class="sem-negrito"> ${valorInput} </span> <br> Início: <span class="sem-negrito"> ${convertDateFormat(valorInput2)}</span> <br> Fim: <span class="sem-negrito"> ${convertDateFormat(valorInput3)}</span>  <br> Valor: <span class="sem-negrito"> R$ ${valorInput4} </span>
                </div>
                
                <div class="item-botao">
                    <button onclick="deletar(${contador})" class="delete"><i class="mdi mdi-delete"></i> Deletar</button>
                </div>
        </div>`;

        // inserir o novo item na lista
        main.innerHTML += novoItem;

        //zerar os inputs
        descTarefa.value = "";
        dataInicio.value = "";
        dataFim.value = "";
        preco.value = "";

        // objeto que representa cada tarefa adicionada com seus atributos
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

                console.log(data); // Resposta recebida do backend (Informações da tarefa adicionada)
            })
            .catch(error => {
                // Tratamento de erros
                console.error(error);
            });
    }
}


function deletar(id) {
    const cardsContainer = document.getElementById("resultado");
    lucroMaximoElement.innerHTML = ''; 
    var tarefa = document.getElementById(id);  // Pegar o elemento HTML da tarefa que será removida
    tarefa.remove();
    fetch('/delete/' + id, {
        method: 'DELETE'
    })
        .then(response => response.json())
        .then(data => {
            // Exibir se a tarefa foi removida com sucesso
            console.log(data);
        })
        .catch(error => {
            console.error(error);
        });
}

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

