FROM python:3.9.7
WORKDIR /mydir
COPY . .
RUN pip install -r requirements.txt
RUN pip install pytest-html
CMD ["python", "-m", "pytest", "tests/api_tests/", "--html=report.html"]