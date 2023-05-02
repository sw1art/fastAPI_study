from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean,\
    ForeignKey, JSON, Table, MetaData
from datetime import datetime

metadata = MetaData()

role = Table(
    'role', 
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('permissions', JSON),
)


user = Table(
    'user',
    metadata, 
    Column('id', Integer, primary_key=True),
    Column('email', String(length=320), unique=True, index=True, nullable=False),
    Column('username', String(length=20), nullable=False, unique=True),
    Column('hashed_password', String(length=1024), nullable=False),
    Column('firstname', String(length=50)),
    Column('lastname', String(length=120)),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey(role.c.id)),
    Column('age', Integer),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
)


# engine = sqlalchemy.create_engine(DATABASE_URL)
# metadata.create_all(engine)