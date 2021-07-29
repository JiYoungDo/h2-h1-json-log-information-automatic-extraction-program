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



# Loading Data from a Ordered Dictionary
# Example to create a column 2D chart with the chart data passed as Dictionary format.
# The `chart` method is defined to load chart data from Dictionary.

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

# single
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


# multi_chart_template
def multi_chart(request):
   chartObj = FusionCharts( 'mscolumn2d', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "App Publishing Trend",
    "subcaption": "2012-2016",
    "xaxisname": "Years",
    "yaxisname": "Total number of apps in store",
    "formatnumberscale": "1",
    "plottooltext": "<b>$dataValue</b> apps were available on <b>$seriesName</b> in $label",
    "theme": "fusion",
    "drawcrossline": "1"
  },
  "categories": [
    {
      "category": [
        {
          "label": "2012"
        },
        {
          "label": "2013"
        },
        {
          "label": "2014"
        },
        {
          "label": "2015"
        },
        {
          "label": "2016"
        }
      ]
    }
  ],
  "dataset": [
    {
      "seriesname": "iOS App Store",
      "data": [
        {
          "value": "125000"
        },
        {
          "value": "300000"
        },
        {
          "value": "480000"
        },
        {
          "value": "800000"
        },
        {
          "value": "1100000"
        }
      ]
    },
    {
      "seriesname": "Google Play Store",
      "data": [
        {
          "value": "70000"
        },
        {
          "value": "150000"
        },
        {
          "value": "350000"
        },
        {
          "value": "600000"
        },
        {
          "value": "1400000"
        }
      ]
    },
    {
      "seriesname": "Amazon AppStore",
      "data": [
        {
          "value": "10000"
        },
        {
          "value": "100000"
        },
        {
          "value": "300000"
        },
        {
          "value": "600000"
        },
        {
          "value": "900000"
        }
      ]
    }
  ]
}""")
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


class FileListView(ListView):
        # generic 하게 코드 써보기
        model = File
        template_name = 'file_list.html'
        context_object_name = 'files'