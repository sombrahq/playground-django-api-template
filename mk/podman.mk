IMAGE = django-api-template:latest
BUILDER = podman

.PHONY: container
container:
	$(BUILDER) build . -t $(IMAGE)
