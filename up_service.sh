#! /bin/sh

cd pulumi

pulumi up

gcloud dataflow jobs run parse-orders --gcs-location gs://dataflow-templates-us-central1/latest/PubSub_to_BigQuery --region us-central1 --max-workers 1 --num-workers 1 --staging-location gs://data-pipeline-cloud-portfolio/tmp/ --parameters inputTopic=projects/cloud-portfolio-dev/topics/ReceiveOrder,outputTableSpec=cloud-portfolio-dev:Business.Orders