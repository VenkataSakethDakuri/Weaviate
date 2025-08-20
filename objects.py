"""
Creating a Weaviate collection and inserting mock data.
"""

import os
import weaviate
import requests
from dotenv import load_dotenv


load_dotenv()

NLB_DNS_NAME = os.getenv("AWS_NLB")

def check_data_exists():
    client = weaviate.connect_to_custom(
        http_host=NLB_DNS_NAME,
        http_port=8080,
        http_secure=False,
        grpc_host=NLB_DNS_NAME,
        grpc_port=50051,
        grpc_secure=False
    )
    
    try:
        collection = client.collections.get("Exchange")
        objects = collection.query.fetch_objects(limit=100, include_vector=False).objects
        
        print(f"Total objects found: {len(objects)}")
        
        if objects:
            for obj in objects:
                print(f"- {obj.properties.get('name', 'N/A')} (UUID: {obj.uuid})")
        else:
            print("No objects found. Data may not be inserted yet.")
            
    finally:
        client.close()

check_data_exists()