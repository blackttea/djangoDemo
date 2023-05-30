from django.urls import path
from . import views

functions = [e for e in dir(views) if not e.startswith('_') and type(eval('views.' + e)).__name__ == 'function']
print(functions)
urlpatterns = []

for f in functions:
    urlpatterns.append(path(f, eval('views.' + f)))