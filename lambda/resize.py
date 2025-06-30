import boto3
from PIL import Image
import os
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = os.environ['SOURCE_BUCKET']
    dest_bucket = os.environ['DEST_BUCKET']

    for record in event['Records']:
        key = record['s3']['object']['key']
        image_obj = s3.get_object(Bucket=source_bucket, Key=key)
        image = Image.open(image_obj['Body'])

        # Resize
        image.thumbnail((800, 800))

        buffer = io.BytesIO()
        image.save(buffer, 'JPEG')
        buffer.seek(0)

        s3.put_object(Bucket=dest_bucket, Key=key, Body=buffer, ContentType='image/jpeg')

    return {'statusCode': 200, 'body': f'Successfully processed {key}'}
