.PHONY: coverage
coverage:
	-pytest tests --cov-config=qa/.coveragerc --cov=django_api_template --cov-report term --cov-fail-under=0 --cov-report xml:coverage.xml


.PHONY: api
api:
	hurl --variables-file .env api/api.hurl
