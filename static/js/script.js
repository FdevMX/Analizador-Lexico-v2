document.addEventListener('DOMContentLoaded', function() {
    const textarea = document.querySelector('#codeInput');
    const pasteButton = document.querySelector('.paste');
    const clearButton = document.querySelector('.clear');
    const fileInput = document.querySelector('#fileInput');


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
    });

    fileInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (!file) {
            return;
        }
        const reader = new FileReader();
        reader.onload = function(e) {
            textarea.value = e.target.result;
        };
        reader.onerror = function(e) {
            console.error("Error al leer el archivo:", e);
            alert("Hubo un error al leer el archivo.");
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
        data.tokens.forEach(token => {
            const row = tableBody.insertRow();
            row.insertCell(0).textContent = token[0];
            row.insertCell(1).textContent = token[1];
            row.insertCell(2).textContent = token[2];
        });
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Ocurrió un error al procesar la solicitud.');
    });
}