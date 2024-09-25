function startSimulation(algorithm) {
    console.log(algorithm);
    if (!steps || !steps[algorithm] || steps[algorithm].length === 0) {
        console.error("**No hay acciones disponibles para este algoritmo.**");
        return;
    }
    console.log(steps[algorithm]);

    let acciones = steps[algorithm];
    console.log('Acciones:');
    for (let accion of acciones) {
        console.log(accion);
        console.log('Tipo:', determinar_accion(accion));
        console.log('Parametros:', obtener_parametros(accion));
        console.log('---');
    }

    let palabra_vieja = initialWord;
    let palabra_nueva = finalWord;
    console.log('Palabra inicial:', palabra_vieja);
    console.log('Palabra final:', palabra_nueva);

    let delay = 1000;

    // Dependiendo del algoritmo, seleccionamos el div correspondiente
    let resultadoDiv = document.getElementById(`resultado-${algorithm}`);

    // Chequeo para asegurarse de que el div existe
    if (!resultadoDiv) {
        console.error(`Div no encontrado: resultado-${algorithm}`);
        return;
    }

    mostrar_con_delay(palabra_nueva, palabra_vieja, delay, resultadoDiv);
}

function determinar_accion(accion) {
    if (accion.includes('Avanzar')) {
        return 'Avanzar';
    } else if (accion.includes('Reemplazar')) {
        return 'Reemplazar';
    }
    return 'Insertar';
}
function obtener_parametros(accion) {
    if (accion.includes('==')){
        const parametros = accion.match(/\(([^)]+)\)/)[1];
        return parametros.split(' == ');
    }
    const parametros = accion.match(/\(([^)]+)\)/)[1];
    return parametros.split(' -> ');
    
}


function mostrar_con_delay(palabra_vieja, palabra_nueva, delay, resultadoDiv) {
    let maxLength = Math.max(palabra_vieja.length, palabra_nueva.length);
    resultadoDiv.innerHTML = ''; // Limpiar el contenido previo

    for (let i = 0; i < maxLength; i++) {
        setTimeout(() => {
            let parte_vieja = palabra_vieja.slice(0, i + 1);
            let parte_nueva = palabra_nueva.slice(0, i + 1);
            resultadoDiv.innerHTML += `Vieja: ${parte_vieja.padEnd(maxLength, ' ')} | Nueva: ${parte_nueva.padEnd(maxLength, ' ')}<br>`;
        }, i * delay);
    }
}
