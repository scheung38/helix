python -m pip install --user virtualenv
virtualenv .venv --python=3.9
source .venv/bin/activate
pip install pytest
pytest -v -coverage