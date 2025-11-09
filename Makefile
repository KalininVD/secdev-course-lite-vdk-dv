.PHONY: venv deps init run test ci ci-s06

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

ci-s06:
	$(PY) -m venv .venv
	# для linux нужно заменить ".venv\scripts\" на ".venv/bin/"
	.venv\scripts\pip install -r requirements.txt
	.venv\scripts\python scripts/init_db.py
	mkdir -p EVIDENCE/S06
	.venv\scripts\pytest --junitxml=EVIDENCE/S06/test-report.xml -q