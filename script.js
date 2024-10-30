document.getElementById("signupForm").addEventListener("submit", function(event) {
    let hasError = false;

    const nome = document.getElementById("nome").value;
    if (nome === "") {
        showError("nomeError", "O campo 'Nome' é obrigatório.");
        hasError = true;
    } else {
        hideError("nomeError");
    }

    const email = document.getElementById("email").value;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        showError("emailError", "Por favor, insira um e-mail válido.");
        hasError = true;
    } else {
        hideError("emailError");
    }

    const celular = document.getElementById("celular").value;
    const celularRegex = /^[0-9]{10,11}$/;
    if (!celularRegex.test(celular)) {
        showError("celularError", "Por favor, insira um número de celular válido com código de área.");
        hasError = true;
    } else {
        hideError("celularError");
    }

    const senha = document.getElementById("senha").value;
    if (senha.length < 8) {
        showError("senhaError", "A senha deve ter pelo menos 8 caracteres.");
        hasError = true;
    } else {
        hideError("senhaError");
    }

    // Removido event.preventDefault() para testar o envio direto
});

function showError(elementId, message) {
    const element = document.getElementById(elementId);
    element.innerText = message;
    element.style.display = "block";
}

function hideError(elementId) {
    const element = document.getElementById(elementId);
    element.style.display = "none";
}
