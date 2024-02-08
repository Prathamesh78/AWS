
# Application Load Balancer

Create an Application Load Balancer, attach target groups and distribute the load accross them. Use Console, CLI and SDK to Create ALB

## About ALB
A load balancer takes requests from clients and distributes them across targets in a target group.
## Console

1. Launch 2 EC2 instance in an AWS Region
2. In navigation panel of EC2 select Target Groups and choose create Target Groups
3. For Choose a target type, select Instances to specify targets by instance ID or IP addresses to specify targets by only IP address.
4. For Target group name, enter a name for the target group.
5. Modify the Port to HTTP and Protocol to 80 as needed
6. Then Register the targets, in Register targets you can add one or more instances
7. Choose create target group
8. Choose create Load Balancer, Under Application Load Balancer choose create
9. Give name for your Load Balancer
10. For Security Group, use existing Security Group or create a new one.
11. For Listeners and routing, the default listener accepts HTTP traffic on port 80. You can keep the default protocol and port, or choose different ones. For Default action, choose the target group that you created.
12. Review and create Load Balancer.

## CLI

Prerequisits: Two EC2 instances, Security Group and VPC with multiple subnets

1. Use the create-load-balancer command to create a load balancer. You must specify two subnets that are not from the same Availability Zone.
```bash
aws elbv2 create-load-balancer --name my-load-balancer  \
--subnets subnet-0e3f5cac72EXAMPLE subnet-081ec835f3EXAMPLE --security-groups sg-07e8ffd50fEXAMPLE
```
2. Use the create-target-group command to create a target group, specifying the same VPC that you used for your EC2 instances. 
```bash
aws elbv2 create-target-group --name my-targets --protocol HTTP --port 80 --vpc-id vpc-0598c7d356EXAMPLE --ip-address-type [ipv4]
```
3. Use the register-targets command to register your instances with your target group
```bash
aws elbv2 register-targets --target-group-arn targetgroup-arn --targets Id=i-0abcdef1234567890 Id=i-1234567890abcdef0
```
4. Use the create-listener command to create a listener for your load balancer with a default rule that forwards requests to your target group
```bash
aws elbv2 create-listener --load-balancer-arn loadbalancer-arn --protocol HTTP --port 80 --default-actions Type=forward,TargetGroupArn=targetgroup-arn
```
5. Verify Health of registered target group use the following command
```bash
aws elbv2 describe-target-health --target-group-arn targetgroup-arn
```

## SDK for Python
To create a ALB with the above specific configuration, execute the python file using this command. Change the access key, secret access key and aws region.
```bash
    python ALB.py
```
