import typing

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)


@router.post("")
async def add_tasks(
        task: typing.Annotated[STaskAdd, Depends()],

) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("/tasks")
async def get_home() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
