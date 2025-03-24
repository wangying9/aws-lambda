# src/lambda_function.py

def lambda_handler(event, context):
    # Just a simple response for this example
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!33'
    }