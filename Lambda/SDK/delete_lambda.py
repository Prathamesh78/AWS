import boto3
import json
import base64

# Initialize AWS clients
lambda_client = boto3.client('lambda')
iam_client = boto3.client('iam')


# Delete Lambda function
def delete_lambda_function(function_name):
    lambda_client.delete_function(FunctionName=function_name)
    print(f"Lambda function '{function_name}' deleted.")

if __name__ == "__main__":
    # Parameters
    role_name = 'lambda-shankar'
    function_name = 'my-function'
    handler = 'index.handler'
    runtime = 'nodejs20.x'
    zip_file_path = r'C:\Users\rohan\boto\function.zip'

    # Delete Lambda function
    delete_lambda_function(function_name)
