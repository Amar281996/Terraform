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