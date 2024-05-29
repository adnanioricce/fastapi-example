from pydantic import BaseModel, UUID4
from typing import Optional

class PersonBase(BaseModel):
    # BusinessEntityID: int = 0
    PersonType: str
    NameStyle: bool
    Title: Optional[str] = None
    FirstName: str
    MiddleName: Optional[str] = None
    LastName: str
    Suffix: Optional[str] = None
    EmailPromotion: int
    # AdditionalContactInfo: Optional[str] = None
    # Demographics: Optional[str] = None

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    pass

class Person(PersonBase):
    BusinessEntityID: int
    rowguid: UUID4
    ModifiedDate: str

    class Config:
        orm_mode = True
