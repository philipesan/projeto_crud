const id_produto = "{{id_produto}}";

function validar() {
    const descricao = document.getElementById('descricao');
    const cliente = document.getElementById('cliente');
    if (descricao.value === '') {
        alert("Preencha a descrição.");
        return false;
    }
    if (cliente.value == "escolha") {
        alert("Escolha o cliente.");
        return false;
    }
    return true;
}

function salvar() {
    if (!validar()) return;
    document.getElementById("form_principal").submit();
}

function excluir() {
    if (!confirm("Você tem certeza?")) return;
    xhr = new XMLHttpRequest();
    xhr.open('DELETE', '/produto/' + id_produto);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
        if (xhr.readyState !== 4) return;
        if (xhr.status === 200 || xhr.status === 404) {
            document.open();
            document.write(xhr.responseText);
            document.close();
        } else {
            alert('Erro ' + xhr.status);
        }
    };
    xhr.send();
}
