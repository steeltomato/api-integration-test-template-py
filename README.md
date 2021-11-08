# API Integration Test App Template

The tests defined in this tool are enhanced by the apiritif library, [check it out](https://github.com/Blazemeter/apiritif)

### Organization

* apitest
  * client - Consise representation of a client for the API for the tests to consume
  * testdata - Any static data files (JSON/XML/CSV) for test input
  * tests - The pytest tests themselves
  * util - Various utilities to simplify test creation
  * validations - Common validators used across test suites
* mock-service - Contains a simple service used to test this template project

### Cloning this Template

To add an apitest application to your python project:

* Clone the api-integration-test-template repo
* Copy the project into an existing repo:
  * `cp -R api-integration-test-template <my service>/api-integration-tests`
  * Yes, into the repo. These tests should be ran for each PR before the PR is accepted.
* In the new copy, within api-integration-tests:
  * Remove mock-service/
  * Update the Makefile to remove start-mock/stop-mock and and other undesired items
  * If the project already has pre-commit hooks configured, this functionality can be removed
  * Add some config items to config/default.toml
  * Create your API client in apitest/client
  * Start writing tests!

### Dependencies
This project is built using Python 3.9

It is recommended to use a tool like [pyenv](https://github.com/pyenv/pyenv) to manage multiple versions of python on your local system. On a mac this can be easily installed with [homebrew](https://brew.sh/)

```
brew install pyenv
```

To install the appropriate version, specified by .python-version

```
pyenv install
```

### Dev Setup (non-docker)

Change into the project's directory and execute `pyenv local`

Create a virtual environment: `python -m venv .venv`

Activate the virtual environment: `source .venv/bin/activate`

Install the dependencies: `make deps`

Install pre-commit hooks: `pre-commit install`

### Test/Run the template project

Bring up the mock backend: `make start-mock`

Run the test suite: `make test`

Bring down the mock backend: `make stop-mock`

### Pre-commit

If a commit is made with skipped pre-commit hooks, the suite can be ran on all files with: `pre-commit run -a`
