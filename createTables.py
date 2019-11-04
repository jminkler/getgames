import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

table = dynamodb.create_table(
    TableName='pgns',
    KeySchema=[
        {
            'AttributeName': 'hash', 
            'KeyType': 'HASH'
        }
    ], 
    AttributeDefinitions=[
        {
            'AttributeName': 'hash', 
            'AttributeType': 'S'
        }
    ], 
    ProvisionedThroughput={
        'ReadCapacityUnits': 1, 
        'WriteCapacityUnits': 1
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName='staff')
print(table.item_count)