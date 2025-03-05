import qrcode
from pathlib import Path
from utils import ensure_directory_exists  # Importamos función de utils

class QRGenerator:
    """Clase para generar códigos QR y guardarlos como imagen."""

    def __init__(self, data, output_folder="data", filename="qr_code.png"):
        """
        Inicializa la clase QRGenerator.

        :param data: Información a codificar en el QR (ej. una URL)
        :param output_folder: Carpeta donde se guardará el QR
        :param filename: Nombre del archivo de salida
        """
        self.data = data
        self.output_folder = Path(output_folder)
        self.filename = filename

        # Asegurar que la carpeta de salida existe (usando utils)
        ensure_directory_exists(self.output_folder)

    def generate_qr(self):
        """Genera el código QR y lo guarda como imagen."""
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Ruta completa donde se guardará la imagen
        file_path = self.output_folder / self.filename
        img.save(file_path)

        return file_path  # Retorna la ruta del archivo para su uso en main
