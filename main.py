import os
import cv2
import matplotlib.pyplot as plt
from detectron2 import model_zoo
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import Visualizer,ColorMode
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import numpy as np
import io
import nest_asyncio


app = FastAPI(title= 'API')

@app.get("/")
def read_root():
    return ' Welcome to my Api, if you need any help iam here :) '

@app.post('/Predict')
def Prediction(file:UploadFile=File(...)):
    Filename = file.filename
    FileExtension = Filename.split('.')[-1] in ('jpg', 'jpeg', 'png')
    if not FileExtension:
        raise HTTPException(status_code=415, detail='UnSuported file')
    image = np.asanyarray(bytearray(io.BytesIO(file.file.read()).read()), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file('COCO-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_3x.yaml'))
    cfg.MODEL.WEIGHTS = 'model_final.pth'
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 36
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
    cfg.MODEL.DEVICE = 'cpu'
    predictor = DefaultPredictor(cfg)

    
    out = predictor(image)
    v = Visualizer(image[:, :, ::-1], metadata={}, scale=50)
    v = v.draw_instance_predictions(out['instances'].to('cpu'))
    out = v.get_image()[:, :, ::-1]

    cv2.imwrite(f"{os.path.join('images', Filename)}", out)

    im = open(f"{os.path.join('images', Filename)}", mode= 'rb')

    return StreamingResponse(im, media_type= 'image/jpeg')
nest_asyncio.apply()
