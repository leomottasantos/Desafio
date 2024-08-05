FROM python:3.11.9-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONNUNBUFFERED 1

COPY estagio_desafio /estagio_desafio

COPY scripts /scripts

WORKDIR /estagio_desafio

RUN pip install -r requirements.txt

RUN chmod -R +x /scripts

EXPOSE 8000

ENV PATH="/scripts:$PATH"

CMD ["commands.sh"]