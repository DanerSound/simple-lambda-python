import json

def lambda_handler(event, context):
    user = event["user"]
    user_id = event["id"]
    
    return {
        'message': f"Hello {user} your id is {user_id}"
    }

#test event : 

{
  "user": "daner",
  "id": "123"
}