import string, random

import pytest

import game_func

letters = string.ascii_lowercase
hide_letters = '_' * len(letters)
letter = random.choice(letters)

def test_check_letter():
    check_hide_letters = game_func.check_letter(letter, letters, hide_letters)
    assert check_hide_letters != hide_letters

# TASK_ID = 1
# TASK_TEXT = "text text"
# TASKS = {TASK_ID: TASK_TEXT}

# def test_get_task_id_exists(tasks):
#     result_task = service.get_task(TASK_ID)
#     assert result_task == TASK_TEXT

# def test_get_task_doesnt_exist(tasks):
#     result_task = service.get_task(2)
#     assert result_task is None

# def test_get_all_tasks_empty(tasks_empty):
#     all_tasks = service.get_all_tasks()
#     assert all_tasks == {}

# def test_get_all_tasks_not_empty(tasks):
#     all_tasks = service.get_all_tasks()
#     assert all_tasks == TASKS

# def test_create_task_success():
#     date = (
#             datetime.datetime.now() + 
#             datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
#     task = service.create_task(date, TASK_TEXT)
#     assert task 

# def test_create_task_in_the_past():
#     date = (
#             datetime.datetime.now() - 
#             datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
    
#     task = service.create_task(date, TASK_TEXT)
#     assert task is None
