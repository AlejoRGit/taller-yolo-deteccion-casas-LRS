from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI()

# cargar modelo entrenado
model = YOLO("models/house_detector/weights/best.pt")


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # leer imagen
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    # inferencia
    results = model(image)

    # dibujar bounding boxes
    annotated = results[0].plot()

    # convertir a imagen
    img = Image.fromarray(annotated)

    # guardar en buffer
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/jpeg")
