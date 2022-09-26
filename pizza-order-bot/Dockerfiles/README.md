# Deploy on AWS

1. docker build -t rasa-aws .
2. aws ecr create-repository --repository-name rasa-repo --region eu-west-1
3. docker tag rasa-aws repositoryUri
4. aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin repositoryUri
5. docker push repositoryUri
6. Create a cluster with the Getting Started setup and select "empty template". Enter the repos URL there.
   Also, use Load Balancer with HTTP. Expose ports 5005 and 5055.
7. When done, go to the clusters description and find the DNS Name. This is the URL to talk to the bot. eg:
   EC2Co-EcsEl-14H61AU451TXG-1374907128.us-east-1.elb.amazonaws.com:5005/webhooks/rest/webhook.
8. Deploy Rasa Actions server. TODO
   