import os

def ensure_directory_exists(directory):
    """
    Asegura que el directorio exista, si no, lo crea.

    :param directory: Ruta del directorio a verificar o crear.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
