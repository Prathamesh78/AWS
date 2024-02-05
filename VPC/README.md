
# VPC

Launch Virtual Private Cloud in an AWS Region using CLI, Console and Boto3 SDK.

## Console

1. Open AWS Management Console, in search bar type VPC and click on it.
2. Choose Create VPC.
3. In VPC Settings, for Resources to create choose VPC and more
4. To generate Name tags for the VPC resources, leave Name tag auto-generation selected; otherwise, clear it to supply your own Name tags.
5. Enter the IPv4 address range for the VPC in the IPv4 CIDR block. An IPv4 address range is required for a VPC.
6. For a production environment, it is advised that you provision subnets in a minimum of two Availability Zones (AZs). Click Customize AZs and select the AZs you want for your subnets. 
7. Select the numbers for the number of public and private subnets in order to configure your subnets. 
8. Select the number of AZs in which to create NAT gateways if resources within a private subnet require access to the public internet via IPv4.
9. Leave the other Settings to default.
10. Select Create VPC once you have completed configuring your VPC.

## CLI

1. Create a VPC with the specified IPv4 CIDR block using the 'create-vpc' command
```bash
   aws ec2 create-vpc --cidr-block 10.0.0.0/24 --query Vpc.VpcId --output text
```
2. Create one or more subnets 
```bash
   aws ec2 create-subnet --vpc-id vpc-0b420648437c3a7be --cidr-block 10.0.1.0/24 --availability-zone us-east-1a --query Subnet.SubnetId --output text 
```
3. Create an internet gateway for public subnet for your web servers.
```bash
   aws ec2 create-internet-gateway --query InternetGateway.InternetGatewayId --output text
```
4. Attach the internet gateway to your VPC
```bash
   aws ec2 attach-internet-gateway --vpc-id vpc-0b420648437c3a7be --internet-gateway-id igw-01423a137b4c46a73
```
5. Create a custom route table for your public subnet by using the following create-route-table command.
```bash
   aws ec2 create-route-table --vpc-id vpc-0b420648437c3a7be --query RouteTable.RouteTableId --output text 
```
6. Create a route in the route table that sends all IPv4 traffic to the internet gateway with the following command
```bash
   aws ec2 create-route --route-table-id rtb-0b3e259885c36bb2d --destination-cidr-block 0.0.0.0/0 --gateway-id igw-01423a137b4c46a73
```
7. Associate the route table with the public subnet with the following command.
```bash
   aws ec2 associate-route-table --route-table-id rtb-0b3e259885c36bb2d --subnet-id subnet-0a45434e978f36ed1
```

## SDK Python for Boto3

To create a VPC with the above specific configuration, execute the python file using this command.
```bash
python vpc.py
```
