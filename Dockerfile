FROM python:3.8

ENV PYTHONUNBUFFERED 1
WORKDIR /code
EXPOSE 5000
COPY . .

RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

RUN rm -rf tests/ && rm README.md && rm Pipfile.lock && rm app.db && rm .gitignore && rm Dockerfile && rm docker-compose.yml
CMD ["sh","start.sh"]
