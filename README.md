# IAM Policies CSV Script
### Kevin Goznalez

# IAM Policy Printer

The IAM Policy Printer is a Python script that interacts with AWS Identity and Access Management (IAM) using Boto3 to list IAM policies and save the results to a CSV file.

## Usage

1. Run the script using Python.
2. The script will connect to your AWS account using the IAM client.
3. It will list all IAM policies available in your AWS account.
4. The relevant policy information, including Policy Name, Policy ID, and ARN, will be extracted.
5. The results will be written to a CSV file named `IAM_Policies.csv`.

## Requirements

- Python
- Boto3 library (You can install it using `pip install boto3`)
### Note

Make sure to configure your AWS credentials before running the script to ensure access to your IAM policies.
