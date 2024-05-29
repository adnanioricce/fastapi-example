from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, CheckConstraint, func, CHAR, VARCHAR, UUID
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class BusinessEntity(Base):
    __tablename__ = 'BusinessEntity'
    BusinessEntityID = Column(Integer, primary_key=True, index=True)
    rowguid = Column(pgUUID(as_uuid=True), default=uuid.uuid1, nullable=False)
    ModifiedDate = Column(DateTime, default=func.now(), nullable=False)

class Person(Base):
    __tablename__ = 'Person'
    BusinessEntityID = Column(Integer, ForeignKey('BusinessEntity.BusinessEntityID'), primary_key=True)
    PersonType = Column(CHAR(2), nullable=False)
    NameStyle = Column(Boolean, default=False, nullable=False)
    Title = Column(VARCHAR(8), nullable=True)
    FirstName = Column(String, nullable=False)
    MiddleName = Column(String, nullable=True)
    LastName = Column(String, nullable=False)
    Suffix = Column(VARCHAR(10), nullable=True)
    EmailPromotion = Column("EmailPromotion",Integer, default=0, nullable=False)
    # AdditionalContactInfo = Column(XML, nullable=True)
    # Demographics = Column(XML, nullable=True)
    rowguid = Column(pgUUID(as_uuid=True), default=uuid.uuid1, nullable=False)
    ModifiedDate = Column(DateTime, default=func.now(), nullable=False)

    __table_args__ = (
        CheckConstraint('"EmailPromotion" BETWEEN 0 AND 2', name='CK_Person_EmailPromotion'),
        CheckConstraint("UPPER(\"PersonType\") IN ('SC', 'VC', 'IN', 'EM', 'SP', 'GC')", name='CK_Person_PersonType'),
    )
