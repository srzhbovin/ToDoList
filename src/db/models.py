from datetime import timezone

from sqlalchemy import declarative_base, Integer, Column, String, DateTime, func, ForeignKey, Boolean

Base = declarative_base()


class TodoList(Base):
    __tablename__ = 'todo_list'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    created_at = Column(DateTime, server_default=func.now(tz=timezone.utc))  # заполняется само при добавлении записи


class TodoItem(Base):
    __tablename__ = 'todo_item'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    list_id = Column(ForeignKey(TodoList.id), nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now(tz=timezone.utc))
