document.getElementById("icon_menu").addEventListener("click", mostrar_menu);

function mostrar_menu(){

    document.querySelector(".menu").classList.toggle("mostrar_menu");
    
}

window.onscroll = function () {
    var posicion = window.pageYOffset || document.documentElement.scrollTop;
    var elemento1 = document.getElementById("icon_heart");
    var elemento2 = document.getElementById("icon_fire");
    elemento1.style.bottom = posicion * 0.1 + "px";
    elemento2.style.top = posicion * 0.1 + "px";
}

//animacion de imagen 
const imagenAnimada = document.getElementById('imagenAnimada');

function animarImagen() {
    imagenAnimada.style.animationName = 'flipCoin, upAndDown';
    imagenAnimada.style.animationIterationCount = 'infinite';
  }

animarImagen();

// Animación utilizando Anime.js
const form = document.getElementById('contact-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); 

        // Animación del formulario usando Anime.js
        anime({
            targets: form,
            translateY: [-50, 0],
            opacity: [0, 1],
            duration: 1000,
            easing: 'easeOutExpo',
        });
    });

    function toggleSignInSignUp() {
        const $btnSignIn = document.querySelector('.sign-in-btn');
        const $btnSignUp = document.querySelector('.sign-up-btn');
        const $signUp = document.querySelector('.sign-up');
        const $signIn = document.querySelector('.sign-in');
    
        if ($btnSignIn && $btnSignUp && $signUp && $signIn) {
            document.addEventListener('click', e => {
                if (e.target === $btnSignIn || e.target === $btnSignUp) {
                    $signIn.classList.toggle('active');
                    $signUp.classList.toggle('active');
                }              
            });
        }
    }
    
    // Llama a la función cuando se cargue la página
    window.addEventListener('DOMContentLoaded', toggleSignInSignUp);
    
    