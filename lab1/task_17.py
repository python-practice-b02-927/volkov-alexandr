#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while not cell_is_filled():
        move_up(n=1)
    move_right(n=1)
    if not cell_is_filled():
        move_left(n=2)


if __name__ == '__main__':
    run_tasks()
