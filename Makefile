gcp.deploy.common.topics:
	gcloud pubsub topics create common.health.requested
	gcloud pubsub topics create common.health.processed

gcp.deploy.common.functions:
	gcloud functions deploy health_handler --runtime python37 --trigger-topic common.health.requested

dcp.deploy.init:
	gcp.deploy.common.topics
	gcp.deploy.common.functions

dcp.deploy.update:
	gcp.deploy.common.functions
