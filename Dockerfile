FROM python:3.10-slim-buster
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5001
ENV FLASK_APP=script_api.py
CMD ["flask", "run", "--host", "0.0.0.0","--port","5001"]