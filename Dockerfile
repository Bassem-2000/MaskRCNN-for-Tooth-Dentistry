FROM python:3.8
WORKDIR /app
RUN apt-get -y update && \
    apt-get install -y libgl1-mesa-glx && \
    apt-get clean
COPY . .
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/facebookresearch/fvcore
RUN pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
RUN git clone https://github.com/facebookresearch/detectron2.git detectron_repo
WORKDIR detectron_repo
RUN pip install -e .
WORKDIR /app

EXPOSE 8501 8000
CMD ["/bin/bash", "-c", "(uvicorn main:app --host 0.0.0.0 --port 8000 --reload & streamlit run 1_🏠_Home.py)"]