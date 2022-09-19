from pyspark.sql import SparkSession
from pyspark.sql.types import *
from datetime import date
import time

import sparknlp
spark = sparknlp.start()

from sparknlp.pretrained import PretrainedPipeline

explain_document_pipeline = PretrainedPipeline("explain_document_ml")

def annotate_text(text):
    annotations = explain_document_pipeline.annotate(text)
    return annotations

if __name__ == '__main__':

    df = spark.read.csv("/FileStore/analyst_ratings_processed.csv", header=True)

    t1 = time.time()
    annotations = explain_document_pipeline.annotate(df, 'title')
    t2 = time.time()

    print(t2-t1)