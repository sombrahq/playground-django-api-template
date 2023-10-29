
.PHONY: bdd
bdd:
	business/run.sh

.PHONY: coverage
coverage:
	pytest --cov-config=qa/.coveragerc --cov --cov-report term --cov-report xml:coverage.xml
