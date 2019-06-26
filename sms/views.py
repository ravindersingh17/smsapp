from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
import json
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sms.models import Sms

@csrf_exempt
def newsms(request):
    with open("/tmp/debug_1.json", "w") as f:
        f.write(json.dumps(request.POST))
    return HttpResponse(json.dumps({"payload": {"success": True, "error": None}}))
    s = Sms(
            from_num = request.POST["from"],
            message = request.POST["message"],
            message_id = request.POST["message_id"],
            sent_to = request.POST["sent_to"],
            secret = request.POST["secret"],
            device_id = request.POST["device_id"],
            sent_timestamp = request.POST["sent_timestamp"]
            )

class IndexView(TemplateView):
    template_name = "index.html"

