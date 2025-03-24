# src/lambda_function.py
import requests
def lambda_handler(event, context):
    # Just a simple response for this example
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!33556'
    }