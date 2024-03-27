from .models import Link

def context_dict(req):
    ctx = {}
    link = Link.objects.all()
    for l in link:
        ctx[l.key] = l.url
    return ctx