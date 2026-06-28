install:
    pip install -r requirements.txt
    python setup.py install
test:
    pytest tests/