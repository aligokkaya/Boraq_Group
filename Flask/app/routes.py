"""Initialize Flask app."""
from app import app

with app.app_context():

    from .home import home
    from .news import news
    from .admin import admin
    from .rest_api import rest_api
    
    
    app.register_blueprint(admin.admin_bp)
    app.register_blueprint(home.home_bp)
    app.register_blueprint(news.news_bp)
    app.register_blueprint(rest_api.rest_api)

