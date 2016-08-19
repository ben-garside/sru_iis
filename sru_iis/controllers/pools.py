from sru.support.web import Response
from sru.support.data_process import encode
import iis_shim as iis
import time
import logging


logger = logging.getLogger(__name__)


"""
not_found
get_all
get_by_name
get_by_pipelinemode
get_by_runtimeversion
get_by_state
get_by_site_id
stop_by_site_id
start_by_site_id
length

"""

def not_found(**kw):
    msg = {
        "message": "invalid Action requested",
        "code": 404
    }
    output = encode(msg, json=True)
    
    return Response(body=output, content_type="application/json")

def get_all(**kw):
    msg = {}
    try:
        poolList = iis.pool.get_all()
        message = "{} application pools found".format(len(poolList))
        msg.update({
            "message": message,
            "code": 200,
            "pools": poolList
        })
        logger.debug(message)
        
    except Exception as e:
        logger.error("'pools/get_all' fialed with Exception: {}".format(e))

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def get_by_name(**kw):
    msg = {}
    try:
        if 'name' in kw.keys():
            kw.setdefault('partial', False)
            if isinstance(kw['name'], str):
                pools = iis.pool.get_by_name(kw['name'], partial=kw['partial'])
                if kw['partial'] == True:
                    pool_len = len(pools)
                else:
                    pool_len = 1
                if pools:
                    message = "{} pool(s) found with name '{}' (with partial:{})".format(pool_len, kw['name'], kw['partial'])
                    msg.update({
                        'pools': pools,
                        'message': message,
                        'code': 200
                    })
                    logger.debug(message)
                else:
                    message = "No pools found with name '{}' (with partial:{})".format(kw['name'], kw['partial'])
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
        logger.error("'pools/get_by_name' fialed with Exception: {}".format(e))
    
    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")

def get_by_pipelinemode(**kw):
    modes = ["integrated", "classic"]
    msg = {}
    try:
        if 'mode' in kw.keys():
            if isinstance(kw['mode'], str):
                if kw['mode'].lower() in modes:
                    pools = iis.pool.get_by_PipelineMode(kw['mode'])
                    if len(pools) > 0:
                        message = "{} application pool(s) found that are '{}'".format(len(pools), kw['mode'])
                        msg.update({
                            'pools': pools,
                            'message': message,
                            'code': 200
                        })
                        logger.debug(message)
                    else:
                        message = "No application pool are '{}'".format(kw['mode'])
                        msg.update({
                            'message': message,
                            'code': 404
                        })
                        logger.debug(message)
                else:
                    message = 'Mode must be in: {}'.format(modes)
                    msg.update({
                        'message': message,
                        'code': 404
                    })
                    logger.debug(message)
            else:
                message = "'mode' must be string"
                msg.update({
                    'message': message,
                    'code': 404
                })
                logger.debug(message)
        else:
            message = "'mode' parameter is missing"
            msg.update({
                'message': message,
                'code': 404
            })
            logger.debug(message)
    except Exception as e:
        logger.error("'pools/get_by_PipelineMode' fialed with Exception: {}".format(e))
    
    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def get_by_runtimeverion(**kw):
    msg = {}
    try:
        if 'runtimeverion' in kw.keys():
            if isinstance(kw['runtimeverion'], str):
                pools = iis.pool.get_by_runtimeverion(kw['runtimeverion'])
                if pools:
                    message = "{} application pool(s) found that have a runtimeverion of '{}'".format(len(pools), kw['runtimeverion'])
                    msg.update({
                        'pools': pools,
                        'message': message,
                        'code': 200
                    })
                    logger.debug(message)
                else:
                    message = "No application pool have a runtimeversion of '{}'".format(kw['runtimeverion'])
                    msg.update({
                        'message': message,
                        'code': 404
                    })
                    logger.debug(message)
            else:
                message = "'mode' must be string"
                msg.update({
                    'message': message,
                    'code': 404
                })
                logger.debug(message)
        else:
            message = "'mode' parameter is missing"
            msg.update({
                'message': message,
                'code': 404
            })
            logger.debug(message)
    except Exception as e:
        logger.error("'pools/get_by_PipelineMode' fialed with Exception: {}".format(e))
    
    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def get_by_state(**kw):
    allowed_states = ['started', 'stopped']
    msg = {}
    try:
        if 'state' in kw.keys():
            if isinstance(kw['state'], str):
                if kw['state'].lower() in allowed_states:
                    pools = iis.pool.get_by_state(kw['state'])
                    if len(pools) > 0:
                        message = "{} application pool(s) found that are '{}'".format(len(pools), kw['state'])
                        msg.update({
                            'pools': pools,
                            'message': message,
                            'code': 200
                        })
                        logger.debug(message)
                    else:
                        message = "No application pool are '{}'".format(kw['state'])
                        msg.update({
                            'message': message,
                            'code': 404
                        })
                        logger.debug(message)
                else:
                    message = 'State must be in: {}'.format(allowed_states)
                    msg.update({
                        'message': message,
                        'code': 404
                    })
                    logger.debug(message)
            else:
                message = "'state' must be string"
                msg.update({
                    'message': message,
                    'code': 404
                })
                logger.debug(message)
        else:
            message = "'state' parameter is missing"
            msg.update({
                'message': message,
                'code': 404
            })
            logger.debug(message)
    except Exception as e:
        logger.error("'pools/get_by_state' fialed with Exception: {}".format(e))
    
    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")

def get_by_site_id(**kw):
    msg = {}
    try:
        if 'id' in kw.keys():
            logger.debug("id: {}".format(kw['id']))
            if isinstance(kw['id'], int):
                pool = iis.pool.get_by_site_id(kw['id'])
                if pool is not None:
                    message = "Application pool found for site id {}.".format(kw['id'])
                    msg.update({
                        'pool': pool,
                        'message': message,
                        'code': 200
                        })
                    logger.debug(message)
                else:
                    message = "No application pool matching for site id: {} was found".format(kw['id'])
                    msg.update({
                        'message': message,
                        'code': 404
                        })
                    logger.debug(message)
            else:
                message = "id type must be integer"
                msg.update({
                    'message': message,
                    'code': 404
                })
                logger.debug(message)
        else:
            message = "Missing id parameter"
            msg.update({
                'message': message,
                'code': 404
            })
            logger.debug(message)
    except Exception as e:
        logger.error("'pools/get_by_id' fialed with Exception: {}".format(e))
    
    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def stop_by_site_id(**kw):
    msg = {}
    try:
        if 'id' in kw.keys():
            run = iis.pool.stop_by_site_id(kw['id'])
            if run:
                msg.update(run)
                msg.update({
                            'code': 200
                })
            else:
                message = "Someting went wrong stopping the application pool"
                msg.update({
                            'message': message,
                            'code': 500
                })
                logger.debug(message)

    except Exception as e:
        logger.error("'pool/stop_by_site_id' fialed with Exception: {}".format(e))

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def start_by_site_id(**kw):
    msg = {}
    try:
        if 'id' in kw.keys():
            run = iis.pool.start_by_site_id(kw['id'])
            if run:
                msg.update(run)
                msg.update({
                            'code': 200
                })
            else:
                message = "Someting went wrong starting the application pool"
                msg.update({
                            'message': message,
                            'code': 500
                })
                logger.debug(message)

    except Exception as e:
        logger.error("'pool/start_by_site_id' fialed with Exception: {}".format(e))

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def recycle_by_site_id(**kw):
    msg = {}
    try:
        if 'id' in kw.keys():
            if 'delay' in kw.keys():
                delay = kw['delay']
            else:
                delay = 10
            logger.debug("Stopping the pool...")
            stop = iis.pool.stop_by_site_id(kw['id'])
            if stop:
                pool = iis.pool.get_by_site_id(kw['id'])
                if pool['state'] == 'Stopped':
                    logger.debug("Pool stopped, waiting {} seconds...".format(delay))
                    time.sleep(delay)
                    logger.debug("Staring the site...")
                    start = iis.pool.start_by_site_id(kw['id'])
                    if start:
                        pool = iis.pool.get_by_site_id(kw['id'])
                        if pool['state'] == 'Started':
                            message = "Pool has been restarted"
                            msg.update({
                                        'message': message,
                                        'code': 200
                            })
                            logger.debug(message)
                        else:
                            message = "Pool did not start in time"
                            msg.update({
                                        'message': message,
                                        'code': 500
                            })
                            logger.debug(message)
                    else:
                        message = "Something went wrong re-starting the pool"
                        msg.update({
                                    'message': message,
                                    'code': 500
                        })
                        logger.debug(message)
                else:
                    message = "Pool did not stopp in time"
                    msg.update({
                                'message': message,
                                'code': 500
                    })
                    logger.debug(message)

            else:
                message = "Something went wrong stopping the pool"
                msg.update({
                            'message': message,
                            'code': 500
                })
                logger.debug(message)

    except Exception as e:
        logger.error("'pools/recycle_by_site_id' fialed with Exception: {}".format(e))

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")