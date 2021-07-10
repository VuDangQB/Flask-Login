from app.config import BOILERPLATE_ENV
from app import create_app

app = create_app(config_name = BOILERPLATE_ENV)
app.app_context().push()

if __name__ == '__main__':
    app.run()