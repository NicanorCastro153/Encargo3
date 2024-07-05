$(document).ready(function () {
    $("#formulario").validate({
        submitHandler: function (form) {
            mostrarModal();
        },
        rules: {
            nombre: {
                required: true,
                minlength: 3,
                digits: false
            },
            apellido: {
                required: true,
                minlength: 3,
                digits: false
            },
            email: {
                required: true,
                email: true
            },
            telefono: {
                required: true,
                minlength: 9,
                maxlength: 9,
                digits: true
            },
            textarea: {
                required: true,
                minlength: 30
            }
        },
        messages: {
            nombre: {
                required: "Por favor, ingresa tu nombre",
                minlength: "El nombre debe tener al menos 3 caracteres",
                digits: "El nombre no debe contener números"
            },
            apellido: {
                required: "Por favor, ingresa tu apellido",
                minlength: "El apellido debe tener al menos 3 caracteres",
                digits: "El número no debe contener números"
            },
            email: {
                required: "Por favor, ingresa un Email",
                email: "Por favor, ingresa una dirección de correo electrónico válida"
            },
            telefono: {
                required: "Por favor, ingresa un número válido",
                minlength: "El número debe tener 9 digitos",
                maxlength: "El número debe tener 9 digitos",
                digits: "Por favor, ingresa solo números"
            },
            textarea: {
                required: "Por favor, ingresa un motivo",
                minlength: "El motivo debe contener al menos 10 caracteres"
            }
        }
    });
});



document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("registrationForm").onsubmit = function() {
        var username = document.getElementById("username").value;
        var email = document.getElementById("email").value;
        var password1 = document.getElementById("password1").value;
        var password2 = document.getElementById("password2").value;

        if (password1 !== password2) {
            alert("Las contraseñas no coinciden");
            return false;
        }

        var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            alert("Por favor, ingrese un correo electrónico válido");
            return false;
        }

        if (username === "" || email === "" || password1 === "" || password2 === "") {
            alert("Todos los campos son obligatorios");
            return false;
        }

        return true;
    };
});