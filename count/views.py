import json
from django.shortcuts import redirect
from count.serializers import CountSerializer, EntrySerializer
from .models import count
from django.views.decorators.csrf import csrf_exempt 
# Create your views here.

@csrf_exempt
def like(request,pk1):
    Entry1=count.objects.filter(id=pk1).all()
    serializer = CountSerializer(Entry1, many = True)
    abc1 = json.dumps(serializer.data)
    abc = json.loads(abc1)
    print(abc)
    c=0
    for p in abc:
        if p['like']:
            c=int(p['like'])+1
    print(c)
    count.objects.filter(id=pk1).update(like=c)
    
    return redirect('/entry/totalentrys')

@csrf_exempt
def dslike(request,pk1):
    Entry1=count.objects.all()
    serializer = EntrySerializer(Entry1, many = True)
    abc1 = json.dumps(serializer.data)
    abc = json.loads(abc1)
    print(pk1)
    c=0
    for p in abc:
        if p['dislike']:
            c=int(p['dislike'])+1
    print(c)
    count.objects.filter(id=pk1).update(dislike=c)
    
    return redirect('/entry/totalentrys')
