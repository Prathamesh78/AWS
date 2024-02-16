import boto3

# IAM User Credentials
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
region_name = 'YOUR_REGION_NAME'

# Create EC2 client
ec2_client = boto3.client(
    'ec2',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# VPC ID
vpc_id = 'YOUR_VPC_ID'

# Security Group ID
security_group_id = 'YOUR_SECURITY_GROUP_ID'

# Key Pair Name
key_pair_name = 'YOUR_KEY_PAIR_NAME'

# AMI ID
ami_id = 'YOUR_AMI_ID'

# Instance Type
instance_type = 't2.micro'

# Subnet ID (Optional, you may want to specify a subnet within your VPC)
subnet_id = 'YOUR_SUBNET_ID'

# Create EC2 instance
response = ec2_client.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    MinCount=1,
    MaxCount=1,
    KeyName=key_pair_name,
    SecurityGroupIds=[security_group_id],
    SubnetId=subnet_id,
    # Uncomment the line below if you want to specify a different IAM role
    # IamInstanceProfile={'Name': 'YOUR_IAM_INSTANCE_PROFILE_NAME'},
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'MyEC2Instance'
                }
            ]
        }
    ]
)

# Print instance ID
print("Instance ID:", response['Instances'][0]['InstanceId'])
