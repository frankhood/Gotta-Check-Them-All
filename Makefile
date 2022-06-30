export COMPOSE_PROJECT_NAME=pepposaur_compose
export COMPOSE_FILE=./docker/docker-compose.yaml
COMPOSE_SERVICES=

dup:
	./docker/check_dotenv.sh
	docker compose up ${COMPOSE_SERVICES} -d

dbuild:
	docker compose build ${COMPOSE_SERVICES} --no-cache

ddown:
	docker compose down --remove-orphans

ddestroy:
	docker compose down --remove-orphans -v

dstop:
	docker compose stop ${COMPOSE_SERVICES}

drestart:
	docker compose restart ${COMPOSE_SERVICES}
