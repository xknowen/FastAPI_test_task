from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    balance = Column(Integer, default=0)

    owner = relationship("User", back_populates="accounts")