FROM python:3.8

ADD . .

RUN pip install -r Group4requirements.txt

CMD ["python", "-m", "unittest", "discover", "-s","Group4Test"]
