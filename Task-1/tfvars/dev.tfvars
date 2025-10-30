# Development Environment Configuration
aws_region    = "us-east-1"
env_name      = "dev"
instance_type = "t3.micro"
ami_id        = "ami-07860a2d7eb515d9a"  
key_name      = "dev-key-pair" 

ingress_rules = [
  {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  },
  {
    description = "Allow SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  
  },
  {
    description = "Allow development port 8080"
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
]