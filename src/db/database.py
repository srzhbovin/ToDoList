from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Настройка подключения к базе данных
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5436/ToDoList"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)