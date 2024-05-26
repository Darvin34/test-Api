from pydantic import BaseModel

#  создаём dto, ожидаемые при запросах post и put
class UserDTO(BaseModel):
    name: str
    department_name: str


class DepartmentDTO(BaseModel):
    department_name: str