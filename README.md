TASK- 1

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
| **Development** | `dev.tfvars` | Open access for development and testing |
| **Staging** | `stg.tfvars` | HTTPS enabled, limited SSH access |


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

-------------------------------------------------------------------------------------------------------------------------------------

Task-4 : Uploading files into s3 using boto3

# S3 File Upload Script
A Python script that uploads files to AWS S3 buckets with support for large files, error handling, and logging.
## Prerequisites

- Python 3.x
- AWS CLI installed and configured
- Required Python packages:
  ```bash
  pip install boto3
  ```

## AWS Configuration

1. Install AWS CLI
2. Configure your AWS credentials:
   ```bash
   aws configure
   ```
   You'll need to provide:
   - AWS Access Key ID
   - AWS Secret Access Key
   - Default region
   - Default output format

## Usage

Basic usage:
```bash
python s3-file-upload.py --file "path/to/your/file" --bucket "your-bucket-name"
```

### Command Line Arguments

- `--file`: (Required) Path to the file you want to upload
- `--bucket`: (Required) Name of the S3 bucket
- `--key`: (Optional) Custom name/path for the file in S3
- `--profile`: (Optional) AWS CLI profile to use (default: "default")

### Examples

1. Basic upload:
```bash
python s3-file-upload.py --file "./logs.txt" --bucket "assesment-logs"
```

2. Upload with custom name/path in S3:
```bash
python s3-file-upload.py --file "./logs.txt" --bucket "assesment-logs" --key "custom/path/file.log"
```

3. Using a different AWS profile:
```bash
python s3-file-upload.py --file "./logs.txt" --bucket "assesment-logs" --profile "default"
```

```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

