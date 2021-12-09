from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# application/write_data.pyをインポートする
from .application import write_data


class SampleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app_folder/index.html')
index = SampleView.as_view()
# Create your views here.
# def index(req):
#     return render(req, 'index.html')

# ajaxでurl指定したメソッド
def call_write_data(req):
    # if req.method == 'GET':
        # write_data.pyのwrite_csv()メソッドを呼び出す。
        # ajaxで送信したデータのうち"input_data"を指定して取得する。
        # write_data.deco(req.GET.get("JSON"))
    write_data.save(req.GET.get("input_data"))
    write_data.save2(req.GET.get("input_data2"))
    write_data.save3(req.GET.get("input_data3"))
    write_data.save4(req.GET.get("input_data4"))
    write_data.save5(req.GET.getlist("input_data5[]"))
    write_data.write_csv()
    return HttpResponse()
