############
### Prod ###
############

FROM python:3.10.7-slim as build

COPY . /app
WORKDIR /app
RUN python -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade \
    && /opt/venv/bin/pip install psycopg2-binary \
    && /opt/venv/bin/pip install -r requirements.txt \
    && chmod +x entrypoint.sh \
    && chmod +x migrate.sh
RUN apt-get update && apt-get install -y vim
CMD ["/app/entrypoint.sh"]