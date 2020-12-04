FROM python:3.9-slim

WORKDIR /work

ADD groovy_thing_back /work/groovy_thing_back
ADD Pipfile /work/Pipfile
ADD Pipfile.lock /work/Pipfile.lock
RUN pip install --upgrade pip && \
  pip install --no-cache-dir pipenv && \
  pipenv lock -r > requirements.txt && \
  pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn","groovy_thing_back.main:app","--host","0.0.0.0","--port","8080"]
