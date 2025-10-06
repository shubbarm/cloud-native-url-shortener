# Cloud-Native URL Shortener

A fully GitOps-managed, Kubernetes-native URL shortener built for learning, labs, and portfolio showcasing. This project demonstrates modern DevOps practices including ArgoCD, RBAC, NetworkPolicies, PodSecurity, and a full observability stack with Prometheus, Grafana, and Fluent Bit.

## Architecture Overview

- **Frontend**: Next.js app served via Kubernetes
- **Backend**: FastAPI service with PostgreSQL
- **GitOps**: ArgoCD syncs manifests from GitHub
- **Monitoring**: Prometheus + Grafana dashboards
- **Logging**: Fluent Bit for log collection
- **Security**: RBAC, NetworkPolicies, PodSecurityContext


## Key Features

- GitOps deployment via ArgoCD
- Declarative Helm-based observability stack
- NetworkPolicies to restrict pod communication
- Prometheus metrics and Grafana dashboards
- Fluent Bit log forwarding (stdout)

## Technologies Used

- Kubernetes
- ArgoCD
- Helm
- Prometheus
- Grafana
- Fluent Bit
- FastAPI
- Next.js
- Docker
- GitHub Actions (optional CI)

## Screenshots

- ArgoCD dashboard showing synced apps
- Grafana dashboards with live metrics
- Prometheus targets page
- Fluent Bit logs in pod output

## Final note

This project is for testing, labs, and educational purposes only. It is **not production-ready**. Some values are hardcoded for simplicity.


## Screenshots

<details>
<summary>Click to expand full gallery</summary>

![Screenshot 1](assets/Screenshot%20from%202025-10-06%2012-06-46.png)
![Screenshot 2](assets/Screenshot%20from%202025-10-06%2012-26-29.png)
![Screenshot 3](assets/Screenshot%20from%202025-10-06%2012-51-01.png)
![Screenshot 4](assets/Screenshot%20from%202025-10-06%2014-16-13.png)
![Screenshot 5](assets/Screenshot%20from%202025-10-06%2014-17-04.png)
![Screenshot 6](assets/Screenshot%20from%202025-10-06%2014-18-02.png)
![Screenshot 7](assets/Screenshot%20from%202025-10-06%2014-19-11.png)
![Screenshot 8](assets/Screenshot%20from%202025-10-06%2014-49-47.png)
![Screenshot 9](assets/Screenshot%20from%202025-10-06%2014-50-47.png)
![Screenshot 10](assets/Screenshot%20from%202025-10-06%2014-52-24.png)
![Screenshot 11](assets/Screenshot%20from%202025-10-06%2015-08-41.png)
![Screenshot 12](assets/Screenshot%20from%202025-10-06%2015-11-06.png)
![Screenshot 13](assets/Screenshot%20from%202025-10-06%2016-17-09.png)
![Screenshot 14](assets/Screenshot%20from%202025-10-06%2016-18-05.png)
![Screenshot 15](assets/Screenshot%20from%202025-10-06%2018-30-38.png)
![Screenshot 16](assets/Screenshot%20from%202025-10-06%2018-32-10.png)
![Screenshot 17](assets/Screenshot%20from%202025-10-06%2018-40-17.png)
![Screenshot 18](assets/Screenshot%20from%202025-10-06%2019-04-38.png)
![Screenshot 19](assets/Screenshot%20from%202025-10-06%2019-08-59.png)

</details>
