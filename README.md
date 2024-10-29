# data_platform
Full on data platform

`docker login ghcr.io`
`docker-compose up -d`

## Airbyte: 
Docker setup is deprecated thereby k8 with helm is necessary
### Kubernetes
- enable kubernetes in Docker
- kubectl via Git-Bash https://kubernetes.io/de/docs/tasks/tools/install-kubectl/#installation-der-kubectl-anwendung-mit-curl
- Helm via Git-Bash https://helm.sh/docs/intro/install/#from-winget-windows
### Installation
- `helm repo add airbyte https://airbytehq.github.io/helm-charts`
- `helm repo update`
- `helm search repo airbyte`
- `kubectl create namespace airbyte`
- `helm install airbyte airbyte/airbyte --namespace airbyte --values ./airbyte/values.yaml`

In Bash
- `export POD_NAME=$(kubectl get pods --namespace airbyte -l "app.kubernetes.io/name=webapp" -o jsonpath="{.items[0].metadata.name}")`
- `export CONTAINER_PORT=$(kubectl get pod --namespace airbyte $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")`
- `echo "Visit http://127.0.0.1:8080 to use your application"`
- `kubectl --namespace airbyte port-forward $POD_NAME 8080:$CONTAINER_PORT`
- `helm delete airbyte`
- `kubectl delete deployment airbyte`
- `kubectl delete service airbyte`


### Additions
- https://docs.airbyte.com/deploying-airbyte/creating-secrets
- https://docs.airbyte.com/deploying-airbyte/integrations/database
- https://docs.airbyte.com/operator-guides/using-the-airflow-airbyte-operator

## Airflow: 
- http://localhost:8080

## Superset: 
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



## DataHub: 
- http://localhost:9002
