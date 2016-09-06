from sru.support.web import Response
from . import apps as appsCtrl
from . import sites as sitesCtrl
from . import pools as poolsCtrl
from . import vdir as vdirCtrl
from . import wp as wpCtrl
import logging

logger = logging.getLogger(__name__)

params = [
    'action',
    'action_param'
]

async def apps(request):
    data = await request.json()
    if all(k in params for k in data.keys()):
        data.setdefault('action_param',{}) # set value if non provided
        action = getattr(appsCtrl, data['action'], appsCtrl.not_found)
        res = action(**data['action_param'])
        return res
    else:
        return Response(text="an invalid param was found in request")


async def sites(request):
    data = await request.json()
    if all(k in params for k in data.keys()):
        data.setdefault('action_param',{}) # set value if non provided
        action = getattr(sitesCtrl, data['action'], sitesCtrl.not_found)
        res = action(**data['action_param'])
        return res
    else:
        return Response(text="an invalid param was found in request")


async def pools(request):
    data = await request.json()
    if all(k in params for k in data.keys()):
        data.setdefault('action_param',{}) # set value if non provided
        action = getattr(poolsCtrl, data['action'], poolsCtrl.not_found)
        res = action(**data['action_param'])
        return res
    else:
        return Response(text="an invalid param was found in request")


async def vdir(request):
    data = await request.json()
    if all(k in params for k in data.keys()):
        data.setdefault('action_param',{}) # set value if non provided
        action = getattr(vdirCtrl, data['action'], vdirCtrl.not_found)
        res = action(**data['action_param'])
        return res
    else:
        return Response(text="an invalid param was found in request")


async def wp(request):
    data = await request.json()
    if all(k in params for k in data.keys()):
        data.setdefault('action_param',{}) # set value if non provided
        action = getattr(wpCtrl, data['action'], wpCtrl.not_found)
        res = action(**data['action_param'])
        return res
    else:
        return Response(text="an invalid param was found in request")