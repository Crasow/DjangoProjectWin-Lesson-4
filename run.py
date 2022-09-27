import os
import subprocess

while True:
    # print('Enter "r" for run server: ')
    answer = 'r'
    if answer == 'r':
        subprocess.call('py manage.py runserver', shell=True)
