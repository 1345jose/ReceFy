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

    // Iniciar el carrusel automático
    startAutoSlide();
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
