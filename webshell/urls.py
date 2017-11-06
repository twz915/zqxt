from django.conf.urls import patterns, url

urlpatterns = patterns('webshell.views',
    url(r'^execute/$', 'execute_python', name='execute-python'),
    url(r'^execute-shell/$', 'execute_shell', name='execute-shell'),
)