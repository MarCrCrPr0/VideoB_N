
import cv2              # 1- Uso de librería OpenCV: lectura y escritura de videos
import numpy as np      # Librería NumPy: manejo de arreglos
from PIL import Image   # 1- Uso de librería Pillow: manipulación de imágenes
import time             # Librería estándar: medir tiempos

# Definir rutas de entrada y salida
# Video original en carpeta "Video", resultado en carpeta "resultados"
ruta_entrada = "../Video/video_color.mp4"
ruta_salida = "../resultados/video_bn.mp4"

# Abrir el video original con OpenCV
cap = cv2.VideoCapture(ruta_entrada)
if not cap.isOpened():
    print("No se pudo abrir el video de entrada.")
    exit()

# 4- Duración del video y resolución
fps_real = cap.get(cv2.CAP_PROP_FPS)          # Obtiene fps reales (ej. 59.94)
fps = round(fps_real)                         # Redondea a 60 fps
ancho = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duracion = total_frames / fps
print(f"Duración del video: {duracion/60:.2f} minutos")
print(f"Resolución: {ancho}x{alto} a {fps} fps")

# Crear objeto para escribir el nuevo video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(ruta_salida, fourcc, fps, (ancho, alto), True)

# 3- Medir tiempo total de la tarea
inicio = time.time()

# 2- Procesar los fotogramas del video uno por uno
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir fotograma a formato Pillow (1- uso de librería Pillow)
    pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Convertir a blanco y negro con Pillow (2- conversión a b/n)
    pil_bn = pil_img.convert("L")

    # Volver a NumPy y a 3 canales para OpenCV
    frame_bn = cv2.cvtColor(np.array(pil_bn), cv2.COLOR_GRAY2BGR)

    # Guardar el fotograma en el nuevo video
    out.write(frame_bn)

# Liberar recursos
cap.release()
out.release()

# 3- Calcular tiempo total de la tarea realizada
fin = time.time()
tiempo_total = fin - inicio
print(f"Tiempo total de procesamiento: {tiempo_total:.2f} segundos ({tiempo_total/60:.2f} minutos)")
print(f"Video generado en: {ruta_salida}")


