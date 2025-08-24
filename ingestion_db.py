import pandas as pd
import os
import numpy as np
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='logs/ingestion_db.log',
    filemode='a'
)

engine = create_engine("sqlite:///inventory.db")

def ingest_db (df , table_name, engine):
    df.to_sql(table_name, con = engine, if_exists='replace', index=False)

def load_raw_data():
    start= time.time()
    for file in os.listdir("data"):
        print(file)
        df = pd.read_csv("data/"+file)
        logging.info(f"Ingesting {file}")
        print(df.shape)
        ingest_db(df, file[:-4],engine)
    end= time.time()
    total_time = (end-start) /  60
    logging.info("Ingesting Complete")
    logging.info(f"Total Time taken {total_time} minutes")

if __name__ == "__main__":
    load_raw_data()
