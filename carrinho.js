
let cart = JSON.parse(localStorage.getItem('carrinhoItems')) || [];


// Função para atualizar o carrinho
function updateCart() {
    const cartTableBody = document.querySelector("#cart tbody");
    const totalDisplay = document.getElementById('total');
    cartTableBody.innerHTML = '';

    let totalGeral = 0;

    cart.forEach((item, index) => {
        const itemTotal = (item.price * item.quantity).toFixed(2);
        totalGeral += parseFloat(itemTotal);

        const row = `
            <tr>
            <td>${item.name}</td>
            <td>R$ ${item.price}</td>
                <td>
                <input type="number" min="1" value="${item.quantity}" onchange="changeQuantity(${index}, this.value)">
                </td>
                <td>R$ ${itemTotal}</td>
                <td><button onclick="removeFromCart(${index})">Remover</button></td>
            </tr>
        `;

        cartTableBody.innerHTML += row;
    });
    totalDisplay.textContent = totalGeral.toFixed(2);
}
window.onload = updateCart;

// Função para adicionar itens ao carrinho
function addToCart(name, price,qtd) {
    const existingItem = cart.find(item => item.name === name);

    if (existingItem) {
        existingItem.quantity += qtd;
    } else {
        cart.push({ name, price, quantity: qtd });
    }

    updateCart();
}

// Função para remover itens do carrinho
function removeFromCart(index) {
    cart.splice(index, 1);
    updateCart();
}

// Função para alterar a quantidade de um item
function changeQuantity(index, quantity) {
    if (quantity < 1) return;
    cart[index].quantity = parseInt(quantity);
    updateCart();
}


// Função para "reservar" os itens no carrinho (simular reserva e redirecionamento)
function ReservarItems() {
    if (cart.length === 0) {
        alert("Seu carrinho está vazio! Adicione itens antes de comprar.");
        return;
    }

    // Simulando uma requisição para o backend (reserva dos itens)
    mockFetch('https://falso-backend.com/reserva', {
        method: 'POST',
        body: JSON.stringify({
            items: cart.map(item => ({ id: item.name, quantity: item.quantity }))
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (response.ok) {
            return response.json();  // Simula o retorno do backend
        } else {
            throw new Error('Erro na requisição de reserva');
        }
    })
    .then(data => {
        console.log("Reserva realizada com sucesso:", data);

        // Simulando que a reserva retornou com sucesso
        const reservedItems = cart.map(item => ({
            id: item.name, 
            quantity: item.quantity, 
            price: item.price
        }));

        // Salvando os itens reservados no localStorage
        localStorage.setItem('reservedItems', JSON.stringify(reservedItems));

        // Redirecionar o usuário para a tela de compra
        window.location.href = 'compra/compra.html';
    })
    .catch(error => {
        console.error("Erro na reserva:", error);
        alert('Falha ao reservar os itens. Tente novamente.');
    });
}

document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', () => {
        const name = button.getAttribute('data-name');
        const price = parseFloat(button.getAttribute('data-price'));

        addToCart(name, price);
    });
});

function mockFetch(url, options) {
    return new Promise((resolve, reject) => {
        console.log('Mock fetch called with:', url, options);

        // Simulando um delay de 1 segundo para a requisição
        setTimeout(() => {
            // Simulação de sucesso para a URL de reserva
            if (url === 'https://falso-backend.com/reserva' && options.method === 'POST') {
                // Simula uma resposta bem-sucedida
                resolve({
                    ok: true,
                    json: () => Promise.resolve({
                        message: "Reserva realizada com sucesso",
                        reservedItems: options.body
                    })
                });
            } else {
                // Simula um erro caso a URL ou método não sejam o esperado
                reject(new Error('Falha na requisição. URL ou método incorreto.'));
            }
        }, 1000); // Delay de 1 segundo
    });
}
