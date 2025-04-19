# Importamos los módulos
import os
import shutil
from datetime import datetime

# Rutas esperadas
c_principal = "StudyTaskManager"
ruta_actividades = os.path.join(c_principal, "actividades")
ruta_completadas = os.path.join(c_principal, "completadas")

# Creamos las carpetas
os.makedirs(ruta_actividades, exist_ok=True)
os.makedirs(ruta_completadas, exist_ok=True)

# menu principal 
def mostrar_menu():
    print("StudyTask Manager")
    print("1. Agregar actividad")
    print("2. Ver actividades pendientes")
    print("3. Actividades completadas")
    print("4. Salir")
    
# Agregar las actividades
def agregar_actividad():
    titulo = input("Ingrese el titulo:\n")
    descripcion = input("Ingrese la descripcion:\n")
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    nuevo_archivo = f"{titulo.replace(' ', '_')}.txt"
    ruta_completa = os.path.join(ruta_actividades, nuevo_archivo)
    with open(ruta_completa, "w") as archivo:
        archivo.write(f"Titulo: {titulo}\n")
        archivo.write(f"Descripcion: {descripcion}\n")
        archivo.write(f"Hora: {hora}\n")
        
        print("Actividad agregada con éxito")

# Actividades pendientes
def actividades_pendientes():
    archivos = os.listdir(ruta_actividades)
    if not archivos:
        print("No hay actividades pendientes.")
        return
        
    print("\nACTIVIDADES")
    for archivo in archivos:
        print(f" - {archivo}")
        
# Ver actividad completada
def actividad_completada():
    actividades_pendientes()
    nombre = input("Introduzca el nombre exacto del archivo (.txt al final):\n")
    
    origen = os.path.join(ruta_actividades, nombre)
    destino = os.path.join(ruta_completadas, nombre)
    
    if not os.path.exists(origen):
        print("El archivo no existe.")
        return
    shutil.move(origen, destino)
    print("Actividad completada.")
        
# Bucle while la cabeza del programa    
while True:
    mostrar_menu()
    opción = input("Introduzca una opción del (1-4):\n")
    
    if opción == "1":
        agregar_actividad()
    elif opción == "2":
        actividades_pendientes()
    elif opción == "3":
        actividad_completada()
    elif opción == "4":
        print("Hasta luego crack.")
        break
    else:
        print("Opción no valida. Intente nuevamente.")
        
# Función secreta para probar Git
def funcion_secreta():
    print("Esta es una función oculta de prueba")
# mensaje de prueba para git

