var state = 
{
    querySet: '',
    pagina: 1,
    linhas: document.getElementById('qtePag').value,
    janela: 4,
};

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
            console.log(json);
            state.querySet = json;
            state.pagina = 1;
            state.linhas = document.getElementById('qtePag').value;      
            populaTabela();
        }
        catch (e) {
            alert("Erro no retorno da aplicação");
            console.warn(e);
        }
    }
    request.send();
}

//Função responsável pela paginação
function Paginacao(querySet, pagina, linhas)
{
    var trimStart = (pagina - 1) * linhas;
    var trimEnd = trimStart + linhas;
    var trimmedData = querySet.slice(trimStart, trimEnd);
    var paginas = Math.ceil(querySet.length / linhas);
    return {
        'querySet': trimmedData,
        'paginas': paginas
    }

}

//Controla os botões da paginação
function botoesPagina(paginas)
{
    var wrapper = document.getElementById('botoesPaginas');
    wrapper.innerHTML = '';

    var maxEsq = (state.pagina - Math.floor(state.janela / 2));
    var maxDir = (state.pagina + Math.floor(state.janela / 2));

    if (maxEsq < 1)
    {
        maxEsq = 1;
        maxDir = state.janela;
    }

    if (maxDir > paginas)
    {
        maxEsq = paginas - (state.janela - 1)
        maxDir = paginas
            if(maxEsq < 1)
            {
                maxEsq = 1
            }
    }
    for(var pagina = maxEsq; pagina <= maxDir; pagina++)
    {
        wrapper.innerHTML += `<button value=${pagina} class = "page btn btn-sm btn-success">${pagina}</button>`;
    }
    if (state.pagina != 1)
    {
        wrapper.innerHTML = `<button value=${1} class = "page btn btn-sm btn-success">Primeiro</button>` + wrapper.innerHTML;
    }
    if (state.pagina != paginas)
    {
        wrapper.innerHTML += `<button value=${paginas} class = "page btn btn-sm btn-success">Ultimo</button>`;
    }

    $('.page').on('click', function (){
        state.pagina = Number($(this).val())
        populaTabela()
    })
}

//Essa função serve para exibir a tabela na tela com os itens que foram carregados
function populaTabela() 
{
    //Limpa a tabela HTML
    while(areasBody.firstChild)
    {
        areasBody.removeChild(areasBody.firstChild);
    };
    //Popula a tabela
    var dados_pagina = Paginacao(state.querySet, state.pagina, state.linhas);
    console.log(dados_pagina);
    dados_pagina.querySet.forEach(function(object) {
    var tr = document.createElement('tr');
    tr.innerHTML = '<td>' + object.id + '</td>' +
    '<td>' + (object.id_status == '0' ? "Ativo": "Inativo") + '</td>' +
    '<td>' + object.dt_adicao + '</td>' +
    '<td>' + object.dt_atualizacao + '</td>' +
    '<td><input type="checkbox" id="inativa'+ object.id +'"></td>';
    areasBody.appendChild(tr);
    });
    botoesPagina(dados_pagina.paginas);
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
            state.querySet = json; 
            sstate.linhas = document.getElementById('qtePag').value;
            state.linhas = 5;   
            populaTabela();
        }
        catch (e) {
            alert("Erro no retorno da aplicação");
            console.warn(e);
        }
    }
    request.send(dados);
}
