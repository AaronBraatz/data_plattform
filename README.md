# data_platform
Full on data platform

`docker login ghcr.io`
`docker-compose up -d`

## Airbyte
### start up
- `docker-compose up -d`
- `docker-compose exec airflow bash`
- `airflow users create \
  --username admin \
  --firstname FIRST_NAME \
  --lastname LAST_NAME \
  --role Admin \
  --email admin@example.com
`
- `docker-compose down`

- http://localhost:8080

Airflow: 
- http://localhost:8080
- 

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