
# Security Groups

Create a Security Group in a VPC using console, CLI and SDK. Also add rules to it.

## About Security Groups
A security group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic. Inbound rules control the incoming traffic to your instance, and outbound rules control the outgoing traffic from your instance.

## Console

1. Open EC2 console and in navigation tab choose security groups
2. Choose Create security groups
3. In Basic details, give any name to your security group 
4. Choose the vpc, for which your security groups need to be specified
5. To allow the inbound SSH traffic, Choose Protocol 'TCP', Port Range '22' and source from Anywhere 
6. To allow the outbound All traffic, Choose type All Traffic, Protocol All, Port Range All and Destination Custom
7. Choose Create security group.

## CLI

1. Create a security group for a specified VPC using the following command
```bash
   aws ec2 create-security-group --group-name my-sg --description "My security group" --vpc-id vpc-063428be3278e1579
```
2. Following command adds a rule that allows inbound traffic on TCP port 22 (SSH).
```bash
aws ec2 authorize-security-group-ingress --group-id sg-0e15c7f6ba5e0748d --protocol tcp --port 22 --cidr 49.14.82.241/32
```
3. Add a rule that allows outbound traffic on all ports
```bash
aws ec2 authorize-security-group-egress --group-id sg-0e15c7f6ba5e0748d --ip-permissions IpProtocol=All,FromPort=All,ToPort=All,IpRanges='[{CidrIp=10.0.0.0/16}]'
```

## SDK Python
To create a security groups for a specified VPC, execute the python file using this command. Change the access key, secret access key and aws region.
```bash
    python Security_groups.py
```

