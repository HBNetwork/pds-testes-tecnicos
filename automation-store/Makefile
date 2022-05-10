help: 		## Show this help.
	@echo "Please use \`make <target>' where <target> is one of"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?##"}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install:	## Install.
	cp .env-default .env
	python3 -m venv venv
	. venv/bin/activate; pip install -r requirements/dev.txt

run:		## Builds, (re)creates, starts, and attaches to containers for a service web.
	python manage.py runserver

urls:		## Run show_urls django command.
	python manage.py show_urls

test: 		## Run command test
	pytest