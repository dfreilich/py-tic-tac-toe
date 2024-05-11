run:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	python main.py

random:
	docker run -d --pull always --publish 5050:5000 maguirebrendan/random:latest

dev:
	pre-commit install
	pre-commit run --all-files

.PHONY: dev random run
