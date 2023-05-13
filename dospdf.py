from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import filedialog

# Función para seleccionar los archivos PDF
def select_files():
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(title="Seleccionar archivos PDF", filetypes=[("PDF Files", "*.pdf")])
    return files

# Obtener la lista de archivos PDF a combinar
pdf_files = select_files()

# Crear una instancia de PdfMerger
merger = PdfMerger()

# Agregar los archivos PDF al objeto PdfMerger
for pdf_file in pdf_files:
    merger.append(pdf_file)

# Solicitar al usuario el nombre del archivo resultante
output_file = input("Ingresa el nombre del archivo resultante (sin la extensión .pdf): ")

# Combinar los archivos PDF en uno solo
merger.write(f"{output_file}.pdf")
merger.close()

print(f"Los archivos PDF se han combinado en {output_file}.pdf correctamente.")

