// Mapeando as variáveis exatamente como o professor ensinou
const modal = document.getElementById('meuModal');
const input_nome = document.getElementById('inputnome');
const msg_alerta = document.getElementById('msgalerta');

// 1. Função de abrir o card suspenso
function abrirmodal() {
    // Se estiver visível, fecha; se estiver escondido, abre! (Toggle)
    if (modal.style.display === 'block') {
        modal.style.display = 'none';
    } else {
        modal.style.display = 'block';
    }
}

// 2. Função de fechar no botão (X)
function fechar() {
    modal.style.display = 'none';
}

// 3. Função 'mudou' do professor
function mudou() {
    if (input_nome.value === "") {
        msg_alerta.style.color = "red";
        msg_alerta.style.fontSize = "11px";
        msg_alerta.textContent = "Digite algo válido!";
    } else {
        document.getElementById('nome-perfil').textContent = input_nome.value;
        msg_alerta.style.color = "green";
        msg_alerta.style.fontSize = "11px";
        msg_alerta.textContent = "Nome alterado!";
    }
}