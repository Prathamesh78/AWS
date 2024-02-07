import boto3
from requests import get
from sys import platform
import os


ec2 = boto3.resource('ec2', aws_access_key_id='ACCESS-KEY-OF-THE-AWS-ACCOUNT',
                     aws_secret_access_key='SECRETE-KEY-OF-THE-AWS-ACCOUNT',
                     region_name='AWS-Region')


class awsInfrastructure(object):

    def __init__(self, **config):
        self.region = config.get('region')
        self.zone = config.get('zone')
        self.keyFileName = config.get('keyFileName')
        self.client = boto3.client('ec2', self.region)
        self.resource = boto3.resource('ec2', self.region)
        self.ip = get('https://api.ipify.org').text

        self.vpc = None
        self.igId = None
        self.routeTable = None
        self.subnet = None
        self.secGroup = None

    def createVpc(self, cidrBlock, vpcName):
        vpcInit = self.client.create_vpc(CidrBlock=cidrBlock)
        vpc = self.resource.Vpc(vpcInit["Vpc"]["VpcId"])
        vpc.create_tags(Tags=[{"Key": "Name", "Value": vpcName}])
        vpc.wait_until_available()
        self.vpc = vpc

    def createInternetGateway(self, igName):
        igInit = self.client.create_internet_gateway(
            TagSpecifications=[
                {'ResourceType': 'internet-gateway',
                    'Tags': [{"Key": "Name", "Value": igName}]}, ]
        )
        igId = igInit["InternetGateway"]["InternetGatewayId"]
        self.vpc.attach_internet_gateway(InternetGatewayId=igId)
        self.igId = igId

    def createRouteTable(self, rtName):
        routeTable = self.vpc.create_route_table()
        route = routeTable.create_route(
            DestinationCidrBlock='0.0.0.0/0',
            GatewayId=self.igId
        )
        routeTable.create_tags(Tags=[{"Key": "Name", "Value": rtName}])
        self.routeTable = routeTable

    def createSubnet(self, subnetCidr, snName):
        subnet = self.vpc.create_subnet(
            CidrBlock=subnetCidr, AvailabilityZone="{}{}".format(self.region, self.zone))
        subnet.create_tags(Tags=[{"Key": "Name", "Value": snName}])
        self.routeTable.associate_with_subnet(SubnetId=subnet.id)
        self.subnet = subnet

    def createSecurityGroup(self, sgName):
        secGroup = self.resource.create_security_group(
            GroupName=sgName, Description='EC2 Security Group', VpcId=self.vpc.id)

        secGroup.authorize_ingress(
            IpPermissions=[
                {
                    'FromPort': 22,
                    'IpProtocol': 'tcp',
                    'IpRanges': [
                        {
                            'CidrIp': '{}/0'.format(self.ip),
                            'Description': 'SSH Access'
                        },
                    ],
                    'ToPort': 22,

                },
            ]
        )

        secGroup.create_tags(Tags=[{"Key": "Name", "Value": sgName}])
        self.secGroup = secGroup

    def createKeyPair(self):
        keyPair = self.client.create_key_pair(KeyName=self.keyFileName)
        privateKeyFile = open('{}.pem'.format(self.keyFileName), "w")
        privateKeyFile.write(dict(keyPair)['KeyMaterial'])
        privateKeyFile.close
        if platform == "linux" or platform == "linux2":
            os.chmod('{}.pem'.format(self.keyFileName), 0o400)

    def createEc2Instance(self, ami, instanceType, ec2Name):
        ec2Instances = self.resource.create_instances(
            ImageId=ami, InstanceType=instanceType, MaxCount=1, MinCount=1,
            NetworkInterfaces=[{'SubnetId': self.subnet.id, 'DeviceIndex': 0,
                                'AssociatePublicIpAddress': True, 'Groups': [self.secGroup.group_id]}],
            KeyName=self.keyFileName)
        instance = ec2Instances[0]
        instance.create_tags(
            Tags=[{"Key": "Name", "Value": ec2Name}])
        instance.wait_until_running()
        print('Instance Id: ', instance.id)
        print('Connect Ec2 instance with the following SSH command once initializing process gets completed.')
        print('Check AWS console for current status.')
        print('ssh -i "{}.pem" {}@{}'.format(self.keyFileName,
              'ec2-user', instance.public_ip_address))
        return instance


if __name__ == "__main__":

    infra = awsInfrastructure(
        region='us-east-1', zone='a', keyFileName='infraSecrets')
    infra.createVpc(cidrBlock='192.168.1.0/24', vpcName='ec2-vpc')
    infra.createInternetGateway(igName='ec2-ig')
    infra.createRouteTable(rtName='ec2-rt')
    infra.createSubnet(subnetCidr='192.168.1.0/24', snName='ec2-sn')
    infra.createSecurityGroup(sgName='ec2-sg')
    infra.createKeyPair()
    infra.createEc2Instance(ami='ami-048f6ed62451373d9',
                            instanceType='t2.micro', ec2Name='ec2-infra-instance')