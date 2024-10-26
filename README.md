# data_platform
Full on data platform

`docker login ghcr.io`
`docker-compose up -d`

Airbyte: 
- http://localhost:8000 (Server)
- http://localhost:8001 (Webapp)

Airflow: 
- http://localhost:8080

Superset: 
- http://localhost:8088
- `docker exec -it <superset_container_id> /bin/bash`
- ```superset fab create-admin \
    --username admin \
    --firstname Superset \
    --lastname Admin \
    --email admin@superset.com \
    --password admin
  ```
- `superset db upgrade`
- [optional] `superset load_examples`
- `superset init`



DataHub: 
- http://localhost:9002