FROM python:3
RUN mkdir /usr/src/app/
WORKDIR /usr/src/app/
COPY . /usr/src/app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "app.py" ]