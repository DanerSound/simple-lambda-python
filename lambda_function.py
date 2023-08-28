import boto3
import os

def lambda_handler(event: any, context: any):
    user = event["user"]
    user_id = event["id"]
    visit_counter : int = 0

    # create a dynamoDB client, get a direct reference to the db table
    dynamodb = boto3.resource("dynamodb")
    table_name = os.environ["TABLE_NAME"]
    table = dynamodb.Table(table_name)


    response = table.get_item(Key={"id":user_id})
    if "Item" in response:
        visit_counter = response["Item"]["visit"]

    # increase the numer of visit
    visit_counter += 1
    # update a row
    table.put_item(Item={"user": user, "id" : user_id, "visit":visit_counter})

    message = " Hello " + user + " your id is " + str(user_id) + " you have visit this " + str(visit_counter) + " times! "
    
    return{"message":message}

if __name__ == "__main__":
    os.environ["TABLE_NAME"] = "visit-count-table"
    event = {"user":"Jhon","id":6453}
    print(lambda_handler(event, None))
