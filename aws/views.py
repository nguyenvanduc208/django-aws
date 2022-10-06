from http import client
import json
from django.http import HttpResponse, JsonResponse
from dotenv import load_dotenv
import os
import boto3 as bt3
load_dotenv()

# Create your views here.

# Sign Up


def SignUp(request):

    username = 'ducnv2082001@gmail.com'
    password = 'duc2082001'
    client = bt3.client('cognito-idp', region_name='ap-northeast-1')

    res = client.sign_up(
        ClientId=os.getenv('COGNITO_USER_CLIENT_ID'),
        Username=username,
        Password=password
    )

    res = json.dumps(res)
    return JsonResponse(res, safe=False)


def ResendConfirmCode(request):
    client = bt3.client('cognito-idp', region_name='ap-northeast-1')
    username = 'duc2082001@gmail.com'
    res = client.resend_confirmation_code(
        ClientId=os.getenv('COGNITO_USER_CLIENT_ID'),
        Username=username
    )

    res = json.dumps(res)
    return JsonResponse(res, safe=False)


def ConfirmSignUp(request):
    client = bt3.client('cognito-idp', region_name='ap-northeast-1')
    username = 'duc2082001@gmail.com'
    confirm_code = '307035'
    res = client.confirm_sign_up(
        ClientId=os.getenv('COGNITO_USER_CLIENT_ID'),
        Username=username,
        ConfirmationCode=confirm_code
    )

    res = json.dumps(res)
    return JsonResponse(res, safe=False)


# Sign In

def GetToken(request):
    username = 'ducnv2082001@gmail.com'
    password = 'duc2082001'
    client = bt3.client('cognito-idp', region_name='ap-northeast-1')
    res = client.initiate_auth(
        ClientId=os.getenv('COGNITO_USER_CLIENT_ID'),
        AuthFlow='USER_PASSWORD_AUTH',  # Kiểu quy trình xác thực
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password
        }
    )
    res = {
        'AccessToken': res['AuthenticationResult']['AccessToken'],
        'RefreshToken': res['AuthenticationResult']['RefreshToken']
    }
    return JsonResponse(res, safe=False)


def SignIn(request):
    access_token = "eyJraWQiOiJnZ3RqcEdDS0taVEd3KzJRbWlXQXdhcFFnM25ad01ENzNjMEhZWGl1V1wvTT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI4NDk5ZGE2OC0wM2MzLTQwMmEtODFkYi1lZmU4YWNmOTZjZmEiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtbm9ydGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtbm9ydGhlYXN0LTFfc1FXUFkwZXpUIiwiY2xpZW50X2lkIjoiNjZncjFkdHNxaW1paWEza2t1a282bDE0Z3UiLCJvcmlnaW5fanRpIjoiZDQ2NjY4Y2QtMDFjOS00ZmI2LThlMTUtMGZhY2M1MmE3NTMwIiwiZXZlbnRfaWQiOiJlZjNhYTA5ZC0zZGY3LTRhYzctYjNiYy00ZjM4MmFlYjU1NzYiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjY1MDQ0OTY5LCJleHAiOjE2NjUwNDg1NjksImlhdCI6MTY2NTA0NDk2OSwianRpIjoiNGFiNGQzOGEtYmQyYy00M2YyLTlkNTEtZDg3NjU5ZmY1MGFjIiwidXNlcm5hbWUiOiI4NDk5ZGE2OC0wM2MzLTQwMmEtODFkYi1lZmU4YWNmOTZjZmEifQ.G91FRMKmEL8RoqPDzeuW1M4IpPHmwM0dIr4jpZrNn8DFuysiD6xQ0rWYcIQiK8KYkuwOrGdmqvGWiRWYTB0wHP9ltz9mtqfXXpA-_LIuCOx9h5ZZK6X8TW6aD848lTaQrBIsdD5zsTVw20qcKjjxoup0IK25g4c6h9ab9vOx9yhy0AspKULugjRltMSXUv4kLlhU0k2mDxNFTcnm0D3rivukhbMQLLTsfp_pK93OAiUFaOuM8uT-Qh-THYAF3c7XfYqo-eZmhH9xW0dvfDeZiE4Ga6_Kp_z4v-7sAh8MXBp1Khmm2s2ZRt6jx5346MCICc9mNv5D7GRoHIukiVhpjw"

    client = bt3.client('cognito-idp', region_name='ap-northeast-1')
    res = client.get_user(
        AccessToken=access_token
    )

    print('>>>>', res)
    user = {}
    print('>>> Type', len(res['UserAttributes']))

    for val in res['UserAttributes']:
        if val['Name'] == 'sub':
            user['id'] = val['Value']

        if val['Name'] == 'email':
            user['email'] = val['Value']

    return JsonResponse(user, safe=False)
