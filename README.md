🌦️ Weather Data Collection System

A complete DevOps‑oriented project that fetches real‑time weather data for multiple cities using the OpenWeather API, stores it in AWS S3,
and provides automated provisioning using Terraform, testing via pytest, and CI automation through GitHub Actions.
 
This README is designed to be submission‑ready, covering features, architecture, requirements, setup, deployment, and GitHub usage.

📌 Features
Fetches real-time weather data (temperature, humidity, conditions).
Supports multiple cities via an environment variable.
Stores results as timestamped JSON files in AWS S3.
Uses Infrastructure as Code (Terraform) for S3 + IAM provisioning.
Includes automated tests using pytest.
GitHub Actions CI pipeline for:
Dependency installation
Test execution
Optional weather‑fetch execution (manual trigger)
Clean project structure with reusable modules.
Secure configuration using .env and GitHub Secrets.

🏗️ Architecture
flowchart LR
  A[Scheduler / Manual Run] --> B[Python Weather Collector]
  B -->|Fetch API| C[OpenWeather API]
  B -->|Generate JSON| D[Local Processing]
  D -->|Upload| E[S3 Bucket]

  subgraph AWS
    E[S3 Bucket]:::aws
  end

classDef aws fill:#fff3b0,stroke:#333,stroke-width:1px;
Components
main.py → Orchestrates fetching and uploading
weather_fetcher.py → Communicates with OpenWeather API
s3_uploader.py → Uploads JSON to AWS S3
Terraform → Sets up S3 bucket, IAM, versioning & lifecycle
GitHub Actions → Testing + optional scheduled fetches

📦 Requirements
Languages & Tools
Python 3.10+
AWS CLI configured (or access keys in .env)
Terraform v1.x
Git
Python Packages (requirements.txt)
requests
boto3
python-dotenv
pytest
Cloud Requirements
AWS account with:
S3 access
IAM permissions for Terraform

⚙️ How to Run (Local)

1️⃣ Clone the Repo
git clone https://github.com/<your-username>/weather-data-collection-system.git
cd weather-data-collection-system

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate         # Linux / Mac
venv\Scripts\activate            # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables
Create .env file:

OPENWEATHER_API_KEY=your_api_key
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_REGION=us-east-1
S3_BUCKET_NAME=weather-bucket-demo
CITIES=London,New York,Tokyo

5️⃣ Run the Program
python main.py
✔️ Outputs should show successful fetches and uploads to S3.

🚀 How to Deploy
Option 1: Deploy via Terraform (Recommended)

1️⃣ Initialize Terraform
cd terraform
terraform init

2️⃣ Preview Infrastructure
terraform plan

3️⃣ Apply Changes
terraform apply
Terraform provisions:
S3 bucket
IAM user
IAM access keys
Access policies

4️⃣ Add AWS Keys to .env or GitHub Secrets
Use the generated IAM keys from Terraform.
Option 2: Deploy as AWS Lambda (Optional Upgrade)
You can convert main.py into a Lambda handler and schedule it using EventBridge.
(Ask me if you want this — I can generate the Lambda version for you.)
🔄 GitHub Instructions

1️⃣ Initialize Repo
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/weather-data-collection-system.git
git push -u origin main

2️⃣ Add GitHub Secrets
In GitHub → Settings → Secrets → Actions, add:
OPENWEATHER_API_KEY
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
S3_BUCKET_NAME

3️⃣ CI Workflow (Already Included)
Every push triggers:
Python setup
Dependency install
Tests
You can manually run weather-collection from GitHub Actions under the workflow_dispatch job.

🧪 Testing
Run tests using:
pytest

Expected:
All tests pass
No failures

📁 Project Structure
weather-data-collection-system/
├── main.py
├── weather_fetcher.py
├── s3_uploader.py
├── utils.py
├── terraform/
├── tests/
├── .github/workflows/ci.yml
├── .env.example
├── requirements.txt
└── README.md

🎯 Conclusion
If the following work, the project is fully complete:
Weather fetching works
S3 uploads succeed
Terraform deploys infra
Tests pass locally and in GitHub Actions
README looks complete and professional
This README is submission‑ready and adheres to DevOps project standards.
If you want, I can:
Review your GitHub repo
Improve your README styling
Generate images/diagrams for architecture
Provide Lambda-ready code
