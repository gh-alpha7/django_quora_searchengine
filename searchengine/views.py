from django.shortcuts import render_to_response,render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .quora_search import f

def post(request):
    
    query=request.GET.get('term')
    if query:
        ans=f(query)
        return render(request,'searchengine/basic.html',{'post':[ans]})
    return render(request,'searchengine/post.html',{})
