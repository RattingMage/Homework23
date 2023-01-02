FROM python:3.11

ENV HOME /app
WORKDIR $HOME

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]