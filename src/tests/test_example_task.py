from app.models import ExampleModel
from app.tasks import example_task


def test_creates_new_entry(session):
    example_task()

    assert session.query(ExampleModel).count() == 1


def test_creates_new_entry_as_many_times_as_task_called(session):
    for _ in range(3):
        example_task()

    assert session.query(ExampleModel).count() == 3
