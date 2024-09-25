function startSimulation(algorithm) {
    if (!steps || !steps[algorithm] || steps[algorithm].length === 0) {
        console.error("**No hay acciones disponibles para este algoritmo.**");
        return;
    }

    // console.log(steps[algorithm]);
    const actions = steps[algorithm];
    const container = document.getElementById(`sim-${algorithm}`);
    const chainContainer = document.getElementById(`chain-${algorithm}`);
    let currentStep = 0;

    // Usar la palabra inicial almacenada
    let currentWord = Array.from(initialWord); // Cambiado a 'initialWord'
    let resultWord = Array.from(finalWord);

    container.innerHTML = `<div style="text-align: center; font-weight: bold;">${actions[currentStep]}</div>`;
    chainContainer.innerHTML = `<div style="text-align: center; font-weight: bold;">${formatWord(resultWord)}</div>`; // Muestra la palabra inicial.

    const interval = setInterval(() => {
        // Mostrar el estado actual
        container.innerHTML = `<div style="text-align: center; font-weight: bold;">${actions[currentStep]}</div>`;
        chainContainer.innerHTML = `<div style="text-align: center; font-weight: bold;">${formatWord(resultWord)}</div>`; // Muestra la palabra actualizada.

        currentStep++; // Mueve esto al final para asegurarte de que se procese la acción actual antes de incrementar

        if (currentStep >= actions.length) {
            clearInterval(interval);
            return;
        }
    }, 1000);
}

// Procesar cada acción y actualizar la palabra.

// Formatear y mostrar la palabra actual como una secuencia.
function formatWord(wordArray) {
    return wordArray.join(''); // Muestra la palabra concatenada sin espacios
}
