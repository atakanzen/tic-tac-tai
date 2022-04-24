# tic-tac-tai
A minmax based tic-tac-toe game for a school project.

# MinMax Algorithm

We have implemented two functions regarding the variations of MinMax algorithm. One with Alpha-Beta pruning and one without it. 

Alpha-Beta pruning helps us to make our calculation function runs faster. 

You can find more information about Alpha-Beta pruning [here](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

# How to run in local?

We're using python version 3.9, `pyenv`, and `pipenv` for configurating the system's python versions and virtual environments. 
- Install `pyenv`
  - [Install `pyenv` for **MacOS**](https://github.com/pyenv/pyenv#homebrew-in-macos)
  - [Install `pyenv` for **Windows**](https://github.com/pyenv-win/pyenv-win#installation)
- [Install `pipenv`](https://pipenv.pypa.io/en/latest/#install-pipenv-today)
- Use `pyenv` to set your Python version to `3.9.x`
  - With `pipenv shell` command this should be done automatically, however if something goes wrong you can run this command. 
- In project folder, run `pipenv shell` command to create and use a virtual environment. 
- Run `pipenv install` to install dependencies from the `Pipfile`. 
- Run `python main.py` to run the application locally. 
