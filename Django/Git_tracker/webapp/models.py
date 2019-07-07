from django.db import models
# creating our modles.



class Repo(models.Model):
	r_id =models.AutoField(primary_key=True)
	repo_name=models.CharField(max_length=200)
	url=models.CharField(max_length=200)

class Event(models.Model):
	e_id=models.AutoField(primary_key=True)
	Type=models.CharField(max_length=200)
	r_id=models.ForeignKey('Repo',on_delete=models.CASCADE)
class Actor(models.Model):
	a_id=models.AutoField(primary_key=True)
	login_id=models.IntegerField()
	e_id=models.ForeignKey('Event',on_delete=models.CASCADE)
