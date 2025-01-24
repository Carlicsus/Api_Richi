'''Código principal para realizar mi primera API usando FastAPI'''

from fastapi import FastAPI

# Crear la aplicación de FastAPI
app = FastAPI()

@app.get('/')
async def root():
    """
    Ruta raíz. 
    """
    return {'Saludo': 'Hola amigos del yutu'}

@app.get('/suma')
async def suma_numerica():
    """
    Ruta de suma de dos números.

    Returns:
        dict: Resultado de la suma.
    """
    valor_uno = 1
    valor_dos = 3
    resultado = valor_uno + valor_dos
    return {'Valor de la suma': resultado}