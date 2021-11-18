make build:
	docker build -t game_of_life .
make start:
	docker run -p 8080:8521 game_of_life
make chrome:
	start chrome 127.0.0.1:8080