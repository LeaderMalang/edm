class Config(object):
    # Env config.
    DEBUG = True
    SQLALCHEMY_POOL_RECYCLE = 28799
    SQLALCHEMY_ECHO = True

    # Session object config
    SECRET_KEY = b'T!ZwEjo~G")SrT(nvh&'

    # Database realted config (postgresql)
    DATABASE_NAME = "edm"
    DATABASE_USER = "root"
    DATABASE_PASSWORD = ""
    DATABASE_HOST = "127.0.0.1:89"

    # Payment API Config (Stripe)
    # STRIPE_SECRET_KEY = "sk_test_L39RRwo4BfpVTApJNVJrLoQc"
    # STRIPE_PUBLISHABLE_KEY = "pk_test_LJcpVJ0q93pnuix2fFpGqLbe"

    # EDM API config.
    API_VERSION = "1.1"
    USER_ID =  "726857"
    PARCEFLOW_API_TOKEN =  "R8sfaQdG4y"

    # Sqlalchemy config
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://{}:{}@{}/{}".format(DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = True