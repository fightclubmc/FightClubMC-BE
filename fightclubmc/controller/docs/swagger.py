template = {
    "swagger": "2.0",
    "info": {
            "title": "FightClubMC API",
        "description": "API for FightClubMc",
        "contact": {
            "responsibleOrganization": "",
            "responsibleDeveloper": "",
            "email": "dimaio.albe@gmail.com",
            "url": "",
        },
        "termsOfService": "",
        "version": "1.0.0"
    },
    "basePath": "/api/v_1_0_0",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ]
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}
