import boto3
import os
import logging
from datetime import datetime
from botocore.exceptions import ClientError
import time

# Configure logging
logging.basicConfig(
    filename='upload.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_file_size(file_path):
    """Get file size in bytes"""
    return os.path.getsize(file_path)

def upload_file(file_path, bucket, key=None, profile='default', max_retries=3):
    """
    Upload a file to S3 bucket with multipart support for large files
    """
    # Use file name if no key provided
    if not key:
        key = os.path.basename(file_path)

    # Get file size
    file_size = get_file_size(file_path)
    file_size_mb = file_size / (1024 * 1024)  # Convert to MB

    # Log upload start
    logging.info(f"Starting upload: {file_path} ({file_size_mb:.2f} MB) to s3://{bucket}/{key}")

    # Create S3 client with specified profile
    try:
        session = boto3.Session(profile_name=profile)
        s3 = session.client('s3')
    except Exception as e:
        logging.error(f"Failed to create S3 client with profile {profile}: {str(e)}")
        raise

    # Upload with retries
    for attempt in range(max_retries):
        try:
            if file_size_mb > 100:
                # Use multipart upload for large files
                config = boto3.s3.transfer.TransferConfig(
                    multipart_threshold=100 * 1024 * 1024,  # 100 MB
                    max_concurrency=4
                )
                s3.upload_file(
                    file_path, 
                    bucket, 
                    key,
                    Config=config,
                    Callback=lambda bytes_transferred: logging.info(
                        f"Progress: {bytes_transferred/file_size*100:.1f}% uploaded"
                    )
                )
            else:
                # Regular upload for smaller files
                s3.upload_file(file_path, bucket, key)

            # Log success
            logging.info(f"Successfully uploaded {file_path} to s3://{bucket}/{key}")
            print(f"✅ File uploaded successfully to s3://{bucket}/{key}")
            return True

        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                logging.warning(f"Upload attempt {attempt + 1} failed: {str(e)}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                logging.error(f"Upload failed after {max_retries} attempts: {str(e)}")
                print(f"❌ Upload failed: {str(e)}")
                return False

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Upload a file to S3 with multipart support")
    parser.add_argument('--file', required=True, help='Path to the file to upload')
    parser.add_argument('--bucket', required=True, help='S3 bucket name')
    parser.add_argument('--key', help='Optional: Custom name/prefix for the file in S3')
    parser.add_argument('--profile', default='default', help='AWS CLI profile to use')
    args = parser.parse_args()

    upload_file(args.file, args.bucket, args.key, args.profile)