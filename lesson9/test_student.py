# test_group_student.py

import pytest
from sqlalchemy import create_engine, Column, Integer, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

# Подключение к БД
DATABASE_URL = "postgresql+psycopg2://login:password@localhost:5432/sky"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class GroupStudent(Base):
    __tablename__ = "group_student"

    user_id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, nullable=False)

    __table_args__ = {"schema": "public"}


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Проверяем, что таблица существует."""
    metadata = MetaData()
    metadata.reflect(engine, only=["group_student"])
    assert "group_student" in metadata.tables, "Таблица group_student не найдена"
    yield


@pytest.fixture
def db_session():
    """Сессия с откатом после каждого теста."""
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionLocal(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()


def test_create_student(db_session):
    """Тест: добавление записи в group_student"""
    new_record = GroupStudent(user_id=1001, group_id=999)
    db_session.add(new_record)
    db_session.commit()

    record = db_session.query(GroupStudent).filter_by(user_id=1001).first()
    assert record is not None
    assert record.user_id == 1001
    assert record.group_id == 999


def test_update_student(db_session):
    """Тест: изменение записи"""
    # Добавляем запись
    record = GroupStudent(user_id=1002, group_id=888)
    db_session.add(record)
    db_session.commit()

    # Обновляем group_id
    record.group_id = 777
    db_session.commit()

    # Проверяем обновление
    updated = db_session.query(GroupStudent).filter_by(user_id=1002).first()
    assert updated.group_id == 777


def test_delete_student(db_session):
    """Тест: удаление записи"""
    # Добавляем запись
    record = GroupStudent(user_id=1003, group_id=666)
    db_session.add(record)
    db_session.commit()

    # Удаляем
    db_session.delete(record)
    db_session.commit()

    # Проверяем, что её нет
    deleted = db_session.query(GroupStudent).filter_by(user_id=1003).first()
    assert deleted is None
