from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
import os
import shutil

# Función para seleccionar los archivos PDF
def select_files():
    root = tk.Tk()
    root.title("Juntar Varios PDF en Uno")
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

# Obtenemos el nombre del usario para ponerlo en el directorio Documentos
username = os.getenv('USER')
documentos_dir = f"/home/{username}/Documentos"

try:
    command = ["zenity", "--entry", "--title", "Juntar Varios PDF en Uno", "--text", "Ingresa un nombre para el archivo resultante (sin la extensión .pdf)"]
    output_file = subprocess.check_output(command).decode("utf-8").strip()

    # Combinar los archivos PDF en uno solo
    merger.write(f"{output_file}.pdf")
    merger.close()

    # Mensaje de la conbiancion creada.
    messagebox.showinfo("Juntar Varios PDF en Uno", f"El nuevo nombre del PDF es:\n{output_file}.pdf \nY esta ubicado en:\n{documentos_dir}")

    # Despues de crear el nuevo pdf lo mueve al directorio Documentos
    shutil.move(f"{output_file}.pdf", os.path.join(documentos_dir, f"{output_file}.pdf"))


except subprocess.CalledProcessError as e:
    if e.returncode == 1:
        # El usuario hizo clic en "Cancelar" en el cuadro de diálogo de Zenity
        messagebox.showinfo("Combinación de archivos PDF", "Operación cancelada por el usuario")
    else:
        # Otro error de subprocess, muestra el mensaje de error
        messagebox.showerror("Error", str(e))

##Creado por Jenrry Soto Dextre, correo dextre1481@gmail.com , jsd@dextre.xyz
##este script en python te aseguro qeu corre en fedora Gnu/Linux
