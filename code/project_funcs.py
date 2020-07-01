import os

def change_dir(directory):
    original = os.getcwd()
    os.chdir(original)
    os.chdir('..')
    os.chdir(os.getcwd() + '/' + directory)