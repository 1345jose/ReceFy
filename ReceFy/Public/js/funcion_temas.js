const channel = new BroadcastChannel('theme');

function toggleTheme() {
    const body = document.body;
    const sunIcon = document.getElementById('sun-icon');
    const moonIcon = document.getElementById('moon-icon');

    // Cambia entre las clases 'light-mode' y 'dark-mode'
    body.classList.toggle('light-mode');

    // Cambia la visibilidad de los íconos
    if (body.classList.contains('light-mode')) {
        sunIcon.style.display = 'none';
        moonIcon.style.display = 'inline';
        localStorage.setItem('theme', 'light'); // Guarda el tema claro
        channel.postMessage('light'); // Notifica a otros
    } else {
        sunIcon.style.display = 'inline';
        moonIcon.style.display = 'none';
        localStorage.setItem('theme', 'dark'); // Guarda el tema oscuro
        channel.postMessage('dark'); // Notifica a otros
    }
}

// Cargar el tema guardado al iniciar la página
window.onload = function() {
    const savedTheme = localStorage.getItem('theme');
    const body = document.body;
    const sunIcon = document.getElementById('sun-icon');
    const moonIcon = document.getElementById('moon-icon');

    if (savedTheme === 'light') {
        body.classList.add('light-mode');
        sunIcon.style.display = 'none';
        moonIcon.style.display = 'inline';
    } else {
        body.classList.remove('light-mode');
        sunIcon.style.display = 'inline';
        moonIcon.style.display = 'none';
    }
}

// Escuchar mensajes de otros canales
channel.onmessage = function(event) {
    const body = document.body;
    const sunIcon = document.getElementById('sun-icon');
    const moonIcon = document.getElementById('moon-icon');

    if (event.data === 'light') {
        body.classList.add('light-mode');
        sunIcon.style.display = 'none';
        moonIcon.style.display = 'inline';
    } else if (event.data === 'dark') {
        body.classList.remove('light-mode');
        sunIcon.style.display = 'inline';
        moonIcon.style.display = 'none';
    }
}