boot:
	sudo apt-get install python-setuptools python-dev build-essential

init:
	pip install -r requirements.txt

test:
	nosetests tests
