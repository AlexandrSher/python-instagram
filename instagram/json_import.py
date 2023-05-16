try:
    import simplejson
except ImportError:
    try:
        import json as simplejson # just comment for test
    except ImportError:
        try:
            from django.utils import simplejson
        except ImportError:
            raise ImportError('A json library is required to use this python library')
print("Hello")
# I wanna check if it works


# and Lint also