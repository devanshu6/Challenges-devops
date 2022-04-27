A 3-tier environment is a common setup, Use a tool of your choosing/familiarity create those resources

Tech Used: Terraform

Multiple terraform files are created:

vpc.tf -> This file will create VPC.

ec2.tf -> This file creates 2 compute instances and they both get data from startup-script.

igtw.tf -> This file creates internet gateway.

loadbalancer.tf -> The loadbalancer created here is of external type.Its of application type load balancer.
                   The aws_lb_target_group_attachment resource will attach our instances to the Target Group. Also it will listen requests on port 80.

rds.tf -> RDS is created in this file.

subnet.tf -> There are a total of 6 subnets for the front-end tier and back-end tier with a both public & private subnet.

route_table_public.tf -> This file has a new route table that is forwarding all the requests to the 0.0.0.0/0 CIDR block.
                         Also this route table is being attached with the Subnet created above so its acts as the public subnet.

web_sg.tf ->I have opened 80,443 & 22 ports for the inbound connection and I have opened all the ports for the outbound connection

database_sg.tf ->I have opened 3306 ports for the inbound connection and I have opened all the ports for the outbound connection.

outputs.tf -> In this file, I will be getting the DNS of the application load balancer.

vars.tf -> This file consists of variables used in the whole terraform code.

startup-script -> This will install an apache webserver in the EC2 instances.

terraform init is to initialize the working directory and downloading plugins of the provider
terraform plan is to create the execution plan for our code
terraform apply is to create the actual infrastructure. It will ask you to provide the Access Key and Secret Key in order to create the infrastructure.
So, instead of hardcoding the Access Key and Secret Key, it is better to apply at the run time.
![arch-diagram](https://user-images.githubusercontent.com/43514652/165508675-5a216f2e-bfe1-4467-9fbf-0877bf8ac037.png)
