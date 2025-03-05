from qr_generator import QRGenerator

def main():
    """Función principal del programa."""
    url = "https://youtu.be/R9Ss4JhULOM"  # URL a convertir en QR
    url2 = "https://www.youtube.com/watch?v=-MPvsxsH5c8&list=RDScNNfyq3d_w&index=3"
    url3 = "https://linkedin.com/in/juan-camilo-muñoz-tenorio"
    qr = QRGenerator(url2, output_folder=r"data", filename="QR_example3.png")
    saved_path = qr.generate_qr()
    print(f"✅ QR guardado en: {saved_path}")

if __name__ == "__main__":
    main()
