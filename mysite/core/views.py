from typing import List
from django.shortcuts import redirect, render
from django.views.generic import TemplateView,ListView
from django.core.files.storage import FileSystemStorage,default_storage
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


# used one when single chart
def chart(request, group_name, protocol_name, host_name, datas_array):

    # Chart data is passed to the `dataSource` parameter, as dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = group_name
    chartConfig["subCaption"] = host_name
    chartConfig["xAxisName"] = "nums"
    chartConfig["yAxisName"] = "ms"
    chartConfig["numberSuffix"] = "ms"
    chartConfig["theme"]="fusion"

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()
    
    how_many_datas = len(datas_array)
    for i in range(how_many_datas):
            chartData[str(i+1)] = datas_array[i]

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
    return  render(request, 'chart.html', {'output' : column2D.render(), 'chartTitle': 'Group : '+ str(group_name)})

# single chart template
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


# multi_chart(request,group_name,host_name, datas_array_h1, datas_array_h2)
def multi_chart(request,group_name,host_name, datas_array_h1, datas_array_h2):
        
        len_h1 = len(datas_array_h1)
        len_h2 = len(datas_array_h2)
        
        len_min = 0

        if (len_h1 > len_h2) : 
                len_min = len_h2 
        else: len_min = len_h1


        categories_list = []
        
        h1_value = []
        h2_value = []
        
        for i in range(len_min):
                categories_list.append( {'label': str(i+1)} )
                h1_value.append( {'value' : str(datas_array_h1[i])} )
                h2_value.append( {'value' : str(datas_array_h2[i])} )


        temp_chart = {
                'chart': {'caption': group_name, 'subcaption': host_name, 'xaxisname': 'nums', 'yaxisname': 'ms', 'formatnumberscale': '0', 'plottooltext': '<b>$dataValue</b> apps were available on <b>$seriesName</b> in $label', 'theme': 'fusion', 'drawcrossline': '0'}, 
                
                'categories': [{'category': categories_list}], 
                
                'dataset': [
                        {'seriesname': 'h1', 'data': h1_value}, 

                        {'seriesname': 'h2', 'data': h2_value}, 
                        ]}
        
        chartObj = FusionCharts( 'mscolumn2d', 'ex1', '600', '400', 'chart-1', 'json', json.dumps(temp_chart))  
        return render(request, 'multi_chart.html', {'output': chartObj.render()})



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


# single - showchart
def show_chart(request,filegroup,pk):
        
        files = File.objects.all()
        group_name = str(filegroup)

        pro_name =''                
        host_name = ''
        datas_array = []
        
        for file in files:
                if file.get_file_group() == group_name :
                        datas_array.append(file.get_data())
                        print(file.get_data())
                        pro_name = file.get_protocol_name()
                        host_name = file.get_host_name()
        
        return chart(request,group_name,pro_name,host_name,datas_array)

# Multi - showchart
def show_multi_chart(request,filegroup,pk):
        
        files = File.objects.all()
        group_name = str(filegroup)
        
        h2_str = ["h2", "H2","http2","HTTP2","http2.0","HTTP2.0"]
        h1_str = ["h1", "H1","http1","HTTP1","http1.1","HTTP1.1"]

        h2_host_name=""
        h1_host_name=""

        datas_array_h1 = []
        datas_array_h2 = []
        
        for file in files:
                if file.get_file_group() == group_name :
                        if(file.get_protocol_name() in h2_str):
                                datas_array_h2.append(file.get_data())
                                print("h2" + str(file.get_data()))
                                h2_host_name =  str(file.get_host_name())
                                # h2_protocol_name = file.get_protocol_name()
                                
                        elif(file.get_protocol_name() in h1_str):
                                datas_array_h1.append(file.get_data())
                                print("h1" + str(file.get_data()))
                                h1_host_name =  str(file.get_host_name())
                                # h1_protocol_name = file.get_protocol_name()
        
        # host 이름 종합하여 보여줄 수 있도록
        host_name = "h2 : " + (h2_host_name) + " & h1 : " + (h1_host_name) 

        return multi_chart(request,group_name,host_name, datas_array_h1, datas_array_h2)

class FileListView(ListView):
        # generic 하게 코드 써보기
        model = File
        template_name = 'file_list.html'
        context_object_name = 'files'