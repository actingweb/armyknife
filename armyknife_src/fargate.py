import base64
import json
import os
import logging
import boto3


def in_fargate():
    if os.getenv('LAMBDA_TASK_ROOT', None):
        return False
    return True


def fork_container(req, actor_id):
    """
    If not running in lambda env, a fargate container is forked off to
    take the entire request and execute with it.
    """
    if not os.getenv('LAMBDA_TASK_ROOT', None):
        return False
    headers = {}
    for k, v in req.headers.items():
        headers[k] = v
    params = {}
    for k, v in req.params.items():
        params[k] = v
    webreq = {
        'method': 'POST',
        'data': req.body.decode('utf-8'),
        'cookies': req.cookies,
        'headers': headers,
        'values': params,
        'url': req.url
    }
    webreq = base64.b64encode(json.dumps(webreq).encode('utf-8')).decode('utf-8')
    client = boto3.client('ecs', region_name='us-west-2')
    response = client.run_task(
        cluster=os.getenv('FARGATE_CLUSTER', 'default'),
        launchType='FARGATE',
        taskDefinition=os.getenv('FARGATE_TASK', 'armyknife-fargate-dev'),
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [
                    'subnet-0fe25e095542cf484',
                    'subnet-0d7f06e8a44c4ab4e'
                ],
                'securityGroups': [
                    'sg-07182a58113457cda',
                ],
                'assignPublicIp': 'ENABLED'
            }
        },
        overrides={
            'containerOverrides': [
                {
                    'name': 'armyknife-fargate-dev',
                    'command': [
                        '/usr/local/bin/python',
                        '/src/application.py'
                    ],
                    'environment': [
                        {
                            'name': 'ACTINGWEB_PAYLOAD',
                            'value': webreq
                        },
                        {
                            'name': 'ACTINGWEB_ACTOR',
                            'value': actor_id
                        },
                        {
                            'name': 'APP_HOST_FQDN',
                            'value': os.getenv('APP_HOST_FQDN', 'localhost')
                        },
                        {
                            'name': 'APP_HOST_PROTOCOL',
                            'value': os.getenv('APP_HOST_PROTOCOL', 'http://')
                        },
                        {
                            'name': 'AWS_DB_PREFIX',
                            'value': os.getenv('AWS_DB_PREFIX', 'armyknife_local')
                        },
                        {
                            'name': 'AWS_DEFAULT_REGION',
                            'value': os.getenv('AWS_DEFAULT_REGION', 'us-west-1')
                        },
                        {
                            'name': 'APP_BOT_TOKEN',
                            'value': os.getenv('APP_BOT_TOKEN', '')
                        },
                        {
                            'name': 'APP_BOT_EMAIL',
                            'value': os.getenv('APP_BOT_EMAIL', '')
                        },
                        {
                            'name': 'APP_BOT_SECRET',
                            'value': os.getenv('APP_BOT_SECRET', '')
                        },
                        {
                            'name': 'APP_BOT_ADMIN_ROOM',
                            'value': os.getenv('APP_BOT_ADMIN_ROOM', '')
                        },
                        {
                            'name': 'APP_OAUTH_ID',
                            'value': os.getenv('APP_OAUTH_ID', '')
                        },
                        {
                            'name': 'APP_OAUTH_KEY',
                            'value': os.getenv('APP_OAUTH_KEY', '')
                        }
                    ]
                },
            ]
        }
    )
    if 'failures' in response:
        for f in response['failures']:
            logging.error('Fargate error: ' + f['arn'] + ' ' + f['reason'])
    logging.info('Successfully forked off task to fargate')
    return True


def get_request(req):
    req = base64.b64decode(req.encode('utf-8')).decode('utf-8')
    try:
        req = json.loads(req)
    except json.JSONDecodeError:
        return None
    return req
