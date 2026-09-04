FROM python:3.8-slim
WORKDIR /app

COPY . /app

# Fijamos las dependencias obsoletas que rompen con Flask 1.1.2
RUN pip install --no-cache-dir "markupsafe<2.1.0" "Werkzeug<2.0.0" "Jinja2<3.0.0" "itsdangerous<2.0.0" Flask==1.1.2 PyMySQL==0.9.3 pytest

EXPOSE 5050
CMD ["python", "app.py"]