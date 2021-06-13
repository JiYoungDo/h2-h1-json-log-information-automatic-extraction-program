from typing import List
from django.shortcuts import redirect, render
from django.views.generic import TemplateView,ListView
from django.core.files.storage import FileSystemStorage
from django.views.generic.base import View

from .forms import FileForm
from .models import File

import json
import os

from django.shortcuts import render
from django.http import HttpResponse

from collections import OrderedDict

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .fusioncharts import FusionCharts

# Loading Data from a Ordered Dictionary
# Example to create a column 2D chart with the chart data passed as Dictionary format.
# The `chart` method is defined to load chart data from Dictionary.

def chart(request, group_name, protocol_name, host_name, datas_array):

    # Chart data is passed to the `dataSource` parameter, as dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = group_name
    chartConfig["subCaption"] = protocol_name + host_name
    chartConfig["xAxisName"] = "nums"
    chartConfig["yAxisName"] = "ms"
    chartConfig["numberSuffix"] = "ms"
    chartConfig["theme"]="fusion"

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()
    how_many_datas = datas_array.size()
    for i in range(how_many_datas):
            chartData[str(i+1)] = datas_array[i]
    
    
    '''chartData["1"] = 290
    chartData["2"] = 260
    chartData["3"] = 180
    chartData["4"] = 140
    chartData["5"] = 115
    chartData["6"] = 100
    chartData["7"] = 30
    chartData["8"] = 30'''


    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData` array into a format that can be consumed by FusionCharts.
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

    # Iterate through the data in `chartData` and insert in to the `dataSource['data']` list.
    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json", dataSource)
    return  render(request, 'chart.html', {'output' : column2D.render(), 'chartTitle': 'Simple Chart Using Array'})

def chart_template(request):

    # Chart data is passed to the `dataSource` parameter, as dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Countries With Most Oil Reserves [2017-18]"
    chartConfig["subCaption"] = "In MMbbl = One Million barrels"
    chartConfig["xAxisName"] = "Country"
    chartConfig["yAxisName"] = "Reserves (MMbbl)"
    chartConfig["numberSuffix"] = "K"
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()
    chartData["Venezuela"] = 290
    chartData["Saudi"] = 260
    chartData["Canada"] = 180
    chartData["Iran"] = 140
    chartData["Russia"] = 115
    chartData["UAE"] = 100
    chartData["US"] = 30
    chartData["China"] = 30


    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData` array into a format that can be consumed by FusionCharts.
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

    # Iterate through the data in `chartData` and insert in to the `dataSource['data']` list.
    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json", dataSource)

    return  render(request, 'chart.html', {'output' : column2D.render(), 'chartTitle': 'Simple Chart Using Array'})


class Home(TemplateView):
        template_name = 'base.html'

def upload(request):
        context = {}
        if request.method == 'POST':
                uploaded_file = request.FILES['document']
                fs = FileSystemStorage()
                
                name = fs.save(uploaded_file.name, uploaded_file)
                # url = fs.url(name)
                context['url'] = fs.url(name)
                
                print(uploaded_file.name)
                print(uploaded_file.size )
                #print(url)
        return render(request, 'upload.html', context) 

def file_list(request):
        files = File.objects.all()
        return render(request, 'file_list.html',{
                'files': files
        })

def upload_file(request):
        if request.method == 'POST':
                form = FileForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save()
                        return redirect('file_list')
        else:
                form = FileForm()
        return render(request, 'file_upload.html',{
                'form': form
        }) 


def delete_file(request,pk):
        if request.method == 'POST':
                file = File.objects.get(pk=pk)
                file.delete()
        return redirect('file_list')


def show_chart(request):
        
        files = File.objects.all()

        #file = File.objects.get(pk=pk)
        #group_name = file.get_file_group()
        group_name = 'h2_img_10'
        # group_name_list 길이 만큼 반복문을 돌면서 해당 그룹에 해당하는 파일의 datas 값 가져오기 
        # > chart 로 넘겨 줘야 한다.
        
        pro_name =''                
        host_name = ''
        datas_array = []
        
        for file in files:
                if file.get_file_group() == group_name :
                        datas_array.append(get_data(file))
                        pro_name = file.get_protocol_name()
                        host_name = file.get_host_name()
        
        chart(request,group_name,pro_name,host_name,datas_array)


def get_data(file):
        user_input_host = file.hostname
        user_host_id = 0 # temp 값
        result_send = 0
        result_recv = 0
        result_diff = 0

        '''파일에서 해당 url 에 대한 '''
        
        with open(file.json.url,'r') as f:
            json_data = json.load(f)
            
        # 원하는 호스트에 대해서 source_id 구하기
        for data in json_data['polledData']['spdySessionInfo']:
            if(user_input_host in data['host_port_pair']):
                user_host_id = data['source_id']
            
                
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

class FileListView(ListView):
        # generic 하게 코드 써보기
        model = File
        template_name = 'file_list.html'
        context_object_name = 'files'