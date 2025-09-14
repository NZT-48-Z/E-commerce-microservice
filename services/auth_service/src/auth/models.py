from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pydantic import EmailStr

from auth.column_types import intpk, created_at, updated_at
from auth.enums import UserStatus
from database.database import Base


class UsersOrm(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    email: Mapped[EmailStr] = mapped_column(unique=True, index=True, nullable=False)
    phone: Mapped[str] = mapped_column(
        length=16, unique=True, index=True, nullable=True
    )
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[UserStatus] = mapped_column(
        Enum(UserStatus, name="user_status_enum"),
        default=UserStatus.ACTIVE,
        nullable=False,
    )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    roles = relationship(
        "RolesOrm", secondary="role_permissions", back_populates="users"
    )


class RolesOrm(Base):
    __tablename__ = "roles"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(length=50, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(length=255, nullable=True)

    users = relationship(
        "UsersOrm", secondary="role_permissions", back_populates="roles"
    )


class PermissionsOrm(Base):
    __tablename__ = "permissions"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(length=50, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(length=255, nullable=True)


class RolePermissionsOrm(Base):
    __tablename__ = "role_permissions"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True
    )