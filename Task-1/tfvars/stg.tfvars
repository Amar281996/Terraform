# Staging Environment Configuration
aws_region    = "us-east-1"
env_name      = "stg"
instance_type = "t3.small"              # Slightly larger for staging
ami_id        = "ami-0c02fb55956c7d316"  # Amazon Linux 2 AMI in us-east-1
key_name      = "stg-key-pair"           # Replace with your staging key pair name

# Staging ingress rules - more restrictive than dev
ingress_rules = [
  {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  },
  {
    description = "Allow HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  },
  {
    description = "Allow SSH from office network"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["203.0.113.0/24"]  # Replace with your office IP range
  }
]