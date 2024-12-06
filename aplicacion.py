import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pymysql

def conexionBD():
    return pymysql.connect(
        host='localhost',
        user='root',
        passwd='1234',  # Contraseña
        database='matriculas'  # Nombre de la BD
    )


def main():

    # Menú Principal
    root = tk.Tk()
    root.title("Gestión de Consultas SQL")
    root.geometry("800x600")
    root.configure(bg="#e6f7ff")  


    # Titulo y Diseño
    style = ttk.Style()
    style.theme_use("clam")

    titulo = tk.Label(
        root,
        text="Sistema de Consultas SQL",
        font=("Arial", 24, "bold"),
        fg="#2b3d4f",  
        bg="#e6f7ff",  
        pady=20  
    )
    titulo.pack()


    # Opciones y Diseño
    botones = [
        ("Gestionar Tablas", ventana_tablas),
        ("Abrir Consultas SQL", ventana_consultas),
        ("Salir", root.quit)
    ]

    style.configure("TButton",
                    font=("Arial", 16, "bold"),
                    padding=10,
                    relief="flat",
                    background="#d1ecf1",
                    foreground="#2b3d4f",
                    focuscolor="none")

    style.map("TButton",
              background=[('active', '#add8e6'), ('!active', '#d1ecf1')])

    for i, (texto, comando) in enumerate(botones):
        boton = ttk.Button(
            root,
            text=texto,
            style="TButton",
            command=comando
        )
        boton.pack(pady=10, ipadx=20, ipady=10)

    root.mainloop()

# Función para obtener los datos de la tabla
def obtener_datos(tabla):
    try:
        conexion = conexionBD()
        cursor = conexion.cursor()

        # Consulta para obtener los datos de cada tabla
        consulta = f"SELECT * FROM {tabla}"

        cursor.execute(consulta)

        # Resultados y Nombres de columnas
        resultados = cursor.fetchall()
        columnas = [col[0] for col in cursor.description]

        #Vista para la tabla
        treeview.delete(*treeview.get_children())
        treeview["columns"] = columnas
        for col in columnas:
            treeview.heading(col, text=col, anchor=tk.W)
            treeview.column(col, anchor=tk.W, width=150)

        for fila in resultados:
            treeview.insert("", tk.END, values=fila)

    finally:
        conexion.close()

# Función para las consultas
def obtener_consulta(consulta_sql):
    try:
        conexion = conexionBD()
        cursor = conexion.cursor()

        cursor.execute(consulta_sql)

        # Resultados y Nombres de columnas
        resultados = cursor.fetchall()
        columnas = [col[0] for col in cursor.description]

        #Vista para la tabla
        treeview.delete(*treeview.get_children())
        treeview["columns"] = columnas
        for col in columnas:
            treeview.heading(col, text=col, anchor=tk.W)
            treeview.column(col, anchor=tk.W, width=150)

        for fila in resultados:
            treeview.insert("", tk.END, values=fila)

    finally:
        conexion.close()

# Función para obtener las calificaciones de un estudiante en un curso específico
def obtener_calificaciones_estudiante_curso(estudiante_id, curso_id):
    try:
        conexion = conexionBD()
        cursor = conexion.cursor()

        consulta = """
        SELECT E.Nombre AS Nombre_Estudiante, C.Nombre_Curso, Cal.Nota
        FROM Calificaciones Cal
        JOIN Estudiante E ON Cal.Estudiante_ID = E.Estudiante_ID
        JOIN Cursos C ON Cal.Curso_ID = C.Curso_ID
        WHERE E.Estudiante_ID = %s
        AND C.Curso_ID = %s;
        """
        cursor.execute(consulta, (estudiante_id, curso_id))

        # Resultados y Nombres de columnas
        resultados = cursor.fetchall()
        columnas = [col[0] for col in cursor.description]

        #Vista para la tabla
        treeview.delete(*treeview.get_children())
        treeview["columns"] = columnas
        for col in columnas:
            treeview.heading(col, text=col, anchor=tk.W)
            treeview.column(col, anchor=tk.W, width=150)

        for fila in resultados:
            treeview.insert("", tk.END, values=fila)

    finally:
        conexion.close()

# Función para crear la ventana donde ingresar el ID del Estudiante y el ID del Curso
def ventana_calificaciones():
    ventana = tk.Toplevel()
    ventana.title("Consulta de Calificaciones")
    ventana.geometry("400x300")

    # Diseño de la Ventana junto al texto
    label = tk.Label(ventana, text="Introduce el ID del Estudiante y el ID del Curso:", font=("Arial", 12))
    label.pack(pady=10)

    label_estudiante = tk.Label(ventana, text="ID Estudiante:", font=("Arial", 12))
    label_estudiante.pack(pady=5)
    entry_estudiante = tk.Entry(ventana, font=("Arial", 12))
    entry_estudiante.pack(pady=5)

    label_curso = tk.Label(ventana, text="ID Curso:", font=("Arial", 12))
    label_curso.pack(pady=5)
    entry_curso = tk.Entry(ventana, font=("Arial", 12))
    entry_curso.pack(pady=5)
 
    def ejecutar_consulta():
        estudiante_id = entry_estudiante.get()
        curso_id = entry_curso.get()
        
        if estudiante_id and curso_id:
            try:
                estudiante_id = int(estudiante_id)
                curso_id = int(curso_id)
                obtener_calificaciones_estudiante_curso(estudiante_id, curso_id)
                ventana.destroy() 
            except ValueError:
                messagebox.showerror("Error", "Los IDs deben ser números válidos.")
        else:
            messagebox.showerror("Error", "Por favor, ingresa ambos IDs.")

    boton_ejecutar = tk.Button(ventana, text="Ver Calificaciones", font=("Arial", 12), command=ejecutar_consulta)
    boton_ejecutar.pack(pady=20)


def obtener_matricula_estudiante(estudiante_id):
    try:
        conexion = conexionBD()
        cursor = conexion.cursor()

        # Consulta SQL con parámetros
        consulta = """
        SELECT M.Inscripcion_ID, C.Nombre_Curso, M.Fecha_Inscripcion, M.Estado
        FROM Matricula M
        JOIN Cursos C ON M.Curso_ID = C.Curso_ID
        WHERE M.Estudiante_ID = %s;
        """
        cursor.execute(consulta, (estudiante_id,))

        # Resultados y Nombres de columnas
        resultados = cursor.fetchall()
        columnas = [col[0] for col in cursor.description]

        # Vista para la tabla
        treeview.delete(*treeview.get_children())
        treeview["columns"] = columnas
        for col in columnas:
            treeview.heading(col, text=col, anchor=tk.W)
            treeview.column(col, anchor=tk.W, width=150)

        for fila in resultados:
            treeview.insert("", tk.END, values=fila)

    finally:
        conexion.close()

# Función para crear la ventana para ingresar el ID del Estudiante
def ventana_matricula_estudiante():
    ventana = tk.Toplevel()
    ventana.title("Consulta de Matrícula de Estudiante")
    ventana.geometry("400x300")

    # Diseño de la Ventana junto al texto
    label = tk.Label(ventana, text="Introduce el ID del Estudiante:", font=("Arial", 12))
    label.pack(pady=10)

    label_estudiante = tk.Label(ventana, text="ID Estudiante:", font=("Arial", 12))
    label_estudiante.pack(pady=5)
    entry_estudiante = tk.Entry(ventana, font=("Arial", 12))
    entry_estudiante.pack(pady=5)

    def ejecutar_consulta():
        estudiante_id = entry_estudiante.get()

        if estudiante_id:
            try:
                estudiante_id = int(estudiante_id)
                obtener_matricula_estudiante(estudiante_id)
                ventana.destroy()  # Cerrar la ventana una vez ejecutada la consulta
            except ValueError:
                messagebox.showerror("Error", "El ID debe ser un número válido.")
        else:
            messagebox.showerror("Error", "Por favor, ingresa el ID del estudiante.")

    boton_ejecutar = tk.Button(ventana, text="Ver Matrícula", font=("Arial", 12), command=ejecutar_consulta)
    boton_ejecutar.pack(pady=20)

def obtener_cursos_profesor(profesor_id):
    try:
        conexion = conexionBD()
        cursor = conexion.cursor()

        # Consulta SQL con parámetros
        consulta = """
        SELECT C.Curso_ID, C.Nombre_Curso
        FROM Profesor_Curso PC
        JOIN Cursos C ON PC.Curso_ID = C.Curso_ID
        WHERE PC.Profesor_ID = %s;
        """
        cursor.execute(consulta, (profesor_id,))

        # Resultados y Nombres de columnas
        resultados = cursor.fetchall()
        columnas = [col[0] for col in cursor.description]

        # Vista pra las tablas
        treeview.delete(*treeview.get_children())
        treeview["columns"] = columnas
        for col in columnas:
            treeview.heading(col, text=col, anchor=tk.W)
            treeview.column(col, anchor=tk.W, width=150)

        for fila in resultados:
            treeview.insert("", tk.END, values=fila)

    finally:
        conexion.close()

# Función para crear la ventana para ingresar el ID del Profesor
def ventana_cursos_profesor():
    ventana = tk.Toplevel()
    ventana.title("Consulta de Cursos por Profesor")
    ventana.geometry("400x300")

    # Diseño de la Ventana junto al texto
    label = tk.Label(ventana, text="Introduce el ID del Profesor:", font=("Arial", 12))
    label.pack(pady=10)

    label_profesor = tk.Label(ventana, text="ID Profesor:", font=("Arial", 12))
    label_profesor.pack(pady=5)
    entry_profesor = tk.Entry(ventana, font=("Arial", 12))
    entry_profesor.pack(pady=5)

    def ejecutar_consulta():
        profesor_id = entry_profesor.get()

        if profesor_id:
            try:
                profesor_id = int(profesor_id)
                obtener_cursos_profesor(profesor_id)
                ventana.destroy()  
            except ValueError:
                messagebox.showerror("Error", "El ID debe ser un número válido.")
        else:
            messagebox.showerror("Error", "Por favor, ingresa el ID del Profesor.")

    boton_ejecutar = tk.Button(ventana, text="Ver Cursos", font=("Arial", 12), command=ejecutar_consulta)
    boton_ejecutar.pack(pady=20)


# Función para crear una ventana para las consultas
def ventana_consultas():
    ventana = tk.Toplevel()
    ventana.title("Consultas SQL")
    ventana.geometry("800x600")
    ventana.configure(bg="#f0f8ff") 

    titulo = tk.Label(
        ventana,
        text="Selecciona una consulta para ver los resultados:",
        font=("Arial", 20, "bold"),
        fg="#2b3d4f", 
        bg="#f0f8ff", 
        pady=20
    )
    titulo.pack()

    # Letras y Diseño
    frame_botones = tk.Frame(ventana, bg="#f0f8ff")
    frame_botones.pack(fill="both", expand=True, padx=20, pady=10)

    canvas = tk.Canvas(frame_botones)
    scrollbar = tk.Scrollbar(frame_botones, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    frame_botones_scrollable = tk.Frame(canvas, bg="#f0f8ff")

    # Consultas SQL
    consultas = [
        ("1. Estudiantes Inscritos en Cada Curso", """
        SELECT C.Nombre_Curso, E.Nombre AS Nombre_Estudiante, E.Telefono, E.Email
        FROM Cursos C
        JOIN Matricula M ON C.Curso_ID = M.Curso_ID
        JOIN Estudiante E ON M.Estudiante_ID = E.Estudiante_ID
        ORDER BY C.Nombre_Curso, E.Nombre;
        """),
        ("2. Horario de Clases de Estudiantes Inscritos con Requisitos", """
        SELECT E.Nombre AS Nombre_Estudiante, C.Nombre_Curso, H.Dia, H.Hora_Inicio, H.Hora_Fin, S.Numero_Sala
        FROM Estudiante E
        JOIN Matricula M ON E.Estudiante_ID = M.Estudiante_ID
        JOIN Cursos C ON M.Curso_ID = C.Curso_ID
        JOIN Horarios H ON C.Curso_ID = H.Curso_ID
        JOIN Salas S ON H.Sala_ID = S.Sala_ID
        WHERE C.Requisitos = TRUE
        ORDER BY E.Nombre, H.Dia, H.Hora_Inicio;
        """),
        ("3. Promedio de Calificaciones por Curso", """
        SELECT C.Nombre_Curso, ROUND(AVG(CA.Nota), 1) AS Promedio_Calificacion
        FROM Cursos C
        JOIN Calificaciones CA ON C.Curso_ID = CA.Curso_ID
        GROUP BY C.Nombre_Curso
        ORDER BY Promedio_Calificacion DESC;
        """),
        ("4. Cursos con Mayor Cantidad de Estudiantes", """
        SELECT C.Nombre_Curso, COUNT(M.Estudiante_ID) AS Total_Estudientes
        FROM Cursos C
        JOIN Matricula M ON C.Curso_ID = M.Curso_ID
        GROUP BY C.Nombre_Curso
        HAVING COUNT(M.Estudiante_ID) = (SELECT MAX(Total)
                                         FROM ( SELECT COUNT(M2.Estudiante_ID) AS Total
                                                FROM Cursos C2 
                                                JOIN Matricula M2 ON C2.Curso_ID = M2.Curso_ID
                                                GROUP BY C2.Nombre_Curso) 
                                                AS Subquery
                                        );
        """),
        ("5. Calificaciones de un Estudiante y Curso especifico", lambda: ventana_calificaciones()),
        ("6. Estudiantes que tengan nota inferior a 4.0", """ 
        SELECT E.Estudiante_ID, E.Nombre, Cal.Nota
        FROM Calificaciones Cal
        JOIN Estudiante E ON Cal.Estudiante_ID = E.Estudiante_ID
        WHERE Cal.Nota < 4.0;      
        """),
        ("7. Información de Matrícula de un Estudiante", lambda: ventana_matricula_estudiante()),
        ("8. Cursos Inscritos por Profesor", lambda: ventana_cursos_profesor()),
        ("9. Estudiantes que han pagado la Matricula", """ 
        SELECT E.Estudiante_ID, E.Nombre
        FROM Matricula M
        JOIN Estudiante E ON M.Estudiante_ID = E.Estudiante_ID
        WHERE M.Estado != 'Pagado';        
        """),
        ("10. Salas disponibles para un curso", """ 
        SELECT S.Sala_ID, S.Numero_Sala, S.Capacidad
        FROM Salas S
        WHERE NOT EXISTS (
            SELECT 1 FROM Horarios H
            WHERE H.Curso_ID = 4 AND H.Sala_ID = S.Sala_ID
        );
        """),
        ("11. Promedio de Calificaciones por Facultad", """ 
        SELECT F.Nombre AS Facultad, ROUND (AVG(CA.Nota),1) AS Promedio_Calificacion, COUNT(DISTINCT C.Curso_ID) AS Total_Cursos
        FROM Facultad F
        JOIN Cursos C ON F.Facultad_ID = C.Facultad_ID
        JOIN Calificaciones CA ON C.Curso_ID = CA.Curso_ID
        GROUP BY F.Nombre
        HAVING COUNT(DISTINCT C.Curso_ID) > 0;
        """),
        ("12. Número de Cursos Ofrecidos por Semestre", """ 
        SELECT COUNT(*) AS Numero_Cursos
        FROM Cursos;
        """),
        ("13. Información de Contacto de Profesores", """ 
        SELECT Nombre_Profesor, Telefono_Profesor, Email_Profesor
        FROM Profesores;
        """),
        ("14. Ranking de estudiantes con mejor rendimiento", """ 
        SELECT F.Nombre AS Facultad, Cr.Nombre_Curso AS Curso, E.Estudiante_ID AS ID_Estudiante, E.Nombre AS Estudiante, ROUND(AVG(Cal.Nota), 1) AS Promedio
        FROM Calificaciones Cal
        JOIN Estudiante E ON Cal.Estudiante_ID = E.Estudiante_ID
        JOIN Cursos Cr ON Cal.Curso_ID = Cr.Curso_ID
        JOIN Facultad F ON Cr.Facultad_ID = F.Facultad_ID
        GROUP BY F.Nombre, Cr.Nombre_Curso, E.Estudiante_ID
        ORDER BY Promedio DESC, Cr.Nombre_Curso ASC
        LIMIT 10;
        """),
        ("15. Distribución de Calificaciones por Curso", """ 
        SELECT C.Nombre_Curso,
        CASE 
            WHEN CA.Nota >= 6.0 THEN '6.0 - 7.0'
            WHEN CA.Nota >= 5.0 THEN '5.0 - 5.9'
            WHEN CA.Nota >= 4.0 THEN '4.0 - 4.9'
            ELSE 'Menos de 4.0'
            END AS Rango_Calificacion, COUNT(CA.Estudiante_ID) AS Total_Estudientes
        FROM Cursos C
        JOIN Calificaciones CA ON C.Curso_ID = CA.Curso_ID
        GROUP BY C.Nombre_Curso, Rango_Calificacion
        ORDER BY C.Nombre_Curso, Rango_Calificacion;
        """)
    ]

    # Creacion de botones 
    for i, (nombre, consulta) in enumerate(consultas):
        button = tk.Button(frame_botones_scrollable, text=nombre, font=("Arial", 12), bg="#b3d9ff", fg="#2b3d4f", 
                           relief="raised", bd=2, anchor="center", wraplength=700, # Ajuste automático y texto centrado
                           command=lambda c=consulta: obtener_consulta(c) if isinstance(c, str) else c())
        button.grid(row=i, column=0, padx=20, pady=5, sticky="ew")  # 'ew' para que se expanda de izquierda a derecha

    # Configurar para la barra lateral (subir y bajar)
    canvas.create_window((0, 0), window=frame_botones_scrollable, anchor="nw")
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    frame_botones_scrollable.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Vista y Diseño para la Tabla
    global treeview
    treeview = ttk.Treeview(ventana, show="headings", style="Custom.Treeview")
    treeview.pack(fill="both", expand=True, padx=20, pady=20)

    estilo = ttk.Style()
    estilo.configure("Custom.Treeview",
                     background="#e6f7ff", 
                     foreground="#2b3d4f", 
                     fieldbackground="#f0f8ff", 
                     font=("Arial", 12))
    
    estilo.configure("Custom.Treeview.Heading",
                    font=("Arial", 12, "bold"),
                    background="#2b3d4f",  
                    foreground="white")  

    scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=treeview.yview)
    treeview.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")


# Función para crear la ventana de las tablas
def ventana_tablas():
    ventana = tk.Toplevel()
    ventana.title("Ver Datos de Tablas")
    ventana.geometry("800x600")
    ventana.configure(bg="#f0f8ff")

    # Titulo y Diseño
    titulo = tk.Label(
        ventana,
        text="Selecciona una tabla para ver sus datos:",
        font=("Arial", 20, "bold"),
        fg="#2b3d4f",  # Color del texto
        bg="#f0f8ff",  # Fondo de la ventana
        pady=20
    )
    titulo.pack()

    frame_botones = tk.Frame(ventana, bg="#f0f8ff")
    frame_botones.pack(fill="both", expand=True, padx=20, pady=10)

    canvas = tk.Canvas(frame_botones)
    scrollbar = tk.Scrollbar(frame_botones, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    frame_botones_scrollable = tk.Frame(canvas, bg="#f0f8ff")

    # Agregar botones 
    tablas = ["Estudiante", "Facultad", "Cursos", "Profesores", "Horarios", "Calificaciones", "Salas", "Matricula"]
    for tabla in tablas:
        button = tk.Button(frame_botones_scrollable, text=tabla, font=("Arial", 12), bg="#b3d9ff", fg="#2b3d4f", 
                           width=20, height=2, relief="raised", bd=2, 
                           command=lambda t=tabla: obtener_datos(t))
        button.pack(pady=10, padx=20) 

    # Configurar para la barra lateral (subir y bajar)
    canvas.create_window((0, 0), window=frame_botones_scrollable, anchor="nw")
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    frame_botones_scrollable.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Vista y Diseño para la Tabla
    global treeview
    treeview = ttk.Treeview(ventana, show="headings", style="Custom.Treeview")
    treeview.pack(fill="both", expand=True, padx=20, pady=20)

    estilo = ttk.Style()
    estilo.configure("Custom.Treeview",
                     background="#e6f7ff", 
                     foreground="#2b3d4f", 
                     fieldbackground="#f0f8ff",  
                     font=("Arial", 12))

    estilo.configure("Custom.Treeview.Heading",
                    font=("Arial", 12, "bold"),
                    background="#2b3d4f",  
                    foreground="white")  

    scrollbar_treeview = tk.Scrollbar(ventana, orient="vertical", command=treeview.yview)
    treeview.configure(yscrollcommand=scrollbar_treeview.set)
    scrollbar_treeview.pack(side="right", fill="y")


# Ejecutar la función donde se crea la ventana para el Menú de Inicio
if __name__ == "__main__":
    main()


