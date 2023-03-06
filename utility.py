def response_obj(msg, code):
    return {'status':'success' if code==200 else 'error',
            'response':msg,
            'status_code':code
            }