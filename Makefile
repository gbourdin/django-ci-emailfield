.PHONY: test release


test:
	py.test

release:
	rm -rf dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*

clean:
	find . -name '*.pyc' -delete
