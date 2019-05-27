import boto3
import click
from boto3.dynamodb.conditions import Key, Attr

session = boto3.Session(profile_name='reddit')
db = session.resource('dynamodb')


@click.group()
def cli():
	"db.py used to test Dynamodb table creation and modification"
	pass




@cli.command('create-table')
@click.argument('tablename')
def create_table(tablename):
	"Create a table in dynamodb"
	table = db.create_table(
	    AttributeDefinitions=[
	        {
	            'AttributeName': 'string',
	            'AttributeType': 'S'
	        },
	    ],
	    TableName=tablename,
	    KeySchema=[
	        {
	            'AttributeName': 'string',
	            'KeyType': 'HASH'
	        },
	    ],
		ProvisionedThroughput={
	        'ReadCapacityUnits': 123,
	        'WriteCapacityUnits': 123
	    	}
	)


@cli.command('put-item1')
@click.argument('tablename')
@click.argument('item')
def put_item1(tablename, item):
	"Put item into table"
	table = db.Table(tablename)
	table.put_item(   
		Item={'string':item}
    )

@cli.command('scan-table')
@click.argument('tablename')
def scan_table(tablename):
	"Scan table for all items"
	table = db.Table(tablename)
	print(table.scan())



@cli.command('query-table')
@click.argument('tablename')
@click.argument('item')
def query_table(tablename, item):
	"Query table for item and return item if matched"
	table = db.Table(tablename)
	result = table.query(KeyConditionExpression=Key('string').eq(item)).get('Items')
	print(result)

@cli.command('delete-item1')
@click.argument('tablename')
@click.argument('item')
def delete_item1(tablename, item):
	"Delete item from table"
	table = db.Table(tablename)
	table.delete_item(Key={'string':item})





if __name__ == '__main__':
	cli()

