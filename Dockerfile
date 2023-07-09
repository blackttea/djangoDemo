FROM python:3.7

RUN apt-get update && apt-get install -y --no-install-recommends \
postgresql-client
RUN rm -rf /var/lib/apt/lists/*


WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ $WORKDIR
EXPOSE 8000

RUN  ["python", "manage.py", "migrate"]


CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]