from django.db import connection
from upload.celery import app


@app.task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={'max_retries': 2, 'countdown': 2},
)
def upload(self, items):
    def getter(label):
        return lambda d: d[label]

    names = list(map(getter('name'), items))
    codes = list(map(getter('code'), items))
    categories = list(map(getter('category'), items))

    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO backend_item (name, code, category) SELECT unnest(%s), unnest(%s), unnest(%s)",
            (names, codes, categories)
        )
