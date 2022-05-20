class Config:
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:Access@localhost/career_mentor'
    SECRET_KEY='QWERTY1234'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True
    
config_options={
    'production':ProdConfig,
    'development':DevConfig
}