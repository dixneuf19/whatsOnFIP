.PHONY: build push release deploy force-reload

DOCKER_REPOSITERY="dixneuf19"
IMAGE_NAME="whatsonfip"
# IMAGE_TAG="arm"
IMAGE_TAG="latest"
DOCKER_IMAGE_PATH="$(DOCKER_REPOSITERY)/$(IMAGE_NAME):$(IMAGE_TAG)"
APP_NAME="whats-on-fip"

build:
	docker build -t $(DOCKER_IMAGE_PATH) .

run:
	docker run -p 8000:80 --env-file=.env $(DOCKER_IMAGE_PATH)

push:
	docker push $(DOCKER_IMAGE_PATH)

release: build push
