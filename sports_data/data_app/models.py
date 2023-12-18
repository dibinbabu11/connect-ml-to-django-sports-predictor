from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib
# Create your models here.
Gender=(
    (0,'Female'),
    (1,'Male'),
)

class Data(models.Model):
    name=models.CharField( max_length=250,null=True)
    age=models.PositiveIntegerField(validators =[MinValueValidator(13),MaxValueValidator(19)] ,null=True)
    height=models.PositiveIntegerField(null=True)
    sex=models.PositiveIntegerField(choices=Gender,null=True)
    prediction=models.CharField( max_length=520,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    
    def save(self,*args,**kwargs):
        ml_model=joblib.load('ml_model/ml_sport_model.joblib')
        self.prediction= ml_model.predict([[ self.age,self.height,self.sex ]])
        return super().save(*args,**kwargs)

    class Meta:
        ordering=['-date']

    def __str__(self):
        return self.name
    