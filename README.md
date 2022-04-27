# README.md

cd into project and execute on Mac/Linux:

./install_run_test.sh

Results:

================ test session starts ================
platform darwin -- Python 3.9.9, pytest-7.1.2, pluggy-1.0.0 -- $HOME/Documents/ubs_helix/.venv/bin/python
cachedir: .pytest_cache
rootdir: $HOME/Documents/ubs_helix, configfile: overage
collected 1 item                                                                                                                                                       

tests/test_Sebastian_Cheung_Python.py::TestGuru::test_ask PASSED                                                                                                 [100%]

================ 1 passed in 0.02s ================





### Commands to run to get test running

➜  virtualenv .venv --python=3.9

➜  source .venv/bin/activate


### Once inside our virtual environment as noted by (.venv) in front of the prompt:

(.venv) ➜  pip install pytest


### Run test

(.venv) ➜ pytest -v -coverage


### Results (100%)

============================== test session starts ==============================
platform darwin -- Python 3.9.9, pytest-7.1.2, pluggy-1.0.0 -- $HOME/Documents/ubs_helix/.venv/bin/python
cachedir: .pytest_cache
rootdir: $HOME/Documents/ubs_helix, configfile: overage
collected 1 item                                                                                                                              

tests/test_Sebastian_Cheung_Python.py::TestGuru::test_ask PASSED                                                                                             [100%]

============================== 1 passed in 0.02s ==============================
