FROM python:3.9
WORKDIR /code
COPY ./requirements_api.txt ./
COPY . .
RUN pip install --no-cache-dir -r requirements_api.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
