import os
from dotenv import load_dotenv
from werkzeug.contrib.fixers import ProxyFix

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from bluelog import create_app  # noqa

# config_name = os.getenv('FLASK_CONFIG', 'development')
if os.getenv('FLASK_CONFIG') == 'production':
    app = create_app('production')
    app.wsgi_app = ProxyFix(app.wsgi_app)
