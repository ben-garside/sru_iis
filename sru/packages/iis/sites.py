from sru.support.web import Response
from sru.support.data_process import encode
import sru.packages.iis_shim as iis
import time
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
        sitesList = iis.site.get_all()
        message = "{} sites found".format(len(sitesList))
        msg = {
            "message": message,
            "code": 200,
            "result": sitesList
        }
        logger.debug(message)

    except Exception as e:
        message = "'sites/get_all' fialed with Exception: {}".format(e)
        msg.update({
                    'message': message,
                    'result' : [],
                    'code': 501
        })
        logger.error(message)

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")

def get_by_id(**kw):
    msg = {}
    try:
        if 'id' in kw.keys():
            logger.debug("id: {}".format(kw['id']))
            if isinstance(kw['id'], int):
                site = iis.site.get_by_id(kw['id'])
                if site is not None:
                    message = "Site found with id {}.".format(kw['id'])
                    msg.update({
                        'result': [site],
                        'message': message,
                        'code': 200
                        })
                    logger.debug(message)
                else:
                    message = "No site matching id: {} was found".format(kw['id'])
                    msg.update({
                        'message': message,
                        'result' : [],
                        'code': 404
                        })
                    logger.debug(message)
            else:
                message = "id type must be integer"
                msg.update({
                    'message': message,
                    'result' : [],
                    'code': 404
                })
                logger.debug(message)
        else:
            message = "Missing id parameter"
            msg.update({
                'message': message,
                'result' : [],
                'code': 404
            })
            logger.debug(message)
    except Exception as e:
        message = "'sites/get_by_id' fialed with Exception: {}".format(e)
        msg.update({
                    'message': message,
                    'result' : [],
                    'code': 501
        })
        logger.error(message)
    
    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")

def get_by_name(**kw):
    msg = {}
    try:
        if 'name' in kw.keys():
            kw.setdefault('partial', False)
            if isinstance(kw['name'], str):
                sites = iis.site.get_by_name(kw['name'], partial=kw['partial'])
                if kw['partial'] == True:
                    site_len = len(sites)
                else:
                    site_len = 1
                    sites = [sites]
                if sites[0]:
                    message = "{} sites(s) found with name '{}' (with partial:{})".format(site_len, kw['name'], kw['partial'])
                    msg.update({
                        'result': sites,
                        'message': message,
                        'code': 200
                    })
                    logger.debug(message)
                else:
                    message = "No sites found with name '{}' (with partial:{})".format(kw['name'], kw['partial'])
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
        message = "'sites/get_by_name' fialed with Exception: {}".format(e)
        msg.update({
                    'message': message,
                    'result' : [],
                    'code': 501
        })
        logger.error(message)
    
    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")

def get_by_state(**kw):
    allowed_states = ['started', 'stopped']
    msg = {}
    try:
        if 'state' in kw.keys():
            if isinstance(kw['state'], str):
                if kw['state'].lower() in allowed_states:
                    sites = iis.site.get_by_state(kw['state'])
                    if len(sites) > 0:
                        message = "{} sites(s) found that are '{}'".format(len(sites), kw['state'])
                        msg.update({
                            'result': sites,
                            'message': message,
                            'code': 200
                        })
                        logger.debug(message)
                    else:
                        message = "No sites are '{}'".format(kw['state'])
                        msg.update({
                            'message': message,
                            'result' : [],
                            'code': 404
                        })
                        logger.debug(message)
                else:
                    message = 'State must be in: {}'.format(allowed_states)
                    msg.update({
                        'message': message,
                        'result' : [],
                        'code': 404
                    })
                    logger.debug(message)
            else:
                message = "'state' must be string"
                msg.update({
                    'message': message,
                    'result' : [],
                    'code': 404
                })
                logger.debug(message)
        else:
            message = "'state' parameter is missing"
            msg.update({
                'message': message,
                'result' : [],
                'code': 404
            })
            logger.debug(message)
    except Exception as e:
        message = "'sites/get_by_state' fialed with Exception: {}".format(e)
        msg.update({
                    'message': message,
                    'result' : [],
                    'code': 501
        })
        logger.error(message)
    
    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")

def get_by_binding(**kw):
    msg = {}
    try:
        if 'binding' in kw.keys():
            kw.setdefault('partial', False)
            if isinstance(kw['binding'], str):
                sites = iis.site.get_by_bindings(kw['binding'], partial=kw['partial'])
                if kw['partial'] == True:
                    site_len = len(sites)
                else:
                    site_len = 1
                    sites = [sites]
                if sites[0]:
                    message = "{} sites(s) found with binding '{}' (with partial:{})".format(site_len, kw['binding'], kw['partial'])
                    msg.update({
                        'result': sites,
                        'message': message,
                        'code': 200
                    })
                    logger.debug(message)
                else:
                    message = "No sites found with binding '{}' (with partial:{})".format(kw['binding'], kw['partial'])
                    msg.update({
                        'message': message,
                        'result' : [],
                        'code': 404
                    })
                    logger.debug(message)
            else:
                message = "'binding' type must be a string"
                msg.update({
                    'message': message,
                    'result' : [],
                    'code': 404
                })
                logger.debug(message)
        else:
            message = "The 'binding' parameter is missing"
            msg.update({
                'message': message,
                'result' : [],
                'code': 404
            })
            logger.debug(message)
    except Exception as e:
        message = "'sites/get_by_binding' fialed with Exception: {}".format(e)
        msg.update({
                    'message': message,
                    'result' : [],
                    'code': 501
        })
        logger.error(message)
    
    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")

def start_by_id(**kw):
    msg = {}
    try:
        if 'id' in kw.keys():
            run = iis.site.start_by_id(kw['id'])
            if run:
                msg.update(run)
                msg.update({
                            'result' : [],
                            'code': 200
                })
            else:
                message = "Someting went wrong starting the site"
                msg.update({
                            'message': message,
                            'result' : [],
                            'code': 500
                })
                logger.debug(message)

    except Exception as e:
        message = "'sites/start_by_id' fialed with Exception: {}".format(e)
        msg.update({
                    'message': message,
                    'result' : [],
                    'code': 501
        })
        logger.error(message)

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")

def stop_by_id(**kw):
    msg = {}
    try:
        if 'id' in kw.keys():
            run = iis.site.stop_by_id(kw['id'])
            if run:
                msg.update(run)
                msg.update({
                            'result' : [],
                            'code': 200
                })
            else:
                message = "Someting went wrong stopping the site"
                msg.update({
                            'message': message,
                            'result' : [],
                            'code': 500
                })
                logger.debug(message)

    except Exception as e:
        message = "'sites/stop_by_id' fialed with Exception: {}".format(e)
        msg.update({
                    'message': message,
                    'result' : [],
                    'code': 501
        })
        logger.error(message)

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")

def recycle_by_id(**kw):
    msg = {}
    try:
        if 'id' in kw.keys():
            if 'delay' in kw.keys():
                delay = kw['delay']
            else:
                delay = 10
            logger.debug("Stopping the site...")
            stop = iis.site.stop_by_id(kw['id'])
            if stop:
                site = iis.site.get_by_id(kw['id'])
                if site['state'] == 'Stopped':
                    logger.debug("Site stopped, waiting {} seconds...".format(delay))
                    time.sleep(delay)
                    logger.debug("Staring the site...")
                    start = iis.site.start_by_id(kw['id'])
                    if start:
                        site = iis.site.get_by_id(kw['id'])
                        if site['state'] == 'Started':
                            message = "Site has been restarted"
                            msg.update({
                                        'message': message,
                                        'result' : [],
                                        'code': 200
                            })
                            logger.debug(message)
                        else:
                            message = "Site did not start in time"
                            msg.update({
                                        'message': message,
                                        'result' : [],
                                        'code': 500
                            })
                            logger.debug(message)
                    else:
                        message = "Something went wrong re-starting the site"
                        msg.update({
                                    'message': message,
                                    'result' : [],
                                    'code': 500
                        })
                        logger.debug(message)
                else:
                    message = "Site did not stop in time"
                    msg.update({
                                'message': message,
                                'result' : [],
                                'code': 500
                    })
                    logger.debug(message)

            else:
                message = "Something went wrong stopping the site"
                msg.update({
                            'message': message,
                            'result' : [],
                            'code': 500
                })
                logger.debug(message)

    except Exception as e:
        message = "'sites/recycle_by_id' fialed with Exception: {}".format(e)
        msg.update({
                    'message': message,
                    'result' : [],
                    'code': 501
        })
        logger.error(message)

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")