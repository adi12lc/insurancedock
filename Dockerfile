FROM python:3.9
CMD mkdir /insuref
COPY . /insuref
WORKDIR /insuref
EXPOSE 8501
RUN pip install -r requirements.txt
CMD streamlit run D_app.py