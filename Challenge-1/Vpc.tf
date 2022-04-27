# Creating VPC
resource "aws_vpc" "myvpc" {
cidr_block       = "${var.vpc_cidr}"
instance_tenancy = "default"

  tags = {
    Name = "My VPC"
  }
}
