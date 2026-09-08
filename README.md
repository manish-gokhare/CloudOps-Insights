Cloud Cost & Infrastructure Monitor

Absolutely. Here's a README tailored to the **current state** of your project: Python + Flask + Pandas + Matplotlib, Docker, Ruff, pytest/coverage, GitHub Actions, AWS ECR, and EC2 deployment.

# CloudOps Insight

## Cloud Cost & Infrastructure Monitor

CloudOps Insight is a lightweight Python-based cloud cost monitoring application that reads cloud cost data from a CSV file, analyzes the data using Pandas, generates a cost visualization using Matplotlib, and displays the results through a Flask web dashboard.

The application is containerized with Docker and integrated with GitHub Actions for automated CI/CD. Docker images are published to Amazon ECR and deployed to an Amazon EC2 instance.

---

## Architecture

```text
                         Developer
                             |
                             | git push
                             v
                    +------------------+
                    |     GitHub       |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    | GitHub Actions   |
                    |                  |
                    | Ruff             |
                    | Pytest           |
                    | Coverage         |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    |  Docker Build    |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    |    AWS ECR       |
                    |                  |
                    | cloudops-insight |
                    |    :<git-sha>    |
                    +--------+---------+
                             |
                             | SSH
                             v
                    +------------------+
                    |   EC2 Instance   |
                    |                  |
                    | Docker Container |
                    | CloudOps Insight |
                    +--------+---------+
                             |
                             | HTTP :5000
                             v
                         Web Browser
```

---

## Application Flow

```text
cloud_cost.csv
      |
      v
    Pandas
      |
      +------------------+
      |                  |
      v                  v
Total Cost        Cost by Service
                         |
                         v
                    Matplotlib
                         |
                         v
                  cost_chart.png
                         |
                         v
                      Flask
                         |
                         v
                   Web Dashboard
```

---

## Features

* Read cloud cost data from CSV
* Calculate total cloud cost
* Calculate cost by cloud service
* Calculate cost by environment
* Generate a Matplotlib bar chart
* Display results through a Flask web dashboard
* Automated code linting with Ruff
* Automated formatting validation with Ruff
* Automated testing with pytest
* Code coverage enforcement
* Dockerized application
* Automated Docker image build
* Push Docker image to Amazon ECR
* Automated deployment to Amazon EC2
* Git commit SHA based Docker image versioning

---

## Technology Stack

| Area                 | Technology     |
| -------------------- | -------------- |
| Programming Language | Python 3.12    |
| Web Framework        | Flask          |
| Data Analysis        | Pandas         |
| Visualization        | Matplotlib     |
| Testing              | pytest         |
| Coverage             | pytest-cov     |
| Code Quality         | Ruff           |
| Containerization     | Docker         |
| CI/CD                | GitHub Actions |
| Container Registry   | AWS ECR        |
| Compute              | AWS EC2        |
| Authentication       | AWS IAM        |
| Source Control       | Git / GitHub   |

---

## Project Structure

```text
CloudOps-Insights/
│
├── app/
│   ├── __init__.py
│   ├── analytics.py
│   └── routes.py
│
├── data/
│   └── cloud_cost.csv
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── charts/
│       └── cost_chart.png
│
├── templates/
│   └── index.html
│
├── tests/
│   ├── test_analytics.py
│   └── test_routes.py
│
├── run.py
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

---

# Local Development

## Prerequisites

Install:

* Python 3.12
* Docker
* Git

---

## Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd CloudOps-Insights
```

---

## Create Virtual Environment

```bash
python3 -m venv .venv
```

Activate it:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

---

## Install Dependencies

Application dependencies:

```bash
pip install -r requirements.txt
```


# Run the Application Locally

```bash
python run.py
```

The Flask application runs on:

```text
http://localhost:5000
```

Open the URL in a browser to view the CloudOps Insight dashboard.

If port `5000` is already being used locally, you can temporarily change the Flask port in `run.py`.

---

# Testing

Run the complete test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest \
  --cov=app \
  --cov-report=term-missing
```

The CI pipeline enforces a minimum coverage threshold:

```bash
pytest \
  --cov=app \
  --cov-report=term-missing \
  --cov-report=xml \
  --cov-fail-under=80
```

---

# Code Quality

## Ruff Lint

```bash
ruff check .
```

## Ruff Format

Format the source code:

```bash
ruff format .
```

Verify formatting without modifying files:

```bash
ruff format --check .
```

The CI pipeline uses:

```bash
ruff check .
ruff format --check .
```

---

# Docker

## Build the Docker Image

```bash
docker build \
  -t cloudops-insight:1.0 \
  .
```

Verify:

```bash
docker images
```

---

## Run the Docker Container

The Flask application listens on port `5000` inside the container.

Run:

```bash
docker run \
  --name cloudops-insight \
  -p 5001:5000 \
  cloudops-insight:1.0
```

Open:

```text
http://localhost:5001
```

The mapping is:

```text
Host:      5001
Container: 5000
```

---

# AWS ECR

The application image is published to Amazon Elastic Container Registry.

### AWS Configuration

```text
AWS Account: 195231312458
AWS Region:  eu-west-1
ECR Repository: cloudops-insight
```

ECR repository:

```text
195231312458.dkr.ecr.eu-west-1.amazonaws.com/cloudops-insight
```

---

## Authenticate Docker with ECR

```bash
aws ecr get-login-password \
  --region eu-west-1 \
| docker login \
  --username AWS \
  --password-stdin \
  195231312458.dkr.ecr.eu-west-1.amazonaws.com
```

---

## Tag the Docker Image

```bash
docker tag cloudops-insight:1.0 \
195231312458.dkr.ecr.eu-west-1.amazonaws.com/cloudops-insight:1.0
```

---

## Push the Image

```bash
docker push \
195231312458.dkr.ecr.eu-west-1.amazonaws.com/cloudops-insight:1.0
```

---

# Image Versioning

GitHub Actions uses the Git commit SHA to version Docker images.

For example:

```text
Git commit:

af308df55ffb9f0d4935c93ba5f05935db33f222
```

The CI pipeline generates the short tag:

```text
af308df
```

The resulting ECR image becomes:

```text
195231312458.dkr.ecr.eu-west-1.amazonaws.com/cloudops-insight:af308df
```

Using a Git-based image tag provides traceability between:

```text
Git Commit
     |
     v
Docker Image
     |
     v
ECR
     |
     v
EC2 Deployment
```

It also allows a previous image version to be deployed for rollback.

---

# GitHub Actions CI/CD

The project uses GitHub Actions to automate the software delivery process.

## CI Pipeline

Pull requests and development changes run the quality checks:

```text
Checkout
   |
   v
Setup Python
   |
   v
Install Dependencies
   |
   v
Ruff Lint
   |
   v
Ruff Format Check
   |
   v
Pytest
   |
   v
Coverage
```

Only after the quality gates pass does the `main` branch continue to Docker build and ECR publishing.

---

## CD Pipeline

Changes merged into `main` trigger the deployment pipeline:

```text
Git Push to main
       |
       v
CI Quality Gates
       |
       v
Docker Build
       |
       v
ECR Push
       |
       v
SSH to EC2
       |
       v
ECR Authentication
       |
       v
Docker Pull
       |
       v
Stop Existing Container
       |
       v
Start New Container
       |
       v
CloudOps Insight
```

---

# Git Branching Strategy

The project uses a simple development workflow:

```text
feature/*
    |
    v
develop
    |
    | Pull Request
    v
main
    |
    v
Build + Push + Deploy
```

### `feature/*`

Used for individual development tasks.

### `develop`

Used for integration and CI validation.

### `main`

Contains production-ready code.

Only pushes to `main` publish the Docker image to ECR and trigger EC2 deployment.

---

# GitHub Actions Configuration

The workflow is located at:

```text
.github/workflows/ci.yml
```

The workflow performs:

* Ruff linting
* Ruff formatting validation
* pytest
* Code coverage
* Docker image build
* ECR authentication
* ECR image push
* EC2 deployment

---

# GitHub Configuration

The following GitHub repository variables are used:

```text
EC2_HOST
EC2_USER
```

Example:

```text
EC2_HOST = <EC2_PUBLIC_IP>
EC2_USER = ubuntu
```

Sensitive values are stored as GitHub Secrets:

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
EC2_SSH_KEY
```

AWS credentials are used by GitHub Actions to publish the Docker image to ECR.

The EC2 instance uses an IAM role with ECR read permissions to pull the image.

---

# EC2 Configuration

The EC2 instance requires:

* Docker
* AWS CLI
* Network access to AWS ECR
* An IAM role with ECR read permissions
* Security Group access for the application port

Recommended IAM permission for the EC2 instance:

```text
AmazonEC2ContainerRegistryReadOnly
```

The EC2 instance does not need the application source code.

It pulls the pre-built Docker image directly from ECR.

---

# EC2 Deployment

The deployment process pulls the exact image generated by the GitHub commit.

Example:

```bash
docker pull \
195231312458.dkr.ecr.eu-west-1.amazonaws.com/cloudops-insight:af308df
```

The existing container is stopped and replaced with the new version:

```bash
docker stop cloudops-insight || true

docker rm cloudops-insight || true

docker run -d \
  --name cloudops-insight \
  --restart unless-stopped \
  -p 5000:5000 \
  195231312458.dkr.ecr.eu-west-1.amazonaws.com/cloudops-insight:af308df
```

---

# Access the Application

After deployment, the application is available on the EC2 instance at:

```text
http://<EC2_PUBLIC_IP>:5000
```

Ensure the EC2 Security Group allows inbound TCP traffic on port `5000`.

For production deployment, a reverse proxy such as Nginx or an AWS Application Load Balancer can be placed in front of the Flask application.

---

# CI/CD Security Model

The project separates AWS permissions between GitHub Actions and EC2.

```text
GitHub Actions
      |
      | AWS credentials
      | ECR push
      v
     ECR
      ^
      |
      | EC2 IAM Role
      | ECR read
      |
     EC2
```

GitHub Actions requires permission to push images.

EC2 only requires permission to pull images.

This follows the principle of granting each component only the permissions required for its task.

---

# Future Enhancements

The current project focuses on the core CI/CD pipeline.

Planned improvements include:

* SonarQube code quality analysis
* Trivy Docker image vulnerability scanning
* GitHub Actions OIDC authentication with AWS
* Replace SSH deployment with AWS Systems Manager
* Nginx reverse proxy
* HTTPS
* AWS Application Load Balancer
* Prometheus monitoring
* Grafana dashboards
* CloudWatch integration
* Automated rollback
* Infrastructure as Code using Terraform
* Kubernetes deployment

Future target architecture:

```text
                         GitHub
                            |
                            v
                    GitHub Actions
                            |
             +--------------+--------------+
             |              |              |
            Ruff         SonarQube       Pytest
             |              |              |
             +--------------+--------------+
                            |
                            v
                       Docker Build
                            |
                            v
                         Trivy
                            |
                            v
                           ECR
                            |
                            v
                           EC2
                            |
                    +-------+-------+
                    |               |
                 Flask          Prometheus
                    |               |
                    v               v
                 Browser          Grafana
```

---

# DevOps Skills Demonstrated

This project demonstrates an end-to-end containerized DevOps workflow:

```text
Python Application
        ↓
Git
        ↓
GitHub
        ↓
GitHub Actions
        ↓
Code Quality
        ↓
Automated Testing
        ↓
Code Coverage
        ↓
Docker
        ↓
Security Scanning
        ↓
Amazon ECR
        ↓
Amazon EC2
        ↓
Production Application
```

Key DevOps practices demonstrated:

* Source control
* Branch-based development
* CI automation
* Automated testing
* Code quality gates
* Code coverage
* Containerization
* Container image versioning
* Container registry
* AWS IAM
* Automated deployment
* Infrastructure deployment
* Production-style rollback capability

---

## Project Goal

The goal of CloudOps Insight is to demonstrate how a simple Python application can be transformed into a **containerized, tested, quality-controlled, security-scanned, and automatically deployed cloud application** using modern DevOps practices.

> **Build once, test once, package once, and deploy the same Docker image across environments.**

This README reflects the **current working architecture** without pretending that SonarQube, Trivy, OIDC, Prometheus, or Grafana are already implemented. Those are clearly marked as future enhancements.
