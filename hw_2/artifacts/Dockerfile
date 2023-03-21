FROM python:3.9

RUN apt-get update && \
    apt-get install -y texlive-latex-base \
    apt-get install graphviz graphviz-dev

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "generate_pdf.py"]
