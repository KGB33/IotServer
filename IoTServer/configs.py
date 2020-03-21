class BaseConfig:
    pass


class ProductionConfig(BaseConfig):
    FLASK_ENV = "production"


class DevelopmentConfig(BaseConfig):
    FLASK_ENV = "development"


class TestingConfig(BaseConfig):
    TESTING = True
