from PIL import Image, ImageTk, ImageFilter, ImageEnhance
import tkinter as tk
from tkinter import filedialog, messagebox
import os

#Variables globales
img = None
img_display = None
filepath = None
#Funcion para abrir la imagen 
def open_image():
    global img, img_display, filepath
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jepg;*.bmp;*.gif ")])
    if filepath:
        img = Image.open(filepath)
        img_display = img.copy()
        update_image_display()

# Funcion para actualizar la imagen  en la interfaz
def update_image_display():
    global img_display
    tk_img = ImageTk.PhotoImage(img_display)
    img_label.config(image=tk_img)
    img_label.image = tk_img


#Funcion para guardar la imagen modificada
def save_image():
    global img_display, filepath
    if img_display: 
        save_filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files",  "*.png"),( "LPEG files", ".jpg"),("ALL files", "*.*")])
        if save_filepath:
            img_display.save(save_filepath)
            messagebox.showinfo("Guardado",  f"Imagen guardada en{save_filepath}")
    else:
        messagebox.showwarning("Advertencia" "No hay imagen  para guardar")


#Funcion para rotar imagen
def rota_image():
    global img_display
    if img_display:
        img_display = img_display.rotate(90, expand=True)

#Funcion para redimensionar la imagen
def resize_image():
     global img_display
     if img_display:
         new_widht = int(widht_entry.get())
         new_widht = int(height_entry.get())
         img_display = img_display.resize((new_widht, new_widht))
         update_image_display()


#Funcion para recortar la imagen
def crop_image():
    global img_display
    if img_display
    crop_box = (100, 100, 400, 400)
    img_display = img_display.crop(crop_box)
    update_image_display

#funcion para ajustar el brillo mde la imagwn    
def adjust_brightness():
    global img_display
    if img_display:
        enhancer = ImageEnhance.Brightness(img_display)
        brightness_factor = float (brightness_scale.get())
        img_display = enhancer.enhance(brightness_factor)
        update_image_display


#Funcion para convertir la imagen a escala de grises
def convert_to_grayescale():
    global img_display
    if img_display:
        img_display = img_display.convert("L")  
        update_image_display()


#        





  





