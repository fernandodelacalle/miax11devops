# miax11devops



Para hacerlo manual:

1. Create the repositorio en ECR (con comando o desde la UI):
aws ecr create-repository --repository-name lambdamiax11  --region eu-west-3

# Build the image
docker build -t 076977333390.dkr.ecr.eu-west-1.amazonaws.com/fastapi-suma:0.0.1 .

# To test:
# docker run  -p 8080:8080 467432373215.dkr.ecr.eu-west-1.amazonaws.com/fastapi-suma

# Log docker into the aws registry
aws ecr get-login-password | docker login --username AWS --password-stdin 076977333390.dkr.ecr.eu-west-1.amazonaws.com

# Push the image
docker push 076977333390.dkr.ecr.eu-west-1.amazonaws.com/fastapi-suma:0.0.1


