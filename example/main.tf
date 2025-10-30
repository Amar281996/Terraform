terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

module "nginx_server" {
  source = "../module"

  aws_region    = var.aws_region
  env_name      = var.env_name
  instance_type = var.instance_type
  ami_id        = var.ami_id
  key_name      = var.key_name
  ingress_rules = var.ingress_rules
  egress_rules  = var.egress_rules
}