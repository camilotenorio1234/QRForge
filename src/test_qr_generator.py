import unittest
from pathlib import Path
from qr_generator import QRGenerator
from utils import ensure_directory_exists

class TestQRGenerator(unittest.TestCase):

    def setUp(self):
        """Configura una instancia de QRGenerator para las pruebas."""
        self.test_output_folder = Path("codigo en desarrollo/PyQRGen/data")
        self.test_filename = "test_qr.png"
        self.qr = QRGenerator("https://test.com", output_folder=self.test_output_folder, filename=self.test_filename)

    def test_generate_qr_creates_file(self):
        """Prueba que el código QR se genera y se guarda correctamente."""
        file_path = self.qr.generate_qr()
        self.assertTrue(file_path.exists())  # Verifica que el archivo se creó

    def test_generate_qr_returns_correct_path(self):
        """Prueba que la ruta retornada es la esperada."""
        expected_path = self.test_output_folder / self.test_filename
        actual_path = self.qr.generate_qr()
        self.assertEqual(actual_path, expected_path)

    def test_ensure_directory_exists(self):
        """Prueba que la función ensure_directory_exists crea la carpeta si no existe."""
        test_folder = Path("codigo en desarrollo/PyQRGen/test_data")
        ensure_directory_exists(test_folder)
        self.assertTrue(test_folder.exists())

if __name__ == "__main__":
    unittest.main()
