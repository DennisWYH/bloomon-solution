FROM python
WORKDIR /Users/marve/Documents/codingProjects/bloomon
COPY . .
CMD ["BloomonBouquetMaker.py"]
ENTRYPOINT ["python3"]