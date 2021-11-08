
clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build:  ## remove build artifacts
	rm -rf build/ dist/ .eggs/
	rm -rf *.egg-info *.egg

clean-pyc:  ## remove Python file artifacts
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '*~' -delete
	find . -name '__pycache__' -delete

clean-test:  ## remove test and coverage artifacts
	rm -rf .coverage htmlcov/

clean-docker:
	docker rm apitest-template || echo "Removed container"
	docker rm mock-service || echo "Removed container"
	docker network rm apitest || echo "Removed network"

deps:
	python -m pip install -r requirements.txt

test:
	pytest -vv .

test-docker:
	docker rm apitest-template || echo "" 2>&1
	docker network create apitest || echo "Network created"
	docker build -t apitest-template .
	docker run -it --name apitest-template --network apitest -e APITEST_BASEURL="http://mock-service:8000" apitest-template
	docker rm apitest-template

start-mock:
	docker rm mock-service || echo 2>&1
	docker network create apitest || echo "Network created"
	docker build -f mock-service/Dockerfile -t mock-service ./mock-service
	docker run --name mock-service -p 8000:8000 --network apitest -d mock-service

stop-mock:
	docker kill mock-service || echo "Already stopped"
	docker rm mock-service
	docker network rm apitest || echo "Network removed"

start-mock-nondocker:
	uvicorn --app-dir mock-service --reload-dir mock-service main:app --reload

scan-deps:
	docker scan
