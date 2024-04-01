FROM python:3-alpine

## Install Poetry
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
RUN pip install poetry

## Install Poetry deps
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-root

WORKDIR /usr/src

COPY main.py main.py

RUN mkdir run
WORKDIR /run
CMD ["python3", "/usr/src/main.py"]
