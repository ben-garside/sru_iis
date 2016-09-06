from sru.support.web import Response
from sru.support.data_process import encode
import sru.packages.iis_shim as iis
import logging


logger = logging.getLogger(__name__)


def not_found(**kw):
    msg = {
        "message": "invalid Action requested",
        'result': [],
        "code": 404
    }

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def get_all(**kw):
    try:
        sitesList = iis.wp.get_all()
        message = "{} worker process(es) found".format(len(sitesList))
        msg = {
            "message": message,
            "code": 200,
            "result": sitesList
        }
        logger.debug(message)

    except Exception as e:
        message = "'wp/get_all' fialed with Exception: {}".format(e)
        msg = {
            "message": message,
            "code": 501,
            "result": []
        }
        logger.error(message)

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")



def get_by_name(**kw):
    msg = {}
    try:
        if 'name' in kw.keys():
            if isinstance(kw['name'], int):
                sites = iis.wp.get_by_name(kw['name'])
                if sites:
                    message = "Worker process found with name '{}'".format(kw['name'])
                    msg.update({
                        'result': sites,
                        'message': message,
                        'code': 200
                    })
                    logger.debug(message)
                else:
                    message = "No worker processes found with name '{}'".format(kw['name'])
                    msg.update({
                        'message': message,
                        'result': [],
                        'code': 404
                    })
                    logger.debug(message)
            else:
                message = "'name' type must be a int"
                msg.update({
                    'message': message,
                    'result': [],
                    'code': 404
                })
                logger.debug(message)
        else:
            message = "The 'name' parameter is missing"
            msg.update({
                'message': message,
                'result': [],
                'code': 404
            })
            logger.debug(message)
    except Exception as e:
        message = "'wp/get_by_name' fialed with Exception: {}".format(e)
        msg = {
            "message": message,
            "code": 501,
            "result": []
        }
        logger.error(message)
    
    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")

def get_by_pool_name(**kw):
    msg = {}
    try:
        if 'name' in kw.keys():
            kw.setdefault('partial', False)
            if isinstance(kw['name'], str):
                sites = iis.wp.get_by_pool_name(kw['name'], partial=kw['partial'])
                logger.debug(sites)
                if kw['partial'] == True:
                    site_len = len(sites)
                else:
                    site_len = 1
                    sites = [sites]
                if sites[0]:
                    message = "{} worker process(es) found with name '{}' (with partial:{})".format(site_len, kw['name'], kw['partial'])
                    msg.update({
                        'result': sites,
                        'message': message,
                        'code': 200
                    })
                    logger.debug(message)
                else:
                    message = "No worker processes found with name '{}' (with partial:{})".format(kw['name'], kw['partial'])
                    msg.update({
                        'message': message,
                        'result': [],
                        'code': 404
                    })
                    logger.debug(message)
            else:
                message = "'name' type must be a string"
                msg.update({
                    'message': message,
                    'result': [],
                    'code': 404
                })
                logger.debug(message)
        else:
            message = "The 'name' parameter is missing"
            msg.update({
                'message': message,
                'result': [],
                'code': 404
            })
            logger.debug(message)
    except Exception as e:
        message = "'wp/get_by_pool_name' fialed with Exception: {}".format(e)
        msg = {
            "message": message,
            "code": 501,
            "result": []
        }
        logger.error(message)
    
    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")
