const areasBody = document.querySelector("#areas-tabela > tbody");
document.addEventListener("DOMContentLoaded", () => {carregaTabela();});

//Essa função é utilizada para pegar os itens que serão listados carregar a tabela.
function carregaTabela()
{
    const request = new XMLHttpRequest();
    const filtroId = document.getElementById("area");
    const filtroStatus = document.getElementById("status");
    if (filtroId.value) {
        var requestURL = "http://localhost:5000/areas_localizar/" + filtroId.value + "/" + filtroStatus.value;
    }
    else {
        var requestURL = "http://localhost:5000/areas_listar";
    }
    request.open("GET", requestURL);
    request.onload = () => {
        try {
            const json = JSON.parse(request.responseText);
            populaTabela(json);
        }
        catch (e) {
            alert("Erro no retorno da aplicação");
            console.warn(e);
        }
    }
    request.send();
}

//Essa função serve para exibir a tabela na tela com os itens que foram carregados
function populaTabela(json) 
{
    //Limpa a tabela HTML
    while(areasBody.firstChild)
    {
        areasBody.removeChild(areasBody.firstChild);
    };
    //Popula a tabela
    console.log(json);
    json.forEach(function(object) {
    var tr = document.createElement('tr');
    tr.innerHTML = '<td>' + object.id + '</td>' +
    '<td>' + (object.id_status == '0' ? "Ativo": "Inativo") + '</td>' +
    '<td>' + object.dt_adicao + '</td>' +
    '<td>' + object.dt_atualizacao + '</td>' +
    '<td><input type="checkbox" id="inativa'+ object.id +'"></td>';
    areasBody.appendChild(tr);
    });
}
//Essa função serve para pegar todos os itens que serão inativados
function deletarSelecionados() 
{
    //Pega a referência da tabela pelo ID
    var tabelas = document.getElementById("areas-tabela");
    //Pega todas as checkboxes
    var checkBoxes = tabelas.getElementsByTagName("INPUT");
    //Mensagem de DEBUG
    var message = "Itens a serem excluidos: \n";
    //Loop pelas checkboxes
    for (var i = 0; i < checkBoxes.length; i++) {
        if (checkBoxes[i].checked) {
            var row = checkBoxes[i].parentNode.parentNode;
            message += row.cells[0].innerHTML;
            message += "   " + row.cells[1].innerHTML;
            message += "   " + row.cells[2].innerHTML;
            message += "\n";
        }
    }
    //Mostra tudo em um Alert.
    alert(message);
}