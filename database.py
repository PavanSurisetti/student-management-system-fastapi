#this files contains all the database connection and session creation and engine creation
from dotenv import load_dotenv#this is used to access the environment variables
import os
from sqlalchemy import create_engine#used to establish the connection
from sqlalchemy.orm import declarative_base,sessionmaker
load_dotenv()
db_url=os.getenv('db_url')#this will import the db_url file
if not db_url:#to handle if no db_url found in .env file
    raise ValueError("db_url not found in .env file")
#create a engine
engine=create_engine(db_url)#this will establish connection to postgresql
#creating a base class for all the tables
Base=declarative_base()
#session factory
SessionLocal=sessionmaker(bind=engine)