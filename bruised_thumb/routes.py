def includeme(config):
    config.add_static_view('stat_assets', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('post', '/post/{date}')
