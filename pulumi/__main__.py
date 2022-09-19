"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi_gcp import bigquery, pubsub, storage

# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket(resource_name='data-pipeline-bucket',
                        name="data-pipeline-cloud-portfolio",
                        location="US",
                        labels={
                            "env": "dev",
                        },
                        project="cloud-portfolio-dev"
                        )

pubsub_topic = pubsub.Topic(resource_name="receive-order-topic",
                            name="ReceiveOrder",
                            message_retention_duration="86600s",
                            project="cloud-portfolio-dev",
                            labels={
                                    "env": "dev",
                            }
                            )

dataset = bigquery.Dataset(resource_name="business-dataset",
                           dataset_id="Business",
                           description="Datapipeline Dataset",
                           location="US",
                           delete_contents_on_destroy=True,
                           accesses=[
                               bigquery.DatasetAccessArgs(
                                   role="OWNER",
                                   user_by_email="balthazarpaixao@gmail.com",
                               ),
                               #                               bigquery.DatasetAccessArgs(
                               # role="READER",
                               #                                   domain="anytesting.com"
                               #                               )
                           ],
                           #                           default_partition_expiration_ms=3600000,
                           labels={
                               "env": "dev"
                           },
                           project="cloud-portfolio-dev"
                           )
default_table = bigquery.Table(resource_name="orders-table",
                               dataset_id="Business",
                               table_id="Orders",
                               deletion_protection=False,
                               #                               clustering=None,
                               time_partitioning=bigquery.TableTimePartitioningArgs(
                                   type="DAY",
                                   field="CreationDate"
                               ),

                               project="cloud-portfolio-dev",
                               labels={
                                   "env": "dev",
                               },
                               schema="""[
  {
    "name": "CreationDate",
    "type": "DATETIME",
    "mode": "NULLABLE",
    "description": "Creation"
  },
  {
    "name": "OrderStatus",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "Order Status"
  },
  {
    "name": "OrderId",
    "type": "INTEGER",
    "mode": "NULLABLE",
    "description": "Order identification"
  },
  {
    "name": "CustomerId",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "Customer username"
  },
  {
    "name": "ProductId",
    "type": "INTEGER",
    "mode": "NULLABLE",
    "description": "Product Id"
  },
  {
    "name": "ProductPrice",
    "type": "FLOAT",
    "mode": "NULLABLE",
    "description": "Product price"
  }
]
""")

# Export the DNS name of the bucket
pulumi.export('data-pipeline', bucket.url)
