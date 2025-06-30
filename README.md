# 📸 Image Upload & Processing Pipeline on AWS

This project builds a serverless image processing pipeline using:

- S3 for uploads
- Lambda for image resizing (Python + Pillow)
- CloudFormation for infrastructure
- GitHub Actions for CI/CD

## 🛠️ Tech Stack

- AWS S3 (raw & processed buckets)
- AWS Lambda (Python 3.11)
- CloudFormation
- GitHub Actions

## 🚀 Deploy Instructions

### 1. Set Up AWS & GitHub
- Create an IAM user and save keys
- Add to GitHub repo secrets:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`

### 2. Push Code
- Push to `main` branch.
- GitHub Actions:
  - Zips lambda
  - Uploads to S3
  - Deploys CloudFormation

## 🧪 Test It
Upload any image to your `image-upload-raw-hauwa` bucket. The resized image will appear in `image-upload-processed-hauwa`.

## 🖼️ Architecture

![Architecture Diagram](assets/architecture.png)
