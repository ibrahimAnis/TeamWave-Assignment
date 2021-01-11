from celery.decorators import task
from celery.utils.log import get_task_logger
from django.contrib.gis.geos import Point
from django.db.models import *
from .models import Cache
logger = get_task_logger(__name__)


@task(name="populatedb")
def populatedb(query, apidata):
	if Cache.objects.filter(query=query).exists()==False:
		cache_db=Cache.objects.create(query=query, data=apidata)
		cache_db.save()
		print("database populated")
	logger.info("created")
