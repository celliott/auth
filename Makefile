include default.mk
export

validate :
	docker-compose config --quiet

build : validate
	docker-compose build

push : build
	docker-compose push

up :
	docker-compose up -d

down :
	docker-compose down

deploy :
	helm init --client-only
	-kubectl create namespace ingress
	helm upgrade -i $(SERVICE) helm/$(SERVICE) \
		--namespace ingress \
		--set ingress.hostname=$(SERVICE).$(DOMAIN) \
		--set ingress.enabled=true

delete :
	helm del --purge $(SERVICE)
