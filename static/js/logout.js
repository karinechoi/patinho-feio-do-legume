document.addEventListener('DOMContentLoaded', function() {
    const logoutButton = document.getElementById('logout');

    logoutButton.addEventListener('click', async function(event) {
        event.preventDefault();
        try {
            await logout();
            window.location.href = '/login.html';
        } catch (error) {
            console.error('Erro ao fazer logout:', error);
            alert('Erro ao fazer logout. Tente novamente.');
        }
    });
}); 