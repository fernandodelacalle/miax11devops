# miax11devops



Para hacerlo manual:

1. Create the repositorio en ECR (con comando o desde la UI):
```bash
aws ecr create-repository --repository-name lambdamiax11  --region eu-west-3
```

2. Build the image
```bash
docker build -t 076977333390.dkr.ecr.eu-west-3.amazonaws.com/lambdamiax11:0.0.1 .
```

3. (opt) To test:
```bash
docker run  -p 8080:8080 076977333390.dkr.ecr.eu-west-3.amazonaws.com/lambdamiax11:0.0.1
```

4. Log docker into the aws registry (only one time)
```bash
aws ecr get-login-password | docker login --username AWS --password-stdin 076977333390.dkr.ecr.eu-west-3.amazonaws.com
```

5. Push the image
```bash
docker push 076977333390.dkr.ecr.eu-west-3.amazonaws.com/lambdamiax11:0.0.1
```
