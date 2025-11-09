.PHONY: venv deps init run test ci test-s06 ci-s06

PY?=python

venv:
	$(PY) -m venv .venv

deps:
	pip install -r requirements.txt

init:
	$(PY) scripts/init_db.py

run:
	uvicorn app.main:app --host 127.0.0.1 --port 8000

test:
	pytest -q

ci:
	mkdir -p EVIDENCE/S08
	pytest --junitxml=EVIDENCE/S08/test-report.xml -q

test-s06:
	mkdir -p EVIDENCE/S06
	pytest --junitxml=EVIDENCE/S06/test-report.xml -q

ci-s06: deps init test-s06