# Nginx Server Terraform Module

This repository contains a Terraform module for deploying an Nginx server on AWS EC2.

## Structure

```
├── module/           # Reusable Terraform module
│   ├── main.tf      # Main module resources
│   ├── variable.tf  # Module input variables
│   └── output.tf    # Module outputs
└── example/         # Example usage of the module
    ├── main.tf      # Main configuration calling the module
    ├── variables.tf # Root-level variables
    ├── outputs.tf   # Root-level outputs
    └── terraform.tfvars.example # Example variables file
```

## Usage

### Method 1: Environment-Specific tfvars Files
### To test the code 
1. Navigate to the `example/` directory:
   ```bash
   cd example
   ```

2. Choose your deployment method:

   **Using PowerShell script (Windows):**
   ```powershell
   # Initialize terraform
   .\deploy.ps1 dev init
   
   # Plan deployment for development
   .\deploy.ps1 dev plan
   
   # Apply for development
   .\deploy.ps1 dev apply
   
   # For staging
   .\deploy.ps1 stg plan
   .\deploy.ps1 stg apply

   **Using Bash script (Linux/Mac):**
   ```bash
   # Make script executable
   chmod +x deploy.sh
   
   # Initialize terraform
   ./deploy.sh dev init
   
   # Plan and apply for different environments
   ./deploy.sh dev plan
   ./deploy.sh dev apply
   ./deploy.sh stg apply
   ./deploy.sh prod apply
   ```

   **Manual terraform commands:**
   ```bash
   # Initialize
   terraform init
   
   # Deploy to specific environment
   terraform plan -var-file="dev.tfvars"
   terraform apply -var-file="dev.tfvars"

### Method 2: Single tfvars File

1. Copy the example variables file and customize it:
   ```bash
   copy terraform.tfvars.example terraform.tfvars
   ```

2. Edit `terraform.tfvars` with your specific values and deploy:
   ```bash
   terraform init
   terraform plan
   terraform apply
   ```

## Environment-Specific Configurations

The repository includes pre-configured tfvars files for different environments:

| Environment | File | Instance Type | Security | Description |
|-------------|------|---------------|----------|-------------|
| **Development** | `dev.tfvars` | t2.micro | Less restrictive | Open access for development and testing |
| **Staging** | `stg.tfvars` | t3.small | Moderate restrictions | HTTPS enabled, limited SSH access |
| **Production** | `prod.tfvars` | t3.medium | Most restrictive | SSH only from bastion hosts |

## Module Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|----------|
| aws_region | AWS region to deploy resources | string | us-east-1 | no |
| env_name | Environment name (dev/prod) | string | n/a | yes |
| instance_type | EC2 Instance type | string | t2.micro | no |
| ami_id | AMI for EC2 instance | string | ami-0c02fb55956c7d316 | no |
| key_name | AWS Key Pair name | string | n/a | yes |
| ingress_rules | List of ingress rules for the security group | list(object) | HTTP(80) and SSH(22) from anywhere | no |

## Module Outputs

| Name | Description |
|------|-------------|
| instance_public_ip | Public IP of the Nginx server |
| website_url | Nginx Website URL |

## Security Group Rules

The module creates a security group with configurable ingress rules. By default:
- **Inbound**: HTTP (port 80) from anywhere (0.0.0.0/0)
- **Inbound**: SSH (port 22) from anywhere (0.0.0.0/0)
- **Outbound**: All traffic to anywhere