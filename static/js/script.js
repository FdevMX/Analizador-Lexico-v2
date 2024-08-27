document.addEventListener('DOMContentLoaded', function() {
    const textarea = document.querySelector('#codeInput');
    const pasteButton = document.querySelector('.paste');
    const clearButton = document.querySelector('.clear');
    const fileInput = document.querySelector('#fileInput');
    const countersDiv = document.querySelector('#counters');
    const tokenTypesTable = document.querySelector('#tokenTypesTable');

    // Ocultar los contadores y la tabla al cargar la página
    countersDiv.style.display = 'none';
    tokenTypesTable.style.display = 'none';

    pasteButton.addEventListener('click', async function() {
        try {
            const text = await navigator.clipboard.readText();
            textarea.value = text;
        } catch (err) {
            console.error('Error al pegar:', err);
        }
    });

    clearButton.addEventListener('click', function() {
        textarea.value = '';
        document.querySelector('#resultTable tbody').innerHTML = '';
        // Resetear y ocultar los contadores y la tabla
        document.getElementById('tokenCount').textContent = '0';
        document.getElementById('tokenTypesCount').textContent = '0';
        countersDiv.style.display = 'none';
        tokenTypesTable.style.display = 'none';
        tokenTypesTable.querySelector('tbody').innerHTML = '';
        fileInput.value = '';
    });

    fileInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (!file) {
            return;
        }
        const reader = new FileReader();
        reader.onload = function(e) {
            textarea.value = e.target.result;
            // Resetear el input de archivo después de leer
            fileInput.value = '';
        };
        reader.onerror = function(e) {
            console.error("Error al leer el archivo:", e);
            alert("Hubo un error al leer el archivo.");
            // Resetear el input de archivo en caso de error
            fileInput.value = '';
        };
        reader.readAsText(file);
    });
});

function analizarCodigo() {
    const code = document.getElementById('codeInput').value;
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `code=${encodeURIComponent(code)}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
            return;
        }
        const tableBody = document.querySelector('#resultTable tbody');
        tableBody.innerHTML = '';
        
        // Objeto para contar la frecuencia de cada tipo de token
        const tokenTypesFrequency = {};
        
        data.tokens.forEach(token => {
            const row = tableBody.insertRow();
            row.insertCell(0).textContent = token[0];
            row.insertCell(1).textContent = token[1];
            row.insertCell(2).textContent = token[2];
            
            // Contar la frecuencia de cada tipo de token
            tokenTypesFrequency[token[0]] = (tokenTypesFrequency[token[0]] || 0) + 1;
        });

        // Actualizar y mostrar los contadores
        document.getElementById('tokenCount').textContent = data.token_count;
        document.getElementById('tokenTypesCount').textContent = data.token_types_count;
        document.getElementById('counters').style.display = 'block';

        // Actualizar la tabla de tipos de tokens
        const tokenTypesTableBody = document.querySelector('#tokenTypesTable tbody');
        tokenTypesTableBody.innerHTML = '';
        for (const [tokenType, frequency] of Object.entries(tokenTypesFrequency)) {
            const row = tokenTypesTableBody.insertRow();
            row.insertCell(0).textContent = tokenType;
            row.insertCell(1).textContent = frequency;
        }
        document.getElementById('tokenTypesTable').style.display = 'table';
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Ocurrió un error al procesar la solicitud.');
    });
}