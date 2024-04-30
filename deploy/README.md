# EmissionsFlow Kubernetes Deployment

This guide provides step-by-step instructions for setting up the EmissionsFlow project on a local Kubernetes cluster using Minikube.

## Prerequisites

Before you begin, ensure you have the following tools installed:

- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)

## Steps

1. **Install Minikube:**

    ```bash
    # Linux
    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
    sudo dpkg -i minikube_latest_amd64.deb

    # macOS with Homebrew
    brew install minikube

    # Verify installation
    minikube version
    ```

2. **Start Minikube:**

    ```bash
    minikube start
    ```

3. **Install kubectl:**

    ```bash
    # Linux
    sudo apt-get update && sudo apt-get install -y kubectl

    # macOS with Homebrew
    brew install kubectl

    # Verify installation
    kubectl version --client
    ```

4. **Apply Kubernetes Configurations:**

    Navigate to the directory containing your YAML files (e.g., `deploy/database`) and apply the configurations:

    ```bash
    kubectl apply -f emissionsflow-db-config.yaml
    kubectl apply -f emissionsflow-db-secret.yaml
    kubectl apply -f emissionsflow-db-storage.yaml
    kubectl apply -f emissionsflow-db-service.yaml
    kubectl apply -f emissionsflow-db-statefulset.yaml
    ```

5. **Monitor Deployment:**

    ```bash
    kubectl get pods
    kubectl get services
    kubectl get statefulsets
    ```

    Wait until the pods are in the `Running` state.

6. **Access PostgreSQL:**

    Forward local port to access PostgreSQL service:

    ```bash
    kubectl port-forward service/emissionsflow-db-service 5432:5432
    ```

    You can now connect to the PostgreSQL database at `localhost:5432` using a PostgreSQL client.

## Cleaning Up

To stop and delete the Minikube cluster, you can use:

```bash
minikube stop
minikube delete
