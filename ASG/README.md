
# Auto Scaling Groups

Create an AutoScaling Group using Console, CLI and SDK with instance size minimum 1, desired capacity 2 and maximum 5.

## About ASG 
An Amazon EC2 Auto Scaling group (ASG) contains a collection of EC2 instances that share similar characteristics and are treated as a logical grouping for the purposes of fleet management and dynamic scaling
## Console

1. Create your Launch Template
2. Specify the Amazon Machine Image (AMI) from which to launch the instances.
3. Choose an instance type that is compatible with the AMI that you specify.
4. Specify the key pair to use when connecting to instances, for example, using SSH.
5. Add one or more security groups to allow network access to the instances.
6. Specify whether to attach additional volumes to each instance.
7. Add custom tags (key-value pairs) to the instances and volumes.
8. Open Auto Scaling Groups and choose create an Auto Scaling Groups
9. Choose Launch Template, Enter name for Auto Scaling Group and Choose the template which we have created
10. Under Network, for VPC, choose a VPC. The Auto Scaling group must be created in the same VPC as the security group you specified in your launch template.
11. For Availability Zones and subnets, choose one or more subnets in the specified VPC. Use subnets in multiple Availability Zones for high availability.
12. To register your Amazon EC2 instances with a load balancer, choose an existing load balancer or create a new one. 
13. On the Configure group size and scaling policies page, choose minimum capacity 1, desired capacity 2 and maximum capacity 5.
14. Review and Create Auto Scaling Group.

## CLI 
Create an Auto Scaling Group using the following command
```bash
aws autoscaling create-auto-scaling-group \
    --auto-scaling-group-name my-asg \
    --launch-template LaunchTemplateId=lt-1234567890abcde12 \
    --target-group-arns arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/943f017f100becff \
    --health-check-type ELB \
    --health-check-grace-period 600 \
    --min-size 1 \
    --max-size 5 \
    --desired-capacity 2\
    --vpc-zone-identifier "subnet-5ea0c127,subnet-6194ea3b,subnet-c934b782"
```






