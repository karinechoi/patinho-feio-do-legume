const reservedItems = JSON.parse(localStorage.getItem('reservedItems')) || [];

// Função para carregar itens reservados e calcular o total
function loadReservedItems() {
    const productList = document.getElementById('product-list');
    const totalPriceDisplay = document.getElementById('total-price');
    let totalPrice = 0;

    if (reservedItems.length > 0) {
        reservedItems.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `${item.id} - Quantidade: ${item.quantity} - Preço: R$ ${(item.price * item.quantity).toFixed(2)}`;
            productList.appendChild(li);

            // Calculando o total da compra
            totalPrice += item.price * item.quantity;
        });
    } else {
        productList.innerHTML = '<li>Nenhum produto reservado.</li>';
    }

    // Exibindo o total da compra
    totalPriceDisplay.textContent = totalPrice.toFixed(2);
}

// Chamar a função ao carregar a página
window.onload = loadReservedItems;

// Mock PayPal Buttons
window.paypal
    .Buttons({
        style: {
            shape: "rect",
            layout: "vertical",
            color: "gold",
            label: "paypal",
        },

        // Criar ordem de pagamento mockada
        async createOrder() {
            try {
                // Simulação da criação de uma ordem no PayPal
                const orderMockResponse = {
                    id: 'ORDER1234', // ID fictício da ordem
                    status: 'CREATED',
                };

                console.log('Ordem criada:', orderMockResponse);
                window.location.href = '../Logout.html';
                return orderMockResponse.id; // Retorna o ID fictício da ordem
            } catch (error) {
                
                console.error('Erro ao criar ordem:', error);
                alert(`Erro ao iniciar o PayPal Checkout: ${error}`);
            }
        },

        // Aprovar a transação após a criação da ordem
        async onApprove(data, actions) {
            try {
                // Simulação de captura de pagamento
                const captureMockResponse = {
                    id: data.orderID,
                    status: 'COMPLETED', // Sucesso na transação mockada
                    purchase_units: [
                        {
                            payments: {
                                captures: [
                                    {
                                        id: 'CAPTURE1234',
                                        status: 'COMPLETED',
                                        amount: {
                                            currency_code: 'USD',
                                            value: '100.00',
                                        },
                                    },
                                ],
                            },
                        },
                    ],
                };

                console.log('Pagamento capturado:', captureMockResponse);
                alert(`Transação ${captureMockResponse.purchase_units[0].payments.captures[0].status}: ${captureMockResponse.purchase_units[0].payments.captures[0].id}`);
                
                // Redirecionar para página de acompanhamento ou finalizar compra
                window.location.href = "acompanhamento.html"; // Mude para sua página de acompanhamento
            } catch (error) {
                window.location.href = "acompanhamento.html"; // Mude para sua página de acompanhamento
                console.error('Erro ao capturar pagamento:', error);
                alert(`Desculpe, sua transação não pôde ser processada: ${error}`);
            }
        },
    })
.render("#paypal-button-container");