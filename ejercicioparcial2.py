"""2. Un colegio privado desea registrar la asistencia de sus estudiantes a las
clases cada docente tiene su listado de los estudiantes en los cuáles se
les ha solicitado colocar a la par de cada estudiante si ha asistido, si
cuenta con permiso o tiene inasistencia con la fecha respectiva.
Actualmente esto se maneja por unas hojas de papel impreso y se
entregan al director al final del día; la escuela necesita agilizar este
proceso.
 Si el estudiante tiene un permiso el director necesita la razón de
dicha falta, ¿Cómo solventarías esta situación? Agrega tu
propuesta al código."""

import tkinter as tk
from tkinter import messagebox
import sqlite3

# Crear la base de datos y la tabla si no existen
conn = sqlite3.connect('asistencia.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS asistencia (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                fecha TEXT,
                estado TEXT,
                razon TEXT)''')
conn.commit()

# Función para registrar la asistencia
def registrar_asistencia():
    nombre = entry_nombre.get()
    fecha = entry_fecha.get()
    estado = var_estado.get()
    razon = entry_razon.get() if estado == 'Permiso' else ''
    
    if nombre and fecha and estado:
        c.execute("INSERT INTO asistencia (nombre, fecha, estado, razon) VALUES (?, ?, ?, ?)",
                  (nombre, fecha, estado, razon))
        conn.commit()
        messagebox.showinfo("Registro", "Asistencia registrada correctamente")
        entry_nombre.delete(0, tk.END)
        entry_fecha.delete(0, tk.END)
        entry_razon.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Registro de Asistencia")

tk.Label(root, text="Nombre del Estudiante").grid(row=0, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

tk.Label(root, text="Fecha (YYYY-MM-DD)").grid(row=1, column=0)
entry_fecha = tk.Entry(root)
entry_fecha.grid(row=1, column=1)

tk.Label(root, text="Estado").grid(row=2, column=0)
var_estado = tk.StringVar(value="Asistió")
tk.Radiobutton(root, text="Asistió", variable=var_estado, value="Asistió").grid(row=2, column=1)
tk.Radiobutton(root, text="Permiso", variable=var_estado, value="Permiso").grid(row=2, column=2)
tk.Radiobutton(root, text="Inasistencia", variable=var_estado, value="Inasistencia").grid(row=2, column=3)

tk.Label(root, text="Razón (si aplica)").grid(row=3, column=0)
entry_razon = tk.Entry(root)
entry_razon.grid(row=3, column=1)

tk.Button(root, text="Registrar", command=registrar_asistencia).grid(row=4, column=1)

root.mainloop()

# Cerrar la conexión a la base de datos al finalizar
conn.close()
