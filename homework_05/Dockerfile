FROM agrigorev/zoomcamp-model:2025

WORKDIR /app

COPY pyproject.toml .

RUN pip install fastapi uvicorn "scikit-learn==1.6.1" pandas

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]