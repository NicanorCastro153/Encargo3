const button = document.getElementById('VerMensajes');
const Mensajes = document.getElementById('Mensajes');

button.addEventListener('click', function() {
    if (Mensajes.style.display === 'none') {
        Mensajes.style.display = 'block';
        button.textContent = 'Ocultar';
    } else {
        Mensajes.style.display = 'none';
        button.textContent = 'Ver Mensajes';
    }
});
