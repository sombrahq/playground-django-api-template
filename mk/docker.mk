IMAGE = django-api-template:latest

.PHONY: docker
docker:
	podman build . -t $(IMAGE)
