# basic_sorting
![Build](https://github.com/BollaBerg/basic_sorting/workflows/Build/badge.svg)
![Test basic_sorting](https://github.com/BollaBerg/basic_sorting/workflows/Test%20basic_sorting/badge.svg)
[![codecov](https://codecov.io/gh/BollaBerg/basic_sorting/branch/master/graph/badge.svg)](https://codecov.io/gh/BollaBerg/basic_sorting)


A repo of basic sorting algorithms implemented in Python.

This is mostly just to keep myself busy, while practicing testing, proper docstringing, pip-modularization, etc. It probably won't see any real world use, as all algorithms already have been implemented in Python by people way smarter than I am!

The goal is to turn this into an actual functioning pip-package, in order to practice that!

---

## Setup
### Virtual environment
I would highly recommend using a virtual environment for this! To create a virtual environment, simply run:
```bash
python3 -m venv /path/to/new/virtual/environment
```
To activate, run the following:
 * Windows: `<path-to-venv>\Scripts\activate.bat`
 * POSIX: `source <path-to-venv>/bin/activate`

For more information regarding virtual environments, check out [the documentation](https://docs.python.org/3/library/venv.html)

### Project-specific setup
In order to make the project package-able, move to the root folder (where `setup.py` is located) and run the following code:
```bash
pip install -e .
```

(For more information about this process, check out [this StackOverflow-comment](https://stackoverflow.com/questions/6323860/sibling-package-imports/50193944#50193944), which is where I learnt it)

Install modules required for developing:
```bash
pip install -r requirements.txt
```

## Contributors
Feel free to pipe in if you want to contribute. While this is primarily a practice project for myself to tinker with, I won't stand in the way of someone building upon it to make something cool! Just don't forget my name along the way.

## Authors
* Berg, Andreas
