FROM python
WORKDIR /app
COPY . .
CMD ["BloomonBouquetMaker.py"]
ENTRYPOINT ["python3"]