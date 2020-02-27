gcp.deploy.common.topics:
	gcloud pubsub topics create common.health.requested
	gcloud pubsub topics create common.health.processed

gcp.deploy.common.functions:
	gcloud functions deploy health_handler --runtime python37 --trigger-topic common.health.requested

gcp.deploy.init:
	make gcp.deploy.common.topics
	make gcp.deploy.common.functions

gcp.deploy.update:
	make gcp.deploy.common.functions
