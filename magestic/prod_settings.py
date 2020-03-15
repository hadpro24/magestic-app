from magestic.settings import *

# DEBUG = False

ALLOWED_HOSTS += ['magestic-test.herokuapp.com',]

MIDDLEWARE += [
 'whitenoise.middleware.WhiteNoiseMiddleware',
 ]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
