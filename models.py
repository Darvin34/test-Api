from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import base


# Таблица работников
class User(base):
    __tablename__ = 'users'
    #  столбцы
    id = Column(Integer, primary_key=True, index=True)  # id работника, первый ключ
    name = Column(String)  # имя работника
    department_id = Column(Integer, ForeignKey(
        'departments.id'))  # id отдела работника, связывает с первичным ключом таблицы отделов
    department = relationship('Department', back_populates='users')  # связь с родительской таблицей


# Таблица отделов
class Department(base):
    __tablename__ = 'departments'
    #  столбцы
    id = Column(Integer, primary_key=True, index=True)  # id отделов, первичный ключ
    name = Column(String, unique=True)  # название отдела
    users = relationship('User', back_populates='department')  # связь с дочерней таблицей
