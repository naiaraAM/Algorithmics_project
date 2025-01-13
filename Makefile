front-build:
	docker build -t algo-front -f front.Dockerfile  .

front-run: 
	docker run -it  -p 3000:3000  algo-front  