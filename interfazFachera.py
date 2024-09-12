import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Interfaz con procesamiento de imagen")
        
        self.imagen_np = None
        self.imagen_procesada = None
        
        self.lienzo = tk.Canvas(ventana, width=400, height=200)
        self.lienzo.pack()

        # Crear dos cuadros en el lienzo para mostrar las imágenes
        self.lienzo.create_rectangle(50, 50, 150, 150, fill="blue")  # Cuadro para la imagen original
        self.lienzo.create_rectangle(200, 50, 300, 150, fill="red")  # Cuadro para la imagen procesada

        # Botones para cargar, procesar y guardar la imagen
        boton_cargar = tk.Button(ventana, text="Cargar Imagen", command=self.cargar_imagen)
        boton_cargar.pack(side="left", padx=10, pady=10)

        boton_procesar = tk.Button(ventana, text="Procesar Imagen", command=self.procesar)
        boton_procesar.pack(side="left", padx=10, pady=10)

        boton_guardar = tk.Button(ventana, text="Guardar Imagen", command=self.guardar_imagen)
        boton_guardar.pack(side="left", padx=10, pady=10)

    def cargar_imagen(self):
        ruta_imagen = filedialog.askopenfilename(title="Seleccionar imagen", filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg")])
        if ruta_imagen:
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((100, 100))  # Ajustar tamaño de la imagen
            imagen_tk = ImageTk.PhotoImage(imagen)
            self.lienzo.create_image(100, 100, image=imagen_tk, anchor="center")
            self.lienzo.image = imagen_tk  # Guardar referencia a la imagen para evitar que sea eliminada por el garbage collector
            self.imagen_np = np.array(imagen)  # Convertir a array numpy y guardar localmente
        else:
            self.imagen_np = None

    def procesar(self):
        if self.imagen_np is not None:
            # Normalizar y recortar los valores de la imagen
            im = np.clip(self.imagen_np / 255.0, 0.0, 1.0)
            
            # Convertir la imagen procesada de vuelta a PIL para mostrarla
            self.imagen_procesada = Image.fromarray((im[:, :, 0] * 255).astype(np.uint8))
            imagen_procesada_tk = ImageTk.PhotoImage(self.imagen_procesada)
            
            # Mostrar la imagen procesada en el segundo cuadro
            self.lienzo.create_image(250, 100, image=imagen_procesada_tk, anchor="center")
            self.lienzo.imagen_procesada_tk = imagen_procesada_tk  # Guardar referencia para evitar que se elimine por el garbage collector
        else:
            print("No se proporcionó ninguna imagen para procesar")

    def guardar_imagen(self):
        if self.imagen_procesada is not None:
            # Guardar la imagen procesada usando el cuadro de diálogo
            ruta_guardar = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Archivo PNG", "*.png"), ("Todos los archivos", "*.*")])
            if ruta_guardar:
                # Guardar la imagen procesada en el archivo seleccionado
                self.imagen_procesada.save(ruta_guardar)
            print("Foto Guardada con exito")
        else:
            print("No hay imagen procesada para guardar")

# Configuración básica de la ventana
ventana = tk.Tk()
app = Aplicacion(ventana)

ventana.mainloop()
