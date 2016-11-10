# setup.py

from cx_Freeze import setup, Executable

# must have the latest beta build of cx_Freeze installed for python 3.5.1
# must use the main.py function to make the executable, since it contains all the dependencies

setup(name='pythonGame', version='0.01', description='python game',
      executables=[Executable('main.py')])

# will find and automatically 'freeze/compile' all dependent python files into an '.exe' file
