let cart = [];

function updateCart() {
    localStorage.setItem('carrinhoItems', JSON.stringify(cart));
}

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
