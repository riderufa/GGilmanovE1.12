import string, random

import pytest

import game_func

letters = string.ascii_lowercase
hide_letters = '_' * len(letters)
letter = random.choice(letters)
list_text = ['ошибка', 'ошибки']
words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']

def test_change_hideword():
    check_hideword = game_func.change_hide_word(letter, letters, hide_letters)
    assert check_hideword != hide_letters

# @pytest.mark.parametrize("letter", list(letters))
# def test_change_hideword():
#     check_hideword = game_func.change_hide_word(letter, letters, hide_letters)
#     assert check_hideword != hide_letters

def test_len_hideword():
    len_hideword = len(game_func.change_hide_word(letter, letters, hide_letters))
    assert len_hideword == len(hide_letters)

def test_random_word():
    word = game_func.random_word(words)
    assert word in words

def test_insert_letter():
    i = random.random(len(hide_letters))
    check_hideword = game_func.insert_letter(hide_letters, letter, i)
    assert check_hideword[i] == letter

def test_change_errors_count():
    errors_count = random.random(100)
    changed_errors_count = game_func.change_errors_count(errors_count)
    assert changed_errors_count == errors_count + 1

def test_change_errors_text():
    errors_count = random.random(1, 5)
    errors_text = game_func.change_errors_text(errors_count)
    assert errors_text in list_text

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
