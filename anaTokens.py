# lexical_analysis.py
funcSpecialMetod = [
    # Palabras reservadas para funciones y métodos especiales
    '__init__', '__del__', '__repr__', '__str__', '__bytes__', '__format__', '__lt__', '__le__',
    '__eq__', '__ne__', '__gt__', '__ge__', '__hash__', '__bool__', '__getattr__', '__setattr__',
    '__delattr__', '__dir__', '__get__', '__set__', '__delete__', '__call__', '__len__', '__getitem__',
    '__setitem__', '__delitem__', '__iter__', '__next__', '__reversed__', '__contains__', '__add__',
    '__sub__', '__mul__', '__truediv__', '__floordiv__', '__mod__', '__divmod__', '__pow__', '__lshift__',
    '__rshift__', '__and__', '__xor__', '__or__', '__iadd__', '__isub__', '__imul__', '__itruediv__',
    '__ifloordiv__', '__imod__', '__ipow__', '__ilshift__', '__irshift__', '__iand__', '__ixor__',
    '__ior__', '__neg__', '__pos__', '__abs__', '__invert__', '__complex__', '__int__', '__float__',
    '__index__', '__round__', '__trunc__', '__floor__', '__ceil__', '__enter__', '__exit__',
    '__await__', '__aiter__', '__anext__', '__aenter__', '__aexit__', '__main__'
]

funcExcepManag = [
    # Palabras reservadas para excepciones
    'BaseException', 'Exception', 'ArithmeticError', 'BufferError', 'LookupError', 'AssertionError',
    'AttributeError', 'EOFError', 'FloatingPointError', 'GeneratorExit', 'ImportError', 'IndexError',
    'KeyError', 'KeyboardInterrupt', 'MemoryError', 'NameError', 'NotImplementedError', 'OSError',
    'OverflowError', 'ReferenceError', 'RuntimeError', 'StopIteration', 'SyntaxError', 'IndentationError',
    'TabError', 'SystemError', 'SystemExit', 'TypeError', 'UnboundLocalError', 'UnicodeError',
    'UnicodeEncodeError', 'UnicodeDecodeError', 'UnicodeTranslateError', 'ValueError', 'ZeroDivisionError',
]

funcModuleManag = [
    # Palabras reservadas para módulos y paquetes
    '__name__', '__package__', '__path__', '__file__', '__doc__', '__all__', '__version__',
    '__author__', '__email__', '__copyright__', '__license__', '__status__', '__maintainer__',
    '__credits__',
]

funcCorrutManag = [
    # Palabras reservadas para generadores y corrutinas
    'yield', 'yield from', 'async', 'await',
]

funcFilesManag = [
    # Palabras reservadas para manejo de archivos
    'open', 'close', 'read', 'write', 'append', 'flush', 'seek', 'tell', 'truncate',
]

funcTimeManag = [
    # Palabras reservadas para manejo de fechas y tiempos
    'datetime', 'date', 'time', 'timedelta', 'timezone', 'tzinfo',
]

funcSubprocManag = [
    # Palabras reservadas para manejo de subprocesos
    'threading', 'Thread', 'Lock', 'RLock', 'Condition', 'Semaphore', 'BoundedSemaphore', 'Event',
    'Timer', 'Barrier',
]

funcDataManag = [
    # Palabras reservadas para manejo de datos
    'json', 'pickle', 'csv', 'xml', 'html', 'url', 'base64', 'hashlib', 'hmac', 'uuid',
]

funcMathManag = [
    # Palabras reservadas para manejo de matemáticas
    'math', 'random', 'statistics', 'decimal', 'fractions', 'cmath', 'numpy', 'scipy',
]

funcGrapManag = [
    # Palabras reservadas para manejo de gráficos
    'turtle', 'tkinter', 'pygame', 'matplotlib', 'plotly', 'seaborn',
]

funcWebManag = [
    # Palabras reservadas para manejo de web
    'flask', 'django', 'requests', 'beautifulsoup', 'scrapy',
]

funcSysManag = [
    # Palabras reservadas para manejo de sistemas
    'os', 'sys', 'subprocess', 'shutil', 'glob', 'pathlib', 'tempfile', 'io', 'logging', 'configparser',
    'argparse', 'getopt', 'optparse', 'platform', 'ctypes', 'gc', 'itertools', 'functools', 'operator',
    'collections', 'enum', 'abc', 'contextlib', 'copy', 'pprint', 'unittest', 'doctest', 'traceback',
    'inspect', 'dis', 'pickletools', 'timeit', 'cProfile', 'profile', 'pstats', 'trace', 'linecache',
    'code', 'codeop', 'compileall', 'py_compile', 'zipfile', 'gzip', 'bz2', 'lzma', 'tarfile', 'zipimport',
    'importlib', 'pkgutil', 'modulefinder', 'runpy', 'venv', 'ensurepip', 'site', 'user', 'distutils',
    'sysconfig', 'imp', 'importlib', 'pkg_resources', 'setuptools', 'pip', 'wheel', 'virtualenv',
    'tox', 'pytest', 'coverage', 'sphinx', 'autopep8', 'black', 'flake8', 'mypy', 'pylint', 'bandit',
    'safety', 'pre-commit', 'twine', 'pyinstaller', 'cx_Freeze', 'py2exe', 'py2app', 'nuitka', 'shiv'
]

reserved_words = [
    'elif', 'for', 'in', 'while', 'break', 'continue', 'pass', 'return',
    'def', 'class', 'try', 'except', 'finally', 'with', 'as', 'raise', 'assert', 'import',
    'from', 'global', 'nonlocal', 'lambda', 'True', 'False', 'None',
    'async', 'await', 'yield', 'del', 'is', 'in', 'not', 'with', 'as',
    'except', 'finally', 'try', 'raise', 'assert', 'yield', 'break', 'continue', 'pass',
    'class', 'def', 'del', 'from', 'global', 'if', 'import', 'lambda', 'nonlocal', 'while',
    'with', 'yield', 'async', 'await'

    # Palabras reservadas adicionales en Python
    'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr',
    'classmethod', 'compile', 'complex', 'delattr', 'dict', 'dir', 'divmod', 'enumerate',
    'eval', 'exec', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
    'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len',
    'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open',
    'ord', 'pow', 'print', 'property', 'range', 'repr', 'reversed', 'round', 'set', 'setattr',
    'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip',
    '__import__',

]

reserved_pattern = r'\b(' + '|'.join(reserved_words) + r')\b'
specialMetod_pattern = r'\b(' + '|'.join(funcSpecialMetod) + r')\b'
excepManag_pattern = r'\b(' + '|'.join(funcExcepManag) + r')\b'
moduleManag_pattern = r'\b(' + '|'.join(funcModuleManag) + r')\b'
corrutManag_pattern = r'\b(' + '|'.join(funcCorrutManag) + r')\b'
filesManag_pattern = r'\b(' + '|'.join(funcFilesManag) + r')\b'
timeManag_pattern = r'\b(' + '|'.join(funcTimeManag) + r')\b'
subprocManag_pattern = r'\b(' + '|'.join(funcSubprocManag) + r')\b'
dataManag_pattern = r'\b(' + '|'.join(funcDataManag) + r')\b'
mathManag_pattern = r'\b(' + '|'.join(funcMathManag) + r')\b'
grapManag_pattern = r'\b(' + '|'.join(funcGrapManag) + r')\b'
webManag_pattern = r'\b(' + '|'.join(funcWebManag) + r')\b'
sysManag_pattern = r'\b(' + '|'.join(funcSysManag) + r')\b'

token_patterns = [
    ('PALABRA_RESERVADA', reserved_pattern), # Palabra reservada
    ('FUNCION_ESPECIAL', specialMetod_pattern), # Funciones especiales
    ('FUNCION_EXCEPCION', excepManag_pattern), # Funciones de excepcion
    ('FUNCION_MODULO', moduleManag_pattern), # Funciones de módulo
    ('FUNCION_CORRUTINA', corrutManag_pattern), # Funciones de corrutina
    ('FUNCION_ARCHIVOS', filesManag_pattern), # Funciones de manejo de archivos
    ('FUNCION_TIEMPO', timeManag_pattern), # Funciones de manejo de tiempo
    ('FUNCION_SUBPROCESOS', subprocManag_pattern), # Funciones de manejo de subprocesos
    ('FUNCION_DATOS', dataManag_pattern), # Funciones de manejo de datos
    ('FUNCION_MATEMATICAS', mathManag_pattern), # Funciones matemáticas
    ('FUNCION_GRAFICOS', grapManag_pattern), # Funciones de gráficos
    ('FUNCION_WEB', webManag_pattern), # Funciones de manejo web
    ('FUNCION_SISTEMA', sysManag_pattern), # Funciones de manejo de sistema
    
    ('NUMERO', r'\d+'),                      # Número entero
    ('IDENTIFICADOR', r'[A-Za-z_]\w*'),      # Identificador
    ('SUMA', r'\+'),                         # Operador de suma
    ('RESTA', r'-'),                         # Operador de resta
    ('MULTIPLICACION', r'\*'),               # Operador de multiplicación
    ('DIVISION', r'/'),                      # Operador de división
    ('PARENTESIS_IZQ', r'\('),               # Paréntesis izquierdo
    ('PARENTESIS_DER', r'\)'),               # Paréntesis derecho
    ('COMA', r','),                          # Coma
    ('PUNTO_Y_COMA', r';'),                  # Punto y coma
    ('DOS_PUNTOS', r':'),                    # Dos puntos
    ('IGUAL', r'='),                         # Operador de asignación
    ('MENOR_QUE', r'<'),                     # Operador menor que
    ('MAYOR_QUE', r'>'),                     # Operador mayor que
    ('MENOR_IGUAL', r'<='),                  # Operador menor o igual
    ('MAYOR_IGUAL', r'>='),                  # Operador mayor o igual
    ('IGUAL_IGUAL', r'=='),                  # Operador de igualdad
    ('DIFERENTE', r'!='),                    # Operador de desigualdad
    ('POTENCIA', r'\*\*'),                   # Operador de potencia
    ('MODULO', r'%'),                        # Operador de módulo
    ('MAS_IGUAL', r'\+='),                   # Operador de suma y asignación
    ('MENOS_IGUAL', r'-='),                  # Operador de resta y asignación
    ('POR_IGUAL', r'\*='),                   # Operador de multiplicación y asignación
    ('DIV_IGUAL', r'/='),                    # Operador de división y asignación
    ('MOD_IGUAL', r'%='),                    # Operador de módulo y asignación
    ('POT_IGUAL', r'\*\*='),                 # Operador de potencia y asignación
    ('ESPACIO', r'\s+'),                     # Espacios
    ('SIMBOLO', r'.'),                       # Otros caracteres
    ('COMILLAS_SIMPLES', r'\''),             # Comillas simples
    ('COMILLAS_DOBLES', r'\"'),              # Comillas dobles
    ('LLAVE_IZQ', r'{'),                     # Llave izquierda
    ('LLAVE_DER', r'}'),                     # Llave derecha
    ('CORCH_IZQ', r'\['),                    # Corchete izquierdo
    ('CORCH_DER', r'\]'),                    # Corchete derecho
    ('PUNTO', r'\.'),                        # Punto
    ('ARROBA', r'@'),                        # Arroba
    ('DOLAR', r'\$'),                        # Dólar
    ('GATO', r'\^'),                         # Gato
    ('BARRA_INVERSA', r'\\'),                # Barra invertida
    ('BARRA', r'/'),                         # Barra
    ('ASTERISCO', r'\*'),                    # Asterisco
    ('MAS', r'\+'),                          # Más
    ('MENOS', r'-'),                         # Menos
    ('TILDE', r'~'),                         # Tilde
    ('PIPE', r'\|'),                         # Pipe
    ('CIRCUNFLEXO', r'\^'),                  # Circunflejo
    ('DOS_PUNTOS_IGUAL', r'::'),             # Dos puntos igual
    ('MAYUSCULA', r'[A-Z]'),                 # Letra mayúscula
    ('MINUSCULA', r'[a-z]'),                 # Letra minúscula
    ('DIGITO', r'\d'),                       # Dígito
    ('NO_DIGITO', r'\D'),                    # No dígito
    ('LETRA', r'\w'),                        # Letra
    ('NO_LETRA', r'\W'),                     # No letra
    ('ESPACIO_BLANCO', r'\s'),               # Espacio en blanco
    ('NO_ESPACIO_BLANCO', r'\S'),            # No espacio en blanco
    ('COMENTARIO', r'\#.*'),                 # Comentario
    ('DECIMAL', r'\d+\.\d+'),                # Número decimal
    ('EXPONENTE', r'\d+[eE][-+]?\d+'),       # Número en notación exponencial
    ('CADENA_MULTILINEA', r'\"\"\".*?\"\"\"'), # Cadena multilinea entre comillas triples
    ('CADENA_MULTILINEA_SIMPLE', r"\'\'\'.*?\'\'\'"), # Cadena multilinea entre comillas triples simples
    ('COMENTARIO_MULTILINEA', r'\"\"\"[^\"]*\"\"\"'), # Comentario multilinea entre comillas triples
    ('PREGUNTA', r'\?'),                     # Signo de interrogación (no común en Python pero puede ser útil en otros contextos)
    ('GUION_BAJO', r'_'),                    # Guion bajo (a menudo usado en nombres de variables en Python)
    ('COMENTARIO_LINEA', r'#.*'),            # Comentario de una línea
    ('CADENA_SIMPLE', r'\'[^\']*\''),        # Cadena entre comillas simples
    ('CADENA_DOBLE', r'\"[^\"]*\"'),         # Cadena entre comillas dobles
    ('OPERADOR_BITWISE', r'&|\||~|\^'),      # Operadores bitwise (AND, OR, NOT, XOR)
    ('OPERADOR_LOGICO', r'and|or|not'),      # Operadores lógicos
    ('OPERADOR_TERNARIO', r'\?|:'),          # Operador ternario (no estándar en Python pero puede ser útil)
    ('OPERADOR_INCREMENTO', r'\+\+'),        # Operador de incremento (no estándar en Python pero puede ser útil)
    ('OPERADOR_DECREMENTO', r'--'),          # Operador de decremento (no estándar en Python pero puede ser útil)
    ('OPERADOR_DESPLAZAMIENTO', r'<<|>>'),   # Operadores de desplazamiento (no estándar en Python pero puede ser útil)
    ('OPERADOR_COMPARACION', r'==|!=|<|>|<=|>='), # Operadores de comparación
    ('OPERADOR_ASIGNACION', r'=|\+=|-=|\*=|/=|%=|\*\*=|//='), # Operadores de asignación
    ('OPERADOR_INDICE', r'\['),              # Operador de índice (corchete izquierdo)
    ('OPERADOR_LLAMADA', r'\('),             # Operador de llamada (paréntesis izquierdo)
    ('OPERADOR_TERNARIO_PYTHON', r'if|else'), # Operador ternario en Python
    ('OPERADOR_RANGE', r'\.\.'),             # Operador de rango (no estándar en Python pero puede ser útil)
    ('OPERADOR_CONCATENACION', r'\+'),       # Operador de concatenación (para cadenas)
    ('OPERADOR_REPETICION', r'\*'),          # Operador de repetición (para cadenas y listas)
]
