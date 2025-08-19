# Weaviate

## Prerequisites
Have a K3S weaviate cluster running in some EC2 instances. Checkout this [notebook](https://notebooklm.google.com/notebook/bec57f15-3091-43dd-b93a-70a09de31274) for some context about Weaviate, K8S and K3S.

## Getting Started
This repository consists of python codes to test out different functionalities in a K3S Weaviate cluster like creating a collection, deleting a collection, checking the objects in a cluster and finding the distribution of objects in the cluster. 

### Configuration
Make sure to add your AWS load balancer URL to your `.env` file:

```
AWS_NLB=your-load-balancer-url-here
```

---

Happy Coding!