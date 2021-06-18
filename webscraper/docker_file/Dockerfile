FROM python:3.9
WORKDIR /code
COPY ./requirements_scrap.txt ./
COPY ../ ./
RUN pip install --no-cache-dir -r requirements_scrap.txt
CMD ['ls']
CMD ["python","first_page.py"]