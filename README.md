[![Build Status](https://travis-ci.org/castlemilk/puzzles.svg?branch=master)](https://travis-ci.org/castlemilk/puzzles)
[![Coverage Status](https://coveralls.io/repos/github/castlemilk/puzzles/badge.svg)](https://coveralls.io/github/castlemilk/puzzles)
# Puzzles
Solving data structure and algorithm problems and
implementing testcases

# project structure
problems

├── categoryA

│   └── solutions1.py

│   └── solutions2.py

│   └── tests

│       └── ...

│       └── solution tests

├── categoryB

│   └── solutions1.py

│   └── solutions2.py

│   └── tests

│       └── ...

│       └── solution tests




# getting started
```bash
git clone https://github.com/castlemilk/puzzles.git
cd puzzles
virtualenv -p `which python3` ./venv
source venv/bin/activate
(venv)$ pip install -r requirements.txt
```
## Run tests
Each solution should have a corresponding test case which
aims to validate the expect output of a solution
for a given input.
We can run the test cases for the current coverage
of the solutions with:
```bash
(venv)$ pytest
```
This will run the pytest suite for all test cases.
If we want to limit the testing to a particular implementation
we can use a regex pattern to match for the corresponding
test cases with:
```bash
(venv)$ pytest -k <some solution name (i.e linkedlist)>
```

## TODO
* Add solutions + tests in Go
* Add solutions + tests in Java
* Add circleCI build and test for project alongside travis CI
