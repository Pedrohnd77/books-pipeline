import boto3

def upload_para_s3(arquivo, bucket_name, object_name=None):
    s3 = boto3.client('s3')
    if object_name is None:
        object_name = arquivo
    s3.upload_file(arquivo, bucket_name, object_name)
