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
        sitesList = iis.vdir.get_all()
        message = "{} vdir(s) found".format(len(sitesList))
        msg = {
            "message": message,
            "code": 200,
            "vdirs": sitesList
        }
        logger.debug(message)

    except Exception as e:
        logger.error("'vdir/get_all' fialed with Exception: {}".format(e))

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def get_by_name(**kw):
    msg = {}
    try:
        if 'name' in kw.keys():
            kw.setdefault('partial', False)
            if isinstance(kw['name'], str):
                sites = iis.vdir.get_by_name(kw['name'], partial=kw['partial'])
                if kw['partial'] == True:
                    site_len = len(sites)
                else:
                    site_len = 1
                if sites:
                    message = "{} vdir(s) found with name '{}' (with partial:{})".format(site_len, kw['name'], kw['partial'])
                    msg.update({
                        'vdirs': sites,
                        'message': message,
                        'code': 200
                    })
                    logger.debug(message)
                else:
                    message = "No vdirs found with name '{}' (with partial:{})".format(kw['name'], kw['partial'])
                    msg.update({
                        'message': message,
                        'code': 404
                    })
                    logger.debug(message)
            else:
                message = "'name' type must be a string"
                msg.update({
                    'message': message,
                    'code': 404
                })
                logger.debug(message)
        else:
            message = "The 'name' parameter is missing"
            msg.update({
                'message': message,
                'code': 404
            })
            logger.debug(message)
    except Exception as e:
        logger.error("'sites/get_by_name' fialed with Exception: {}".format(e))
    
    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def get_by_physicalpath (**kw):
    msg = {}
    try:
        if 'path' in kw.keys():
            kw.setdefault('partial', False)
            if isinstance(kw['path'], str):
                vdirs = iis.vdir.get_by_physicalpath(kw['path'], partial=kw['partial'])
                if kw['partial'] == True:
                    vdirs_len = len(vdirs)
                else:
                    vdirs_len = 1
                if vdirs:
                    message = "{} vdir(s) found with path '{}' (with partial:{})".format(vdirs_len, kw['path'], kw['partial'])
                    msg.update({
                        'vdirs': vdirs,
                        'message': message,
                        'code': 200
                    })
                    logger.debug(message)
                else:
                    message = "No vdirs found with path '{}' (with partial:{})".format(kw['path'], kw['partial'])
                    msg.update({
                        'message': message,
                        'code': 404
                    })
                    logger.debug(message)
            else:
                message = "'name' type must be a string"
                msg.update({
                    'message': message,
                    'code': 404
                })
                logger.debug(message)
        else:
            message = "The 'name' parameter is missing"
            msg.update({
                'message': message,
                'code': 404
            })
            logger.debug(message)
    except Exception as e:
        logger.error("'sites/get_by_name' fialed with Exception: {}".format(e))
    
    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")
