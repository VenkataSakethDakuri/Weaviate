"""
Show live object-per-pod distribution for a Weaviate collection.
Requires Weaviate ≥1.25 (exposes objectCount via /nodes verbose endpoint)
and weaviate-client ≥4.16.
"""

import os
import weaviate
from dotenv import load_dotenv

load_dotenv()                                   # supplies AWS_NLB

NLB = os.getenv("AWS_NLB")                      # e.g.  my-nlb-abc123.elb.amazonaws.com
COLLECTION = "Exchange"                         # collection you want to inspect

client = weaviate.connect_to_custom(
    http_host=NLB,  http_port=8080,  http_secure=False,
    grpc_host=NLB,  grpc_port=50051, grpc_secure=False,
)

def print_distribution(collection: str = COLLECTION) -> None:
    """
    Fetch verbose cluster info once and print object distribution.
    """
    nodes = client.cluster.nodes(output="verbose")   # one round-trip

    print(f"\nLive object distribution for collection '{collection}':\n")

    for node in nodes:
        print(f"Pod: {node.name}   Status: {node.status}")
        shards_for_col = [s for s in node.shards if s.collection == collection]

        if not shards_for_col:
            print("  • No shards for this collection on this pod\n")
            continue

        for shard in shards_for_col:
            print(f"  • Shard {shard.name}  objects={shard.object_count}")
        print()
    
    # for node in nodes:
    #     print(f"Pod: {node.name}   Status: {node.status}")
    #     shards_for_col = [s for s in node.shards if s.collection == collection]
        
    #     for shard in shards_for_col:
    #         print(f"  • Shard {shard.name}")
    #         print(f"    - Objects: {shard.object_count}")
    #         print(f"    - Vector queue: {getattr(shard, 'vectorQueueLength', 'N/A')}")
    #         print(f"    - Index status: {getattr(shard, 'vectorIndexingStatus', 'N/A')}")

    
    

if __name__ == "__main__":
    try:
        if client.is_ready():
            print_distribution()
        else:
            print("Weaviate cluster is not ready.")
        
        

    finally:
        client.close()
