FROM python:3.11.9-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONNUNBUFFERED 1

COPY estagio_desafio /estagio_desafio

WORKDIR /estagio_desafio

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]