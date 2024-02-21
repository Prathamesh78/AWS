import boto3
import json
import base64

# Initialize AWS clients
lambda_client = boto3.client('lambda')
iam_client = boto3.client('iam')

# Invoke Lambda function and get logs
def invoke_lambda_function(function_name):
    response = lambda_client.invoke(
        FunctionName=function_name,
        LogType='Tail'
    )

    # Decode and print logs
    log_result = base64.b64decode(response['LogResult']).decode('utf-8')
    print("Lambda Function Logs:")
    print(log_result)

if __name__ == "__main__":
    # Parameters
    role_name = 'lambda-shankar'
    function_name = 'my-function'
    handler = 'index.handler'
    runtime = 'nodejs20.x'
    zip_file_path = r'C:\Users\rohan\boto\function.zip'

    # Invoke Lambda function and get logs
    invoke_lambda_function(function_name)