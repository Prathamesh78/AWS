# AWS Lambda using CLI Quick Start Guide

This guide provides step-by-step instructions on how to create an AWS Lambda function using the AWS CLI.

## Prerequisites

Before you begin, make sure you have the following:

- AWS CLI installed and configured with appropriate permissions.
- Basic understanding of AWS Lambda.

## Step 1: Create Execution Role

Use the following commands to create an execution role for your Lambda function:
```bash
aws iam create-role --role-name lambda-ex --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'
```

Then attach the AWSLambdaBasicExecutionRole managed policy:
```bash
aws iam attach-role-policy --role-name lambda-ex --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

## Step 2: Create the Function

Create a file named index.js and copy the provided sample code:
```bash
exports.handler = async function(event, context) {
  console.log("ENVIRONMENT VARIABLES\n" + JSON.stringify(process.env, null, 2))
  console.log("EVENT\n" + JSON.stringify(event, null, 2))
  return context.logStreamName
}
```

Create a deployment package:
```bash
zip function.zip index.js
```

Use the create-function command to create the Lambda function:
```bash
aws lambda create-function --function-name my-function \
--zip-file fileb://function.zip --handler index.handler --runtime nodejs20.x \
--role arn:aws:iam::123456789012:role/lambda-ex
```

## Step 3: Invoke the Function

To get logs for an invocation from the command line, use the 'invoke' command with the '--log-type' option:
```bash
aws lambda invoke --function-name my-function out --log-type Tail
```

You can use the base64 utility to decode the logs:
```bash
aws lambda invoke --function-name my-function out --log-type Tail \
--query 'LogResult' --output text |  base64 -d
```

## Step 4: Clean Up

To delete the Lambda function, run the following command:
```bash
aws lambda delete-function --function-name my-function
```

Conclusion

Congratulations! You've successfully created, invoked, and cleaned up an AWS Lambda function using the AWS CLI.
