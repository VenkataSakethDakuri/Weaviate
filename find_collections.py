"""
Getting all Weaviate collections in the cluster.
"""

import os
import weaviate
from dotenv import load_dotenv

load_dotenv()

NLB_DNS_NAME = os.getenv("AWS_NLB")

def get_all_collections():
    client = weaviate.connect_to_custom(
        http_host=NLB_DNS_NAME,
        http_port=8080,
        http_secure=False,
        grpc_host=NLB_DNS_NAME,
        grpc_port=50051,
        grpc_secure=False
    )
    
    try:
        # Get all collections in the cluster
        collections = client.collections.list_all()
        
        print(f"Total collections found: {len(collections)}")
        
        if collections:
            for collection_name in collections:
                print(f"- {collection_name}")
                
                # Optional: Get basic info about each collection
                try:
                    collection = client.collections.get(collection_name)
                    # Get a count of objects in this collection
                    count = collection.aggregate.over_all(total_count=True).total_count
                    print(f"  Objects count: {count}")
                except Exception as e:
                    print(f"  Could not get object count: {e}")
        else:
            print("No collections found in the cluster.")
            
    finally:
        client.close()

get_all_collections()
