from sru.support.web import Response
from sru.support.data_process import encode
import iis_shim as iis
import logging


logger = logging.getLogger(__name__)


def not_found(**kw):
    msg = {
        "message": "invalid Action requested",
        "code": 404
    }

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")

def get_all(**kw):
    try:
        sites = iis.app.get_all()
        message = "{} apps found".format(len(sites))
        if sites:
            msg = {
                "message": message,
                "code": 200,
                "result": sites
            }
            logger.debug(message)
        else:
            msg = {
                "message": "Error getting apps",
                "code": 400,
                "result": sites
            }

        
    except Exception as e:
        logger.error("'pools/get_all' fialed with Exception: {}".format(e))

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def get_by_app_name(**kw):
    msg = {}
    try:
        if "name" in kw.keys():
            kw.setdefault('partial', False)
            if isinstance(kw['name'], str):
                apps = iis.app.get_by_name(kw['name'], partial=kw['partial'])
                if kw['partial'] == True:
                    site_len = len(apps)
                else:
                    site_len = 1
                    apps = [apps]
                if apps[0]:
                    message = "{} app(s) found with name '{}' (with partial:{})".format(site_len, kw['name'], kw['partial'])
                    msg.update({
                        "message": message,
                        "code": 200,
                        "result": apps
                    })
                    logger.debug(message)
                else:
                    message = "No apps found with name '{}' (with partial:{})".format(kw['name'], kw['partial'])
                    msg.update({
                        'message': message,
                        'result' : [],
                        'code': 404
                    })
                    logger.debug(message)
            else:
                message = "'name' type must be a string"
                msg.update({
                    'message': message,
                    'result' : [],
                    'code': 404
                })
                logger.debug(message)
        else:
            message = "The 'name' parameter is missing"
            msg.update({
                'message': message,
                'result' : [],
                'code': 404
            })
            logger.debug(message)

    except Exception as e:
        logger.error("'apps/get_by_name' fialed with Exception: {}".format(e))

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def get_by_pool_name(**kw):
    msg = {}
    try:
        if "name" in kw.keys():
            kw.setdefault('partial', False)
            if isinstance(kw['name'], str):
                apps = iis.app.get_by_pool_name(kw['name'], partial=kw['partial'])
                if kw['partial'] == True:
                    site_len = len(apps)
                else:
                    site_len = 1
                    apps = [apps]
                if apps[0]:
                    message = "{} app(s) found with application pool name '{}' (with partial:{})".format(site_len, kw['name'], kw['partial'])
                    msg.update({
                        "message": message,
                        "code": 200,
                        "result": apps
                    })
                    logger.debug(message)
                else:
                    message = "No apps found with application pool name '{}' (with partial:{})".format(kw['name'], kw['partial'])
                    msg.update({
                        'message': message,
                        'result' : [],
                        'code': 404
                    })
                    logger.debug(message)
            else:
                message = "'name' type must be a string"
                msg.update({
                    'message': message,
                    'result' : [],
                    'code': 404
                })
                logger.debug(message)
        else:
            message = "The 'name' parameter is missing"
            msg.update({
                'message': message,
                'result' : [],
                'code': 404
            })
            logger.debug(message)

    except Exception as e:
        logger.error("'apps/get_by_pool_name' fialed with Exception: {}".format(e))

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def get_by_site_name(**kw):
    msg = {}
    try:
        if "name" in kw.keys():
            kw.setdefault('partial', False)
            if isinstance(kw['name'], str):
                apps = iis.app.get_by_site_name(kw['name'], partial=kw['partial'])
                if kw['partial'] == True:
                    site_len = len(apps)
                else:
                    site_len = 1
                    apps = [apps]
                if apps[0]:
                    message = "{} app(s) found with site name '{}' (with partial:{})".format(site_len, kw['name'], kw['partial'])
                    msg.update({
                        "message": message,
                        "code": 200,
                        "result": apps
                    })
                    logger.debug(message)
                else:
                    message = "No apps found with site name '{}' (with partial:{})".format(kw['name'], kw['partial'])
                    msg.update({
                        'message': message,
                        'result' : [],
                        'code': 404
                    })
                    logger.debug(message)
            else:
                message = "'name' type must be a string"
                msg.update({
                    'message': message,
                    'result' : [],
                    'code': 404
                })
                logger.debug(message)
        else:
            message = "The 'name' parameter is missing"
            msg.update({
                'message': message,
                'result' : [],
                'code': 404
            })
            logger.debug(message)

    except Exception as e:
        logger.error("'apps/get_by_site_name' fialed with Exception: {}".format(e))

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")