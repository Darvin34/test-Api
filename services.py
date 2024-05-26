from models import User, Department
from sqlalchemy.orm import Session
from data_transfer_objects import UserDTO, DepartmentDTO
# Сервис взаимодействия с пользователем

def create_user(data: UserDTO, database: Session):
    #  Создание пользователя. API ожидает dto - имя пользователя и название отдела
    department = database.query(Department).filter(Department.name == data.department_name).first()  # по названию отдела сервис находит id отдела
    user = User(name = data.name, department_id = department.id)
    try:
        database.add(user)
        database.commit()
        database.refresh(user)
    except Exception as error:
        print(error)

    return user


def get_user(id: int, database):
    #  возвращает пользователя по id
    return database.query(User).filter(User.id == id).first()

def update_user(data: UserDTO, database: Session, id: int):
    #  обновляет данные пользователя по id
    user = database.query(User).filter(User.id == id).first()
    department = database.query(Department).filter(Department.name == data.department_name).first()
    user.name = data.name
    user.department_id = department.id
    database.add(user)
    database.commit()
    database.refresh(user)

    return user

def remove_user(database: Session, id: int):
    #  Поиск пользователя по id и удаление
    user = database.query(User).filter(User.id == id).delete()
    database.commit()

    return user