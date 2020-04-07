function validar(usuario, senha) {
    if (usuario.value === '') {
        alert("Preencha o nome de usuario.");
        return false;
    }
    if (senha.value === '') {
        alert("Preencha a senha.");
        return false;
    }

    return true;
}

function salvar() {
    const usuario = document.getElementById('usuario');
    const senha = document.getElementById('senha');
    var url = "http://localhost:5000/login";
    var metodo = "POST";
    if (!validar(usuario, senha)) return;
    var data = JSON.stringify({"usuario": usuario.value, "senha": senha.value});
    envia_request(metodo, url, data)
    .then(responseData => {
        console.log(responseData)
        window.location = "/menu";
    })
    .catch(err => {
        if (err == 403){
            alert("Usuário ou senha incorretos")
        }
    });
}

function envia_request(metodo, url, dados){
    const promise = new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open(metodo, url);
        if (dados){
            xhr.setRequestHeader("Content-Type", "application/json")
        };

        //Arrow function que recebe a resposta da requisição HTTP
        xhr.onload = () => {
            if (xhr.status == 403){
                reject(xhr.status);
            }
            resolve(xhr.response);
        };
        //Arrow function que trata erros HTTP
        xhr.onerror = () => {

            reject("Algo deu errado!");
        };

        xhr.send(dados);

    }
    );
    return promise;
}
