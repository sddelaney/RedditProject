import boto3
import click
from boto3.dynamodb.conditions import Key, Attr

session = boto3.Session(profile_name='reddit')
db = session.resource('dynamodb')



def put_item1(tablename, item):
	"Put item into table"
	table = db.Table(tablename)
	table.put_item(   
		Item={'string':item}
    )


def scan_table(tablename):
	"Scan table for all items"
	table = db.Table(tablename)
	print(table.scan())



def query_table(tablename, item):
	"Query table for item and return item if matched"
	table = db.Table(tablename)
	result = table.query(KeyConditionExpression=Key('string').eq(item)).get('Items')
	print(result)
