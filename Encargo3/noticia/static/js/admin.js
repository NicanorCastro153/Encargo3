document.addEventListener("DOMContentLoaded", function() {
    var botonVerMensajes = document.getElementById("VerMensajes");
    var tablaMensajes = document.getElementById("Mensajes");

    function toggleTablaMensajes() {
        if (tablaMensajes.style.display === "none") {
            tablaMensajes.style.display = "block";
            botonVerMensajes.textContent = "Ocultar Mensajes"
        } else {
            tablaMensajes.style.display = "none";
            botonVerMensajes.textContent = "Ver Mensajes"
        }
    }
    botonVerMensajes.addEventListener("click", function() {
        toggleTablaMensajes();
    });
});


document.addEventListener("DOMContentLoaded", function() {
    var botonCrearNoticia = document.getElementById("VerMensajes");
    var formularioNoticia = document.getElementById("FormularioNoticia");

    // Función para mostrar u ocultar el formulario de creación de noticias
    function toggleFormularioNoticia() {
        if (formularioNoticia.style.display === "none" || formularioNoticia.style.display === "") {
            formularioNoticia.style.display = "block";
        } else {
            formularioNoticia.style.display = "none";
        }
    }

    // Agregar evento clic al botón
    botonCrearNoticia.addEventListener("click", function() {
        toggleFormularioNoticia();
    });
});