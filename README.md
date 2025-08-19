# Weaviate

## Prerequisites
- Have a K3S weaviate cluster running in some EC2 instances. Checkout this [notebook](https://notebooklm.google.com/notebook/bec57f15-3091-43dd-b93a-70a09de31274) for some context about Weaviate, K8S and K3S.

- Install all dependencies from requirements.txt using:
```bash
pip install -r requirements.txt
```

- Thirst to explore 😊

## Getting Started
Weaviate is an open-source vector database for semantic search and retrieval that stores embeddings and metadata, supports hybrid search (keyword+vector), and scales horizontally for use cases like RAG, recommendations, and multimodal search. Kubernetes (k8s) is a container orchestration platform that automates deployment, scaling, and resilience of applications; together, teams often run Weaviate on k8s to manage clustered, stateful vector workloads with declarative configs, high availability, and seamless scaling in production.

This repository consists of python codes to test out different functionalities in a K3S Weaviate cluster like creating a collection, deleting a collection, checking the objects in a cluster and finding the distribution of objects in the cluster. 

### Configuration
Make sure to add your AWS load balancer URL to your `.env` file:

```
AWS_NLB=your-load-balancer-url-here
```

## References
[Weaviate Official Documentation](https://weaviate.io/)

---

Happy Coding!