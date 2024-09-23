from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
import os
import shutil

# Función para seleccionar los archivos PDF
def seleccionar_archivos():
    ventana = tk.Tk()
    ventana.withdraw()
    archivos = filedialog.askopenfilenames(title="Seleccionar Archivos PDF", filetypes=[("PDF Archivos", "*.pdf")])
    return archivos

# Obtener la lista de archivos PDF a combinar
archivos_pdf = seleccionar_archivos()

# Crear una instancia de PdfMerger
merger = PdfMerger()

# Agregar los archivos PDF al objeto PdfMerger
for archivo_pdf in archivos_pdf:
    merger.append(archivo_pdf)

# Obtenemos el nombre del usario para ponerlo en el directorio Documentos
username = os.getenv('USER')
documentos_dir = f"/home/{username}/Documentos"

try:
    command = ["zenity", "--entry", "--title", "Juntar Varios PDF en Uno", "--text", "Ingresa un nombre para el archivo resultante (sin la extensión .pdf)"]
    archivo_saliente = subprocess.check_output(command).decode("utf-8").strip()

    # Combinar los archivos PDF en uno solo
    merger.write(f"{archivo_saliente}.pdf")
    merger.close()

    # Mensaje de la conbiancion creada.
    messagebox.showinfo("Juntar Varios PDF en Uno", f"El nuevo nombre del PDF es:\n{archivo_saliente}.pdf \nY esta ubicado en:\n{documentos_dir}")

    # Despues de crear el nuevo pdf lo mueve al directorio Documentos
    shutil.move(f"{archivo_saliente}.pdf", os.path.join(documentos_dir, f"{archivo_saliente}.pdf"))

except subprocess.CalledProcessError as e:
    if e.returncode == 1:
        # El usuario hizo clic en "Cancelar" en el cuadro de diálogo de Zenity
        messagebox.showinfo("Combinación de archivos PDF", "Operación cancelada por el usuario")
    else:
        # Otro error de subprocess, muestra el mensaje de error
        messagebox.showerror("Error", str(e))

##Creado por Jenrry Soto Dextre, correo dextre1481@gmail.com , jsd@dextre.xyz
##este script en python te aseguro qeu corre en fedora Gnu/Linux

