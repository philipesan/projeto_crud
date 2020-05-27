//Essa função serve para realizar o cadastro
function realizarCadastro()
{
    var campo = document.getElementById("area");
    var mensagens = document.getElementById('mensagem');
    var resposta;
    if (campo.value.length <= 2)
    {
        campo.style.backgroundColor = "#fdff8f";
        alert("O Campo precisa ser preenchido!")
        mensagens.innerHTML = "Favor preencher o campo!"
    }
    enviaCadastro(campo.value);
    {

    }
}

//Envia o cadastro
function enviaCadastro(area)
{
    const xhr = new XMLHttpRequest();
    const requestURL = "http://localhost:5000/nova_area";
    const metodo = "POST";
    const dados = JSON.stringify({"id":area});
    var campo = document.getElementById("area");
    var mensagens = document.getElementById('mensagem');

    xhr.open(metodo, requestURL);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onload = () => {
        if(xhr.status === 201)
        {
            campo.style.backgroundColor = "#39e336";
            alert("Cadastrado com sucesso!");
            mensagens.innerHTML = "Area cadastrada com sucesso!"; 
        }
        else
        {
            alert("Erro no retorno da aplicação");
            console.warn(e);
        }
    };
    xhr.onerror = () => {
        console.error(xhr.statusText);
    };
    xhr.send(dados);

}