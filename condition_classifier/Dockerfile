FROM python:3.8
ADD requirements.txt /
RUN pip install -r /requirements.txt
ADD disease_classification_model_for_quickcare_sophie_sharum.py /
ADD model.pkl /
ADD Training.csv /
ADD Testing.csv /
ENV PYTHONUNBUFFERED=1
CMD [ "python", "./disease_classification_model_for_quickcare_sophie_sharum.py" ]