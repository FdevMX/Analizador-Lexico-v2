from flask import Flask, render_template, request, jsonify, send_from_directory
import re
from anaTokens import token_patterns

app = Flask(__name__)

# Rutas para servir archivos estáticos desde las carpetas 'views' y 'assets'
@app.route('/views/<path:filename>')
def serve_views(filename):
    return send_from_directory('static', filename)

# Preparar la expresión regular para el análisis léxico
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_patterns)
get_token = re.compile(token_regex).match

def tokenize(code):
    line_number = 1
    position = 0
    tokens = []

    while position < len(code):
        match = get_token(code, position)
        if not match:
            raise RuntimeError(f'Error de Análisis en posición {position}')

        for name, value in match.groupdict().items():
            if value:
                if name != 'ESPACIO':
                    tokens.append((name, value, line_number))
                break
        position = match.end()

        if position < len(code) and code[position] == '\n':
            line_number += 1

    return tokens

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form.get('code', '')
        try:
            tokens_list = tokenize(code)
            return jsonify({'tokens': tokens_list})
        except RuntimeError as e:
            return jsonify({'error': str(e)}), 400
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)