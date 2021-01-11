from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .throttles import BurstRateThrottle,SustainedRateThrottle
from rest_framework import generics
from .utils import StackExchange
from .models import Cache
from .serializer import CacheSerializer
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class GetAll_Questions_View(APIView):
	throttle_classes = [BurstRateThrottle,SustainedRateThrottle]
	def get(self,request,*args,**kwargs):
		page = self.request.query_params.get("page")
		stack_exchange = StackExchange()
		ques = stack_exchange.get_all_questions()
		return Response(ques,status=status.HTTP_200_OK)


class Get_By_Query_View(APIView):
	throttle_classes= [BurstRateThrottle,SustainedRateThrottle]
	def get(self,request,*args,**kwargs):
		query = self.request.query_params.get("query")
		sort = self.request.query_params.get("sort")
		order = self.request.query_params.get("order")
		if(sort=="0"):
			sort="desc"
		if(order=="0"):
			order="activity"
		result_set = Cache.objects.filter(query=query)
		if result_set.exists():
			ques_object = result_set.first()
			serialized_data = CacheSerializer(ques_object)
			data = serialized_data.data['data']
			return Response(data,status=status.HTTP_200_OK)
		stack_exchange = StackExchange()
		query_ques_res = stack_exchange.get_by_query(query,order,sort)
		return Response(query_ques_res,status=status.HTTP_200_OK)

