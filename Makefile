test: typetalk.py test_typetalk.py
	@coverage run --source myplugin -m py.test --pep8
	@coverage report
