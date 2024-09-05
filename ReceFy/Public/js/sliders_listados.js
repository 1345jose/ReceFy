document.addEventListener("DOMContentLoaded", function() {
    var searchInput = document.getElementById("searchInput");
    var categoryContainers = document.querySelectorAll(".category-container");

    searchInput.addEventListener("input", function() {
        var searchTerm = searchInput.value.toLowerCase();

        categoryContainers.forEach(function(container) {
            var categoryCards = container.querySelectorAll(".recipe-card");
            var anyCategoryVisible = false;

            categoryCards.forEach(function(card) {
                var recipeTitle = card.querySelector(".card-title").textContent.toLowerCase();
                if (recipeTitle.includes(searchTerm)) {
                    card.style.display = "inline-block";
                    anyCategoryVisible = true;
                } else {
                    card.style.display = "none";
                }
            });

            container.style.display = anyCategoryVisible ? "block" : "none";
        });
    });

    // Iniciar el carrusel automático solo en dispositivos PC
    if (window.innerWidth > 768) {
        startAutoSlide();
    }
});

function startAutoSlide() {
    var sliders = document.querySelectorAll('.slider');
    sliders.forEach(function(slider) {
        var sliderWidth = slider.offsetWidth;
        var sliderTrack = slider.querySelector('.slider-track');
        var scrollWidth = sliderTrack.scrollWidth;
        var scrollPosition = 0;
        var interval = 2000; // Tiempo en milisegundos para el intervalo de desplazamiento

        setInterval(function() {
            scrollPosition += sliderWidth / 3; // Ajusta la velocidad del desplazamiento
            if (scrollPosition >= scrollWidth) {
                scrollPosition = 0; // Volver al inicio
            }
            slider.scrollTo({
                left: scrollPosition,
                behavior: 'smooth'
            });
        }, interval);
    });
}

function slide(direction, category) {
    var slider = document.getElementById("slider-" + category);
    var sliderWidth = slider.offsetWidth;
    var currentScroll = slider.scrollLeft;

    var newScroll = currentScroll + (direction === "left" ? -sliderWidth : sliderWidth);
    slider.scrollTo({
        left: newScroll,
        behavior: "smooth"
    });
}

// Escuchar cambios en el tamaño de la ventana para controlar el slider automático
window.addEventListener('resize', function() {
    if (window.innerWidth <= 768) {
        // Si el tamaño es menor o igual a 768px, podrías considerar detener el slider automático aquí
        // Si no necesitas implementar lógica adicional, simplemente deja esto vacío
    } else {
        // Reiniciar el slider automático si se vuelve a un tamaño mayor a 768px
        startAutoSlide();
    }
});
