from django.shortcuts import render, redirect
from count.models import Entry, count
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from first.serializers import OpSerializer 

@csrf_exempt
def add(request):
    if request.method == 'POST':
        Entry1=count.objects.all()
        serializer = OpSerializer(Entry1, many = True)
        abc1 = json.dumps(serializer.data)
        abc = json.loads(abc1)
        print(abc)
        c=0
        for p in abc:
            if p['id']>=0:
                c=int(p['id'])+1
        fprod = count()
        fprod.id=c  
        fprod.save();
        prod = Entry()
        prod.pk1=c
        prod.post=request.POST.get('post')      
        prod.save();

        Entry.objects.filter(pk1=c).update(id_id=c)      
        print(c) 
                
        return redirect('/entry/totalentrys')

    else:
        return render(request,'add.html')  

@csrf_exempt
def totalentrys(request):
   
    op = Entry.objects.all()
    
    return render(request, 'totalentrys.html', {'exicative':op})
    

