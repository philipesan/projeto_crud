function validar() {
    const usuario = document.getElementById('usuario');
    const senha = document.getElementById('senha');

    if (nome.value === '') {
        alert("Preencha o nome.");
        return false;
    }
    if (nome.value === '') {
        alert("Preencha o nome.");
        return false;
    }

    return true;
}

function salvar() {
    if (!validar()) return;
    document.getElementById("form_principal").submit();
}
