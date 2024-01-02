FROM python:3.10
WORKDIR /app

COPY ["requirements.txt", "requirements-dev.txt", "./"]
RUN pip install -r requirements.txt

ARG ENV="dev"
COPY requirements.txt ./
RUN if [ "${ENV}" = "dev" ]; then \
        pip install -r requirements-dev.txt; \
fi

COPY ./src ./src

CMD ["python3", "./src/main.py"]