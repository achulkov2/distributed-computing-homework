import csv
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from . import tasks

DROP_UNIQUE_CODES = False


class FileUpload(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, *args, **kwargs):
        unique_codes = set()
        for chunk in request.FILES['file'].chunks():
            items = []
            for line in csv.DictReader(chunk.decode().splitlines(),
                                       fieldnames=('name', 'code', 'category'),
                                       delimiter=','):
                print(line)
                name = line.get('name')
                code = line.get('code')
                category = line.get('category')
                if None in [name, code, category]:
                    return Response(data={"message": "Incorrect item format."}, status=HTTP_400_BAD_REQUEST)
                if code not in unique_codes:
                    unique_codes.add(code)
                    items.append({
                        'name': line['name'],
                        'code': code,
                        'category': line['category']
                    })
            tasks.upload.delay(items)
            if DROP_UNIQUE_CODES:
                unique_codes.clear()

        return Response(status=HTTP_200_OK)
