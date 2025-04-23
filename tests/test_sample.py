def test_suma_basica():
    assert 2 + 2 == 4

def test_string():
    mensaje = "Hola Mundo"
    assert mensaje.lower() == "hola mundo"

# Prueba de igualdad de cadenas
def test_string_equality():
    """Verifica que dos cadenas sean iguales después de una conversión"""
    cadena_1 = "test"
    cadena_2 = "TEST"
    assert cadena_1.lower() == cadena_2.lower()

# Prueba de tipo de dato
def test_tipo_dato():
    """Verifica el tipo de datos de una variable"""
    numero = 10
    assert isinstance(numero, int)

# Prueba de lista
def test_lista():
    """Verifica que una lista contenga los elementos esperados"""
    lista = [1, 2, 3, 4, 5]
    assert 3 in lista  # Verifica que el número 3 esté en la lista
    assert len(lista) == 5  # Verifica que la longitud de la lista sea 5

# Prueba de error de división por cero
def test_division_por_cero():
    """Verifica que se produzca un error de división por cero"""
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        pass  # Esperamos el error de división por cero
    else:
        assert False, "Se esperaba una excepción ZeroDivisionError"

# Prueba de número negativo
def test_numero_negativo():
    """Verifica si un número es negativo"""
    numero = -5
    assert numero < 0  # Verifica que el número sea negativo

# Prueba de función de suma
def test_suma_funcion():
    """Verifica que una función de suma funcione correctamente"""
    def suma(a, b):
        return a + b
    
    resultado = suma(5, 3)
    assert resultado == 8  # Verifica que la suma sea correcta
