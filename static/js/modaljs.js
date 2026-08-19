// Captura dos elementos conforme a aula
const modal = document.getElementById('meuModal');
const input_nome = document.getElementById('inputnome');
const msg_alerta = document.getElementById('msgalerta');

// Mostra o card quando o mouse entra na área do perfil
function abrirmodal() {
    modal.style.display = 'block';
}

// Esconde o card quando o mouse sai da área do perfil
function fechar() {
    modal.style.display = 'none';
}

// Validação e alteração do nome no evento 'onchange'
function mudou() {
    if (input_nome.value === "") {
        msg_alerta.style.color = "red";
        msg_alerta.style.fontSize = "12px";
        msg_alerta.textContent = "Digite um nome!";
    } else {
        document.getElementById('nome-perfil').textContent = input_nome.value;
        msg_alerta.style.color = "green";
        msg_alerta.style.fontSize = "12px";
        msg_alerta.textContent = "Nome alterado com sucesso!";
    }
}