# 🖼️ Image Upload & Processing Pipeline

This project enables users to upload images to an S3 bucket, which automatically triggers an AWS Lambda function that resizes the image and stores it in another bucket for optimized display.

## 🌐 Architecture

- Upload S3 Bucket
- Lambda Function (Python + Pillow)
- Output S3 Bucket
- Deployed via GitHub Actions and AWS CloudFormation

## 🚀 Deployment

1. Create IAM user with permissions
2. Add `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to GitHub Secrets
3. Push to `main` branch — deployment auto-triggers
