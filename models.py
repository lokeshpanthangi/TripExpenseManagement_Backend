from database import Base
from sqlalchemy import Column, Integer, String, DateTime, UUID, ForeignKey, ARRAY, Table
from datetime import datetime, timedelta
from sqlalchemy.orm import relationship


group_members = Table(
    "group_members",
    Base.metadata,
    Column("group_id", UUID(as_uuid=True), ForeignKey("groups.id"), primary_key=True),
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True),
)

expense_splits = Table(
    "expense_splits",
    Base.metadata,
    Column("expense_id", UUID(as_uuid=True), ForeignKey("expenses.id"), primary_key=True),
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True),
)


class Users(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)
    password = Column(String)
    groups = relationship(
        "Groups",
        secondary=group_members,
        back_populates="members"
    )
    created_at = Column(DateTime, default=datetime.utcnow() + timedelta(hours=5, minutes=30))


class Groups(Base):
    __tablename__ = "groups"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, index=True)
    created_by = Column(UUID, ForeignKey("users.id"))
    members = relationship(
        "Users",
        secondary=group_members,
        back_populates="groups"
    )   
    created_at = Column(DateTime, default=datetime.utcnow() + timedelta(hours=5, minutes=30))

class Expenses(Base):
    __tablename__ = "expenses"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    group_id = Column(UUID(as_uuid=True), ForeignKey("groups.id"))
    description = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    paid_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    # relationships
    group = relationship("Groups", backref="expenses")
    payer = relationship("Users", foreign_keys=[paid_by])
    split_between = relationship(
        "Users",
        secondary=expense_splits,
        back_populates="expenses_split"
    )


# ----------------- Settlements -----------------
class Settlement(Base):
    __tablename__ = "settlements"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    group_id = Column(UUID(as_uuid=True), ForeignKey("groups.id"))
    from_user = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    to_user = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    amount = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # relationships
    group = relationship("Groups", backref="settlements")
    from_user_rel = relationship("Users", foreign_keys=[from_user], backref="settlements_made")
    to_user_rel = relationship("Users", foreign_keys=[to_user], backref="settlements_received")