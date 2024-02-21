import boto3
import json
import base64
import time

# Initialize AWS clients
lambda_client = boto3.client('lambda')
iam_client = boto3.client('iam')

# Create execution role
def create_execution_role(role_name):
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {"Service": "lambda.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }]
    }

    response = iam_client.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(trust_policy)
    )

    print("Waiting for IAM role to propagate...")
    time.sleep(10)  # Wait for 10 seconds

    # Attach AWSLambdaBasicExecutionRole policy
    try:
        iam_client.attach_role_policy(
            RoleName=role_name,
            PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
        )
    except Exception as e:
        print(f"Error attaching policy to IAM role: {e}")

    return response['Role']['Arn']

# Create Lambda function
def create_lambda_function(function_name, role_arn, handler, runtime, zip_file):
    response = lambda_client.create_function(
        FunctionName=function_name,
        Runtime=runtime,
        Role=role_arn,
        Handler=handler,
        Code={'ZipFile': zip_file}
    )

    return response['FunctionArn']

if __name__ == "__main__":
    # Parameters
    role_name = 'lambda-shankar'
    function_name = 'my-function'
    handler = 'index.handler'
    runtime = 'nodejs20.x'
    zip_file_path = r'C:\Users\rohan\boto\function.zip'

    # Create execution role
    role_arn = create_execution_role(role_name)
    print(f"Execution Role '{role_name}' created with ARN: {role_arn}")

    # Create Lambda function
    with open(zip_file_path, 'rb') as f:
        zip_file = f.read()
    function_arn = create_lambda_function(function_name, role_arn, handler, runtime, zip_file)
    print(f"Lambda function '{function_name}' created with ARN: {function_arn}")
