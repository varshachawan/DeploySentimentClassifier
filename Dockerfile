FROM python:3.7-slim

WORKDIR /usr/src/app
COPY ./ .

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirement.txt

RUN chmod 777 run.sh

EXPOSE 8080

CMD ["./run.sh"]