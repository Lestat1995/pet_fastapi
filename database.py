from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker  # изучить доки
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import typing

engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"   # aiosqlite асинхронный драйвер
)

new_session = async_sessionmaker(engine, expire_on_commit=False)   # what this parameter? курсы по алхимии


class Model(DeclarativeBase):
    pass


class TaskOrm(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)  # Обязательно иначе алхимия будет ругаться, база сама задёт id
    name: Mapped[str]
    description: Mapped[typing.Optional[str]]


# создание таблицы хер значет что за функция, взята из доков
# она асинхронная как и драйвер. create_all-создание всех таблиц
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)