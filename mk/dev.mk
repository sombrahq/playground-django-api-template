IMAGE = django-api-template:latest
PYTHON = python3.10
K8S_CXT = minikube
NAMESPACE = django-api-template

.PHONY: dev-infra
dev-infra:
	minikube start
	kubectl config use-context "$(K8S_CXT)"
	devspace use namespace "$(NAMESPACE)"


.PHONY: build
dev-build:
	devspace run-pipeline build-dev


.PHONY: dev
dev:
	devspace dev


.PHONY: dev-clean
dev-clean:
	kubectl delete all --all -n "$(NAMESPACE)"
