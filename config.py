import multiprocessing

bind = "0.0.0.0:8080"
#cpu = multiprocessing.cpu_count()
#workers = cpu + int(cpu/2)
workers =2
threads=2
#worker_class = "sync"
timeout = 500
preload = True
errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'