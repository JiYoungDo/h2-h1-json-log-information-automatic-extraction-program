
from django.db import models
import json
import os
from django.core.files.storage import default_storage
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

# Create your models here.


class File(models.Model):
    filegroup  = models.CharField(max_length=100)
    filenum  = models.CharField(max_length=100)
    protocoll = models.CharField(max_length=100 , null=True)
    hostname = models.CharField(max_length=100, null=True)
    json = models.FileField(upload_to='files/json/')
    
    # str 메소드 / 클래스 자체 내용 출력하고 싶을 대 형식 지정 메서드
    def __str__(self):
        return 'filegroup: {}, filenum; {}'.format(self.filegroup, self.filenum)

    def delete(self, *args, **kwargs):
        self.json.delete()
        super().delete(*args, **kwargs)

    def get_file_group(self):
        return '{}'.format(self.filegroup)

    def get_file_num(self):
        return '{}'.format(self.filenum)

    def get_protocol_name(self):
        return '{}'.format(self.protocoll)

    def get_host_name(self):
         return '{}'.format(self.hostname)  

    def get_data(self):
        user_input_host = self.hostname
        user_host_id = 0 # temp 값
        result_send = 0
        result_recv = 0
        result_diff = 0

        '''파일에서 해당 url 에 대한 '''
        # 파이썬 애니웨어 글로벌 서비스 일시
        file_path = os.getcwd() +'/source/Capstone-Design/mysite' +self.json.url
        
        # 로컬 테스트 서버 일시
        # file_path = os.getcwd()+self.json.url

        with open(file_path,'r') as f:
            json_data = json.load(f)
       
        # 원하는 호스트에 대해서 source_id 구하기
        for data in json_data['polledData']['spdySessionInfo']:
            
            if(user_input_host in data['host_port_pair']):
                user_host_id = data['source_id']
                print("user_host_id"+str(user_host_id))
            
              
        # 205 == HTTP2_SESSION_RECV_DATA, 188 == HTTP2_SESSION_SEND_HEADERS
        for data in json_data['events']:
            try:
                temp_param = data['params']
                temp_source = data['source']
                temp_type = data['type']
                temp_time = data['time']
                
                if(temp_source['id'] == user_host_id):
                    if(temp_type == 205):
                        if (temp_param['fin'] == True):
                            start = int(temp_source['start_time'])
                            last = int(temp_time)
                            diff = last - start
                            
                            result_send = start
                            result_recv = last
                            result_diff = diff
        
            except:
                pass

        print("first_send : "+ str(result_send))
        print("last recv : " + str(result_recv))
        return(result_diff)




