from functools import wraps
from flask import request

def activity_logger (f):
	@wraps(f)
	def log(*args, **kwargs):
		print(request.url)
		return f(*args, **kwargs)
	
	return log
