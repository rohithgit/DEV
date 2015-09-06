
# DATABASES = {
#     "default": {
#         "ENGINE": 'django.db.backends.mysql',
#         "NAME": 'builder',
#         "USER": 'root',
#         "PASSWORD": 'root',
#         "HOST": 'localhost',
#         "PORT": 3306,
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bwd',
        'USER': 'postgres',
        'PASSWORD': 'winner',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
