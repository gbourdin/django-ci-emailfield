.PHONY: test release


test:
	py.test

release:
	rm -rf dist/*
	python setup.py sdist
	twine upload dist/*

clean:
	find . -name '*.pyc' -delete
