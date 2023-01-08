FROM python:3.9
RUN pip install --upgrade pip
COPY requirements.txt /home/
RUN pip install -r /home/requirements.txt
COPY *.py /home/
COPY templates/*.* /home/templates/
ENTRYPOINT ["python"]
CMD ["/home/catalogue.py" ]
EXPOSE 5000
