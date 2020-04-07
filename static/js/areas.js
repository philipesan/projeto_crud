const areasBody = document.querySelector("#areas-tabela > tbody");
document.addEventListener("DOMContentLoaded", () => {carregaTabela();});

//Essa função é utilizada para pegar os itens que serão listados carregar a tabela.
function carregaTabela()
{
    const request = new XMLHttpRequest();
    const filtroId = document.getElementById("area");
    const filtroStatus = document.getElementById("status");
    var requestURL = "http://localhost:5000/areas_listar";
    if (filtroId.value && filtroStatus.value){
        var requestURL = "http://localhost:5000/areas_localizar/" + filtroId.value + "/" + filtroStatus.value;
    }
    if (filtroId.value && !filtroStatus.value) {
        var requestURL = "http://localhost:5000/areas_localizar_id/" + filtroId.value;
    }
    if (!filtroId.value && filtroStatus.value) {
        var requestURL = "http://localhost:5000/areas_localizar_status/" + filtroStatus.value;
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
    //Cria o JSON como texto
    var mensagem = [];
    //Loop pelas checkboxes
    for (var i = 0; i < checkBoxes.length; i++) 
    {
        if (checkBoxes[i].checked) 
        {
            var row = checkBoxes[i].parentNode.parentNode;
                mensagem.push({ "id": row.cells[0].innerHTML});
        }
    }
    //mensagem += ']';
    var url = "http://localhost:5000//inativa_areas";
    var metodo = "PUT";
    //var dados = JSON.parse(mensagem);
    var dados = JSON.stringify(mensagem);
    const request = new XMLHttpRequest();
    request.open(metodo, url);
    request.setRequestHeader("Content-type", "application/json");
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
    request.send(dados);
}