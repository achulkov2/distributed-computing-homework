import json

from django.db.utils import DataError
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
from backend.models import Item
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse, QueryDict
from django.forms.models import model_to_dict


@csrf_exempt
def item_by_id(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return HttpResponseBadRequest('The provided id {} does not match any item.\n'.format(item_id))
    if request.method == 'PUT':
        params = QueryDict(request.body)
        for key, val in params.items():
            if hasattr(item, key):
                setattr(item, key, val)
        try:
            item.save()
        except DataError:
            return HttpResponseBadRequest('One of the parameters does not follow the requested format.\n')

    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse("Item with id {} was successfully deleted\n".format(item_id))
    elif request.method != 'GET':
        return HttpResponseBadRequest('Only GET, PUT and DELETE requests are accepted.\n')
    return JsonResponse(model_to_dict(item))


def extract_uint(body, param):
    try:
        value = int(body[param])
    except ValueError:
        return False, HttpResponseBadRequest("The {} parameter should be an integer.\n".format(param))
    if value <= 0:
        return False, HttpResponseBadRequest("The {} parameter should be positive.\n".format(param))
    return True, value


@csrf_exempt
def list_items(request=None):
    page = 0
    page_size = Item.objects.count()
    if request is not None:
        if request.method != 'GET':
            return HttpResponseBadRequest("Only GET requests are accepted.\n")
        if 'page' in request.GET:
            res, page = extract_uint(request.GET, 'page')
            if not res:
                return page
            page -= 1
        if 'page_size' in request.GET:
            res, page_size = extract_uint(request.GET, 'page_size')
            if not res:
                return page_size

    result = Item.objects.all().order_by('id')[page * page_size:(page + 1) * page_size]
    return HttpResponse(json.dumps(list(result.values())), content_type='application/json')


@csrf_exempt
def items(request):
    if request.method == 'POST':
        params = QueryDict(request.body)
        try:
            item = Item(name=params['name'], code=params['code'], category=params['category'])
        except MultiValueDictKeyError:
            return HttpResponseBadRequest('The following parameters should be provided: name, code and category\n')
        try:
            item.save()
        except DataError:
            return HttpResponseBadRequest('One of the parameters does not follow the requested format.\n')
        return JsonResponse(model_to_dict(item))
    elif request.method == 'GET':
        return list_items()
    else:
        return HttpResponseBadRequest('Only GET and POST requests are accepted')
