function calcularIMC() {
    var estatura = document.getElementById('estatura').value;
    var peso = document.getElementById('peso').value;
    var resultadoContainer = document.getElementById('resultadoContainer');

    // Limpiar resultados anteriores
    resultadoContainer.innerHTML = '';

    // Validar entrada
    if (estatura === '' || peso === '') {
        resultadoContainer.innerHTML = '<div class="alert alert-danger">Por favor, completa ambos campos.</div>';
        return;
    }

    // Convertir valores
    estatura = estatura.replace(',', '.'); // Convertir coma a punto decimal
    peso = peso.replace(',', '.');

    estatura = parseFloat(estatura);
    peso = parseFloat(peso);

    if (isNaN(estatura) || isNaN(peso)) {
        resultadoContainer.innerHTML = '<div class="alert alert-danger">Por favor, ingresa valores numéricos válidos.</div>';
        return;
    }

    // Calcular IMC
    var imc = peso / (estatura * estatura);

    // Mostrar resultado
    var resultado = '';
    if (imc < 18.5) {
        resultado = 'Bajo peso';
    } else if (imc >= 18.5 && imc <= 24.9) {
        resultado = 'Normal';
    } else if (imc >= 25 && imc <= 29.9) {
        resultado = 'Sobrepeso';
    } else {
        resultado = 'Obesidad';
    }

    resultadoContainer.innerHTML = '<div class="alert alert-success">Tu IMC es ' + imc.toFixed(2) + ' (' + resultado + ').</div>';
}