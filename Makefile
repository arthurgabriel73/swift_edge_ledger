include .env.test

.PHONY: build up down clean remove-image logs

export ENV=test
export PYTHONPATH=$(pwd)

test: unit bdd

unit:
	@echo "\033[0;36mRunning unit tests...\033[0m"
	export ENV=test
	export PYTHONPATH=$(pwd)
	poetry run coverage run --source=./ -m pytest -v
	@echo "\033[0;32mUnit tests completed successfully!\033[0m"

bdd: test-db
	@echo "\033[0;36mRunning BDD tests...\033[0m"
	export ENV=test
	export PYTHONPATH=$(pwd)
	poetry run coverage run --source=./ -m behave
	@echo "\033[0;32mBDD tests completed successfully!\033[0m"

test-db:
	@echo "\033[0;36mStarting test database...\033[0m"
	export ENV=test
	export PYTHONPATH=$(pwd)
	docker rm -f test-db || true
	docker run -d --name test-db -p $(DATABASE_PORT_VALUE):$(DATABASE_PORT_VALUE) \
		-e POSTGRES_USER=$(DATABASE_USER_VALUE) \
		-e POSTGRES_PASSWORD=$(DATABASE_PASSWORD_VALUE) \
		-e POSTGRES_DB=$(DATABASE_NAME_VALUE) \
		postgres:16.3
	@echo "\033[0;32mSetup completed successfully!\033[0m"