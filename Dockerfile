FROM python:3.8

COPY ./enoki /enoki

WORKDIR /enoki

RUN pip install -r requirements.txt
RUN chmod +x wait-for-it.sh

CMD ["./wait-for-it.sh" , "enoki_db:5432", "--timeout=50", "--" , "python", "manage.py", "runserver", "0.0.0.0:8000"]
