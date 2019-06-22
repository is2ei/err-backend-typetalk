test: typetalk.py test_typetalk.py
	@coverage run --source typetalk -m py.test --pep8
	@coverage report
