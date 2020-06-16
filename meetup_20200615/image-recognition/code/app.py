import json
import boto3
import base64
import uuid
from datetime import datetime

rekognition = boto3.client('rekognition')

def imagecheck(event, context):

    confidence = low = high = gender = 0 

    image = event["body"]
    if image is not None:
        image = image.replace("data:image/jpeg;base64,","").replace("data:image/png;base64,","")

        decoded = base64.b64decode(image)

        response = rekognition.detect_faces(
            Image={
                'Bytes': decoded
                },
            Attributes=['ALL']
        )

        print(response)

        if "FaceDetails" in response:

            try:
                confidence = response["FaceDetails"][0]["Confidence"]
                low = response["FaceDetails"][0]["AgeRange"]["Low"]
                high = response["FaceDetails"][0]["AgeRange"]["High"]
                if response["FaceDetails"][0]["Gender"]["Value"] == 'Female':
                    gender = "Mulher"
                else:
                    gender = "Homem"
            except:
                pass

    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": json.dumps({
            "confidence": confidence,
            "low": low,
            "high": high,
            "gender": gender,
        }),
    }
