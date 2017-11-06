from subprocess import Popen, PIPE

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import permission_required

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


@csrf_exempt
@require_POST
@permission_required('is_superuser')
def execute_python(request):
    source = request.POST.get('source', '').replace('"', r'\"')
    proc = Popen('python -c "%s"' % source, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()

    lexer = get_lexer_by_name('pytb', stripall=True)
    formatter = HtmlFormatter(linenos=True, cssclass='source')
    result = highlight(out or err, lexer, formatter)

    return HttpResponse(result)


@csrf_exempt
@require_POST
@permission_required('is_superuser')
def execute_shell(request):
    source = request.POST.get('source', '')
    proc = Popen(source, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()

    lexer = get_lexer_by_name('pytb', stripall=True)
    formatter = HtmlFormatter(linenos=True, cssclass='source')
    result = highlight(out or err, lexer, formatter)

    return HttpResponse(result)
