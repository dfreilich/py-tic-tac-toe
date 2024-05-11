dev:
	pre-commit install
	pre-commit run --all-files

random:
	docker run -d --pull always --publish 5050:5000 maguirebrendan/random:latest

run:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	python main.py

test:
	python -m coverage run -m unittest discover
	python -m coverage report -m

.PHONY: dev random run test
