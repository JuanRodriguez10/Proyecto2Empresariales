import os
import sys

def setup_python_path():
    # Obtiene la ruta del directorio raíz del proyecto
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Añade el directorio raíz al Python path si no está ya
    if root_dir not in sys.path:
        sys.path.insert(0, root_dir)

    # Imprime el Python path para verificarlo
    print("Python path:", sys.path)

# Llama a la función para configurar el path
setup_python_path()
