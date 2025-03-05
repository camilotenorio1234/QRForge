# QRForge 📷🔳

## 🌍 Introduction

QRForge is a simple yet efficient tool for generating QR codes from URLs or any other textual data. It utilizes the `qrcode` library in Python and allows saving QR codes as image files for easy sharing or printing.

This README is available in both English and Spanish. Below, you will find two sections: one in English and another in Spanish, each containing the same detailed information about installation, usage, and testing.

<details>
  <summary>QRForge 📷🔳 English</summary>

  # QRForge 📷🔳

Easily generate QR codes using Python.

## 📌 Description

QRForge is a tool that generates QR codes from URLs or textual data, allowing users to store and share information efficiently.

## 📁 Project Structure

```sh
QRForge/
├── data/                        # Folder to store generated QR codes
│   ├── QR_example2.png          # Example QR code image
├── src/
│   ├── qr_generator.py          # QR code generation logic
│   ├── main.py                  # Main script to run QR generation
│   ├── utils.py                 # Utility functions (e.g., directory creation)
│   ├── test_qr_generator.py     # Unit tests for QR generation
├── requirements.txt             # Dependencies for the project
├── README.md                    # Project documentation
├── .gitignore                   # Files and folders to ignore in the repository
```

# 🚀 Installation and Usage

## 📌 1. Clone the repository

```sh
git clone [https://github.com/camilotenorio1234/QRForge.git](https://github.com/camilotenorio1234/QRForge)
cd QRForge
```

## 📌 2. Install dependencies

Ensure you have **Python 3** installed. Then, install the required dependencies:

```sh
pip install -r requirements.txt
```

## 📌 3. Generate a QR code

Run the main script to create a QR code:

```sh
python src/main.py
```

A QR code image will be generated and saved in the `data/` folder.

## ✅ Unit Test Results

This project includes automated tests executed with pytest.
To run the tests:

```sh
pytest src/test_qr_generator.py
```

If you want more details:

```sh
pytest -v
```

Below are the results:

```sh
=============================================================== test session starts ================================================================ 
platform win32 -- Python 3.9.19, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\JuanC\OneDrive\Escritorio\codigos python\codigo en desarrollo\QRForge
plugins: anyio-4.3.0, dash-2.16.1
collected 3 items                                                                                                                                    

src\test_qr_generator.py ...                                                                                                                  [100%] 

================================================================ 3 passed in 0.12s =================================================================
```
```sh
=============================================================== test session starts ================================================================
platform win32 -- Python 3.9.19, pytest-8.3.4, pluggy-1.5.0 -- C:\Users\JuanC\anaconda3\envs\env_tesis_3_9\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\JuanC\OneDrive\Escritorio\codigos python\codigo en desarrollo\QRForge
plugins: anyio-4.3.0, dash-2.16.1
collected 3 items

src/test_qr_generator.py::TestQRGenerator::test_ensure_directory_exists PASSED                                                                [ 33%] 
src/test_qr_generator.py::TestQRGenerator::test_generate_qr_creates_file PASSED                                                               [ 66%]
src/test_qr_generator.py::TestQRGenerator::test_generate_qr_returns_correct_path PASSED                                                       [100%] 

================================================================ 3 passed in 0.11s =================================================================
```

</details>

---
## 🌍 Introducción

QRForge es una herramienta sencilla pero eficiente para generar códigos QR a partir de URLs o cualquier otro dato en texto. Utiliza la biblioteca `qrcode` en Python y permite guardar códigos QR como archivos de imagen para facilitar su uso o impresión.

Este README está disponible en inglés y español. A continuación, encontrarás dos secciones: una en inglés y otra en español, cada una con la misma información detallada sobre instalación, uso y pruebas.

<details>
  <summary>QRForge 📷🔳 Español</summary>

# QRForge 📷🔳

Genera códigos QR fácilmente con Python.

## 📌 Descripción

QRForge es una herramienta que genera códigos QR a partir de URLs o datos textuales, permitiendo almacenar y compartir información de manera eficiente.

## 📁 Estructura del Proyecto

```sh
QRForge/
├── data/                        # Carpeta para almacenar códigos QR generados
│   ├── QR_example2.png          # Imagen de código QR de ejemplo
├── src/
│   ├── qr_generator.py          # Lógica de generación de códigos QR
│   ├── main.py                  # Script principal para ejecutar la generación
│   ├── utils.py                 # Funciones auxiliares (ej. creación de carpetas)
│   ├── test_qr_generator.py     # Pruebas unitarias para la generación de QR
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Documentación del proyecto
├── .gitignore                   # Archivos y carpetas a ignorar en el repositorio
```

# 🚀 Instalación y Uso

## 📌 1. Clonar el repositorio

```sh
git clone [https://github.com/camilotenorio1234/QRForge.git](https://github.com/camilotenorio1234/QRForge)
cd QRForge
```

## 📌 2. Instalar dependencias

Asegúrate de tener **Python 3** instalado. Luego, instala las dependencias necesarias con:

```sh
pip install -r requirements.txt
```

## 📌 3. Generar un código QR

Ejecuta el script principal para crear un código QR:

```sh
python src/main.py
```

Se generará una imagen con el código QR y se guardará en la carpeta `data/`.

## ✅ Resultados de Pruebas Unitarias

Este proyecto cuenta con pruebas automatizadas ejecutadas con pytest.
Para ejecutar las pruebas:

```sh
pytest src/test_qr_generator.py
```

Si quieres ver más detalles:

```sh
pytest -v
```
A continuación, los resultados:

```sh
=============================================================== test session starts ================================================================ 
platform win32 -- Python 3.9.19, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\JuanC\OneDrive\Escritorio\codigos python\codigo en desarrollo\QRForge
plugins: anyio-4.3.0, dash-2.16.1
collected 3 items                                                                                                                                    

src\test_qr_generator.py ...                                                                                                                  [100%] 

================================================================ 3 passed in 0.12s =================================================================
```
```sh
=============================================================== test session starts ================================================================
platform win32 -- Python 3.9.19, pytest-8.3.4, pluggy-1.5.0 -- C:\Users\JuanC\anaconda3\envs\env_tesis_3_9\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\JuanC\OneDrive\Escritorio\codigos python\codigo en desarrollo\QRForge
plugins: anyio-4.3.0, dash-2.16.1
collected 3 items

src/test_qr_generator.py::TestQRGenerator::test_ensure_directory_exists PASSED                                                                [ 33%] 
src/test_qr_generator.py::TestQRGenerator::test_generate_qr_creates_file PASSED                                                               [ 66%]
src/test_qr_generator.py::TestQRGenerator::test_generate_qr_returns_correct_path PASSED                                                       [100%] 

================================================================ 3 passed in 0.11s =================================================================
```

</details>
