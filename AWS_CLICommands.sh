1. Install the AWS CLI.
2. Verify the installation by running the command aws in the command prompt.
3. Configure AWS by executing aws configure in the command prompt.
4. To check all created AWS S3 buckets, run: aws s3 ls.
5. Export all local dataset files to S3. Use the command: aws s3 cp . s3://youtube-raw-data/ --recursive --exclude "*" --include "*.json".
