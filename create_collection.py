"""
Creating a Weaviate collection and inserting some mock data.
"""

import weaviate
import weaviate.classes.config as wc
import os
from dotenv import load_dotenv
load_dotenv()

# Define the NLB DNS name (from your setup; replace if needed)
NLB_DNS_NAME = os.getenv("AWS_NLB")
print(f"Connecting to Weaviate cluster via NLB: {NLB_DNS_NAME}")

# Connect to the Weaviate instance using custom settings
client = weaviate.connect_to_custom(
    http_host=NLB_DNS_NAME,
    http_port=8080,  
    http_secure=False,
    grpc_host=NLB_DNS_NAME,
    grpc_port=50051,  
    grpc_secure=False
)

try:
  
    if client.is_ready():
        print("Successfully connected to Weaviate.")
    else:
        print("Failed to connect to Weaviate.")
        client.close()
        exit(1)

    # Step 1: Create a collection for exchanges with shards=2 and replication=1

    client.collections.create(
        name="Exchange",
        properties=[
            wc.Property(name="name", data_type=wc.DataType.TEXT),
            wc.Property(name="location", data_type=wc.DataType.TEXT),
            wc.Property(name="founded_year", data_type=wc.DataType.NUMBER),
        ],
        # Sharding configuration: 2 shards
        sharding_config=wc.Configure.sharding(desired_count=3),
        # Replication configuration: replication factor of 1
        replication_config=wc.Configure.replication(factor=2),
        # Optional: Add a vectorizer if needed; here using none for simplicity
        vectorizer_config=wc.Configure.Vectorizer.none()
    )

    print("Collection 'Exchange' created with 3 shards and replication factor 2.")

   
    exchange_collection = client.collections.get("Exchange")

    # Mock data for stock exchanges
    mock_data = [
        {"name": "New York Stock Exchange", "location": "New York, USA", "founded_year": 1792},
        {"name": "NASDAQ", "location": "New York, USA", "founded_year": 1971},
        {"name": "London Stock Exchange", "location": "London, UK", "founded_year": 1801},
        {"name": "Tokyo Stock Exchange", "location": "Tokyo, Japan", "founded_year": 1878}
    ]


    with exchange_collection.batch.dynamic() as batch:
        for data in mock_data:
            batch.add_object(
                properties=data
            )

    print(f"Successfully inserted {len(mock_data)} exchange records into the collection.")

   
    result = exchange_collection.query.fetch_objects(limit=10)
    print(f"Total objects in collection: {len(result.objects)}")
    
    for obj in result.objects:
        print(f"- {obj.properties['name']} ({obj.properties['location']}) - Founded: {obj.properties['founded_year']}")

finally:
    client.close()
