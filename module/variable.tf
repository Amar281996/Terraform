variable "aws_region" {
  description = "AWS region to deploy resources"
  default     = "us-east-1"
}

variable "env_name" {
  description = "Environment name"
  type        = any
}

variable "instance_type" {
  description = "EC2 Instance type"
  default     = "t2.micro"
}

variable "ami_id" {
  description = "AMI for EC2 instance"
  default     = "ami-0c02fb55956c7d316"
}

variable "key_name" {
  description = "AWS Key Pair name"
  type        = string
}

variable "ingress_rules" {
  description = "List of ingress rules for the security group"
  type = any
}

variable "egress_rules" {
  description = "List of egress rules for the security group"
  type = any
}
