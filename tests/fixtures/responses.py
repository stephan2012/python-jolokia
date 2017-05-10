ILLEGAL_ARGUMENT = {
    'error_type': "java.lang.IllegalArgumentException",
    'error': "java.lang.IllegalArgumentException : No type with name 'foo' exists",
    'status': 400
}

ROOT_URL_OK = {
    "request": {
        "type": "version"
    },
    "value": {
        "agent": "1.3.6",
        "protocol": "7.2",
        "config": {
            "maxCollectionSize": "0",
            "agentId": "10.195.20.189-18288-6b59e8eb-servlet",
            "debug": "false",
            "agentType": "servlet",
            "serializeException": "false",
            "detectorOptions": "{}",
            "dispatcherClasses": "org.jolokia.jsr160.Jsr160RequestDispatcher",
            "maxDepth": "15",
            "discoveryEnabled": "false",
            "canonicalNaming": "true",
            "historyMaxEntries": "10",
            "includeStackTrace": "true",
            "maxObjects": "0",
            "debugMaxEntries": "100"
        },
        "info": {
            "product": "JBoss EAP",
            "vendor": "RedHat",
            "version": "7.0.0.GA"
        }
    },
    "timestamp": 1494275547,
    "status": 200
}


# FIXME These need to be DRY
def mock_illegal_arg(self, *args, **kwargs):

    import json
    from requests import Response
    resp_json = json.dumps(ILLEGAL_ARGUMENT)

    resp = Response()
    setattr(Response, 'content', resp_json.encode('utf-8'))
    resp.status_code = 400
    setattr(Response, 'ok', False)

    return resp.json()


def mock_root_ok(self, *args, **kwargs):

    import json
    from requests import Response
    resp_json = json.dumps(ROOT_URL_OK)

    resp = Response()
    setattr(Response, 'content', resp_json.encode('utf-8'))
    resp.status_code = 200
    setattr(Response, 'ok', True)

    return resp.json()
