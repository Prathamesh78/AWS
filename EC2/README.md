
# EC2

Launch an EC2 instance in a VPC and attach a Security Group to it by using Console, CLI and SDK.

## About EC2
Elastic Compute Cloud (Amazon EC2) in the Amazon Web Services (AWS) Cloud offers scalable, on-demand computing power. You can develop and launch apps more quickly by using Amazon EC2 to lower hardware costs. Using Amazon EC2, you can set up networking and security, start as many or as few virtual servers as you need, and control storage.


## Console

1. Open Amazon EC2 and choose Launch instance
2. Under Name and tags, for Name, enter AWS-EC2 Instance name for your instance.
3. Under Application and OS Images (Amazon Machine Image), choose Quick Start and then choose Ubuntu 20.04.
4. In Amazon Machine Image (AMI) choose a free tier version.
5. Under Instance type, from the Instance type list, you can select the hardware configuration for your instance. Choose the t2.micro instance type, which is selected by default.
6. In Key pairs, choose Create new key pair and generate a new key pair.
7. In Network settings, you can create a new security group or attach existing security group.
8. To connect from SSH, choose allow SSH traffic from anywhere
9. Rest of the settings should be remain at default
10. Review the configuration and launch the instance.
11. You can connect to EC2 instance using SSH or from EC2 connect.

## CLI

1. Launch an ec2 instance by typing the command in cli. The requirements for launching instance
are AMI, Instance-type, Key pairs, security groups and Subnets.
```bash
aws ec2 run-instances --image-id ami-xxxxxxxx --count 1 --instance-type t2.micro --key-name MyKeyPair --security-group-ids sg-903004f8 --subnet-id subnet-6e7f829e
```
2. Connect to EC2 instance using SSH
```bash
ssh -i key-pair.pem  ec2-user@58.4.243
87
```
3. Terminate the instance
```bash
aws ec2 terminate-instances --instance-ids i-5203422c
```

## SDK for Python
To create a EC2 with the specific configuration, execute the python file using this command. Change the access key, secret access key and aws region.
```bash
python EC2.py
```


