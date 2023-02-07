from .base import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "__w)i8^i)r#4%&topk+$uw5&pj6&+ss8ns%jabog)_tl0(#"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["127.0.0.1","localhost"]


try:
    from .local import *
except ImportError:
    pass
