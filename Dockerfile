FROM python:3.8.6-slim

WORKDIR /frontend
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 
COPY . .
EXPOSE 80
CMD ["gunicorn","-w","2","--timeout","92","-b","0.0.0.0:80","webcreator.wsgi:application"]
