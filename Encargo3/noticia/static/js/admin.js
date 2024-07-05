document.addEventListener("DOMContentLoaded", function() {
    var botonVerMensajes = document.getElementById("VerMensajes");
    var contenedorMensajes = document.getElementById("ContenedorMensajes");

    function toggleTablaMensajes() {
        if (contenedorMensajes.style.display === "none") {
            contenedorMensajes.style.display = "block";
            botonVerMensajes.textContent = "Cerrar";
        } else {
            contenedorMensajes.style.display = "none";
            botonVerMensajes.textContent = "Ver Mensajes";
        }
    }

    botonVerMensajes.addEventListener("click", function() {
        toggleTablaMensajes();
    });
});


document.addEventListener("DOMContentLoaded", function() {
    var botonCrearNoticia = document.getElementById("CrearNoticia");
    var formularioNoticia = document.getElementById("Noticia");

    function toggleFormularioNoticia() {
        if (formularioNoticia.style.display === "none" || formularioNoticia.style.display === "") {
            formularioNoticia.style.display = "block";
            botonCrearNoticia.textContent = "Cerrar";
        } else {
            formularioNoticia.style.display = "none";
            botonCrearNoticia.textContent = "Crear Noticia";
        }
    }

    botonCrearNoticia.addEventListener("click", function() {
        toggleFormularioNoticia();
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var botonVerNoticias = document.getElementById("VerNoticias");
    var divNoticias = document.getElementById("Noticias");

    function toggleNoticias() {
        if (divNoticias.style.display === "none" || divNoticias.style.display === "") {
            divNoticias.style.display = "block";
            botonVerNoticias.textContent = "Cerrar";
        } else {
            divNoticias.style.display = "none";
            botonVerNoticias.textContent = "Ver Noticias";
        }
    }

    botonVerNoticias.addEventListener("click", function() {
        toggleNoticias();
    });
});

