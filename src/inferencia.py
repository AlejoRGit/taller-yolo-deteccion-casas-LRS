from ultralytics import YOLO
import os
import cv2

def cargar_modelo(ruta_pesos):
    """
    Carga el modelo entrenado.
    """
    if not os.path.exists(ruta_pesos):
        raise FileNotFoundError(f"No se encontró el modelo en {ruta_pesos}")
    
    model = YOLO(ruta_pesos)
    return model


def detectar_imagen(model, ruta_imagen, guardar=True, output_dir="../models/predicciones"):
    """
    Ejecuta detección sobre una imagen y muestra/guarda resultados.
    """

    if not os.path.exists(ruta_imagen):
        raise FileNotFoundError(f"No se encontró la imagen {ruta_imagen}")

    # Ejecutar inferencia
    results = model(ruta_imagen)

    # Mostrar resultados en pantalla
    results[0].show()

    # Imprimir detecciones con probabilidad
    print("\nDetecciones encontradas:")
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        print(f"Clase: {model.names[cls_id]} | Probabilidad: {conf:.4f}")

    # Guardar imagen con bounding boxes
    if guardar:
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, os.path.basename(ruta_imagen))
        results[0].save(filename=output_path)
        print(f"\nImagen guardada en: {output_path}")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    modelo_path = os.path.join(base_dir, "models/house_detector/weights/best.pt")
    imagen_prueba = os.path.join(base_dir, "ejemplo3.jpg")

    modelo = cargar_modelo(modelo_path)
    detectar_imagen(modelo, imagen_prueba)
