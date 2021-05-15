FROM tiangolo/uwsgi-nginx:python3.7
WORKDIR /app
COPY . /app
RUN pip install  -r requirements.txt
CMD python /app/api/inference.py