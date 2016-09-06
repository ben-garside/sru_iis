from . import routes

def setup(app):
    app.router.add_route('POST', '/iis/apps', routes.apps)
    app.router.add_route('POST', '/iis/sites', routes.sites)
    app.router.add_route('POST', '/iis/pools', routes.pools)
    app.router.add_route('POST', '/iis/vdir', routes.vdir)
    app.router.add_route('POST', '/iis/wp', routes.wp)