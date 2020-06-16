import json
import boto3
import base64
import uuid
from datetime import datetime
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
import requests

patch_all()
xray_recorder.configure(service='APPMeetup')

rekognition = boto3.client('rekognition')
dynamodb = boto3.client('dynamodb')
s3 = boto3.client('s3')

@xray_recorder.capture("imagecheck")
def imagecheck(event, context):

    confidence = low = high = gender = 0 

    image = event["body"]
    if image is not None:

        #Analisando imagem através do rekognition
        subseg = xray_recorder.begin_subsegment('Rekognition check')
        image = image.replace("data:image/jpeg;base64,","").replace("data:image/png;base64,","")

        decoded = base64.b64decode(image)

        response = rekognition.detect_faces(
            Image={
                'Bytes': decoded
                },
            Attributes=['ALL']
        )
        subseg.put_annotation('chamada', 'medir retorno')
        subseg.put_metadata('resposta', response)
        xray_recorder.end_subsegment()

        #Armazenando os metadados no DynamoDB
        xray_recorder.begin_subsegment('Dynamodb put item')
        idimg = str(uuid.uuid4())

        responsedy = dynamodb.put_item(
                                    Item={
                                        'id': {
                                            'S': idimg,
                                        },
                                        'timestamp': {
                                            'S': str(datetime.utcnow().isoformat()),
                                        },
                                        'imagecheck': {
                                            'S': str(response)
                                        }
                                    },
                                    TableName='ImageRecognition'
                                )
        xray_recorder.end_subsegment()

        #Salvando imagem no S3
        xray_recorder.begin_subsegment('S3 PutObject')
        s3.put_object(Body=decoded, Bucket='imagerecognitionmeetup2020', Key=idimg+'.jpg')
        xray_recorder.end_subsegment()

        if "FaceDetails" in response:

            try:
                confidence = response["FaceDetails"][0]["Confidence"]
                low = response["FaceDetails"][0]["AgeRange"]["Low"]
                high = response["FaceDetails"][0]["AgeRange"]["High"]
                if response["FaceDetails"][0]["Gender"]["Value"] == 'Female':
                    gender = "Mulher"
                else:
                    gender = "Homem"
                    xray_recorder.begin_subsegment('API com delay')
                    responsedelay = requests.get('http://3.232.229.57/delay.php')
                    xray_recorder.end_subsegment()
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
