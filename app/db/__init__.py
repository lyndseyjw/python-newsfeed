from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# generates temp connections for performing CRUD operations
Session = sessionmaker(bind=engine)
# map the models to real MySQL tables
Base = declarative_base()