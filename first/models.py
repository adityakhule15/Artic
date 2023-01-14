from django.db import models

class count(models.Model):
    
    like = models.CharField(max_length=10, default=0)
    dislike = models.CharField(max_length=12, default=0)   
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = "count"

class Entry(models.Model):
    
    pk1 = models.IntegerField(primary_key=True, default=1)
    post = models.CharField(max_length=1200)
    id=models.ForeignKey(count,null=True, on_delete=models.SET_NULL, unique=True)
    
    class Meta:
        db_table = "entrys"


