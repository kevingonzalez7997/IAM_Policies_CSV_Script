import csv
import boto3
import time
import os.path
print("Hello and Welcome to IAM Policy Printer\n")
time.sleep(2)
print("All IAM policies will be returned and filter\n")
time.sleep(2)
print("The results will be written in IAM_Policies.csv\n")
# Create an AWS Identity and Access Management (IAM) client using Boto3
client = boto3.client('iam')
# Define the function
def policies_list():
    # Request the policies
    # If parameters are not included, all policies will be returned
    response = client.list_policies()
    # Create a CSV file where the results will be written
    csv_filename = 'IAM_Policies.csv'
    # Initialize an empty list to store policy data
    policies_filtered = []

    # Collect policy information
    for policy in response['Policies']:
       # For every policy in the returned dictionary 
       # Append the nth list item, with the following key names
        policies_filtered.append({
            "Policy_Name": policy['PolicyName'],
            "PolicyId": policy['PolicyId'],
            "Arn": policy['Arn']
        })
    # Write the results to the CSV file
    # Open the CSV file, set this command to csv_file
    with open(csv_filename, 'w', newline='') as csv_file:
       #Use DictWriter as results have been stored in a dictionary 
        writer = csv.DictWriter(csv_file, fieldnames=['Policy_Name', 'PolicyId', 'Arn'], extrasaction='ignore')
        # Creates a header with field names
        writer.writeheader()
        # Writes each dictionary as a row
        writer.writerows(policies_filtered)
# Run Function
policies_list()
# Creates a variable for the path of the CSV file
path = './IAM_Policies.csv'
# Check if the file has been created
check_file = os.path.exists(path)
# If statement depending on the result
if check_file == True:
       time.sleep(2)
       print("Everything went smoothly, you should see the IAM_Policies.csv")
else:
       time.sleep(2)
       print("Error try again")
