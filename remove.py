"""
Deleting Weaviate collections
"""

import weaviate
import weaviate.classes.config as wc
import os
from dotenv import load_dotenv


load_dotenv()

# Define the NLB DNS name (from your setup; replace if needed)
NLB_DNS_NAME = os.getenv("AWS_NLB")
print(f"Connecting to Weaviate cluster via NLB: {NLB_DNS_NAME}")


client = weaviate.connect_to_custom(
    http_host=NLB_DNS_NAME,
    http_port=8080, 
    http_secure=False,
    grpc_host=NLB_DNS_NAME,
    grpc_port=50051,  
    grpc_secure=False
)

try:
    # Delete the entire collection - this removes all shards and data
    client.collections.delete("Exchange")
    print("Collection 'Exchange' and all its shards have been deleted.")
    
    # Optional: Delete multiple collections at once
    # client.collections.delete(["Exchange", "AnotherCollection"])
    
    # Optional: Delete ALL collections in the instance
    # client.collections.delete_all()  # USE WITH EXTREME CAUTION!
    
finally:
    client.close()