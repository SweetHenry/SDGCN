from django.shortcuts import render, redirect
import time
# Create your views here.
def test(request):
    print("hello world")
    return render(request, "test.html")


def page(req, pageName):
    return render(req, pageName)


def text(req):
    txt = req.GET.get('txt')
    target = req.GET.get('aspect')
    # print(text)
    context = dict()
    context["text"] = txt
    context['aspect'] = target
    time.sleep(2.5)
    return render(req, "text.html", context)


def kobe(req):
    return render(req, "kobe.html")


