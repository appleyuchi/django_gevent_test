from django.shortcuts import render
from rest_framework.views import APIView
from .models import Test
from rest_framework.response import Response
import time
# Create your views here.
class Add_data(APIView):

    def post(self, requsts):
        print("-----------------------进度检测----------1---------------------")
        Test.objects.create(**{'url': str(1000000 * time.time())})
        # 代码的意思是每次post测试都创建一条数据
        print("-----------------------进度检测-----------2--------------------")
        return Response({"status": 200})