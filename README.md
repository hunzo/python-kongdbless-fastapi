# KONG db-less with Python FastAPI example
- start
```
docker-compose up -d
```
- update config using [`HTTPIe`](https://httpie.io/)
```
http :8001/config config=@kong.yaml
```
- test
```
docker run --rm skandyla/wrk -t5 -c2000 -d30  http://wsl_ip_address:8000/api?x-api-key=my-key
```