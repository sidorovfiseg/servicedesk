import os
import signal

from config.sgi_config import sgi_config

wsgi_app = sgi_config.WSGI_APP
bind = f"{sgi_config.HOST}:{sgi_config.PORT}"
workers = sgi_config.WORKERS_COUNT
worker_class = sgi_config.WORKER_CLASS
reload = sgi_config.AUTO_RELOAD
timeout = 60 * 60 * 24


def worker_int(worker):
    os.kill(worker.pid, signal.SIGINT)