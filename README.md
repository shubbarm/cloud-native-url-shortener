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
