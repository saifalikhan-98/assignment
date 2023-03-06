from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func

from sql_app.database import Base


class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    last_login=Column(DateTime(timezone=True))
