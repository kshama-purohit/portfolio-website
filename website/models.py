from django.db import models

class Home(models.Model):
    name = models.CharField(max_length=50)
    greetings_1 = models.CharField(max_length=50)
    greetings_2 = models.CharField(max_length=50)
    picture = models.ImageField(upload_to = 'home/')
    updated = models.DateTimeField(auto_now = True) #auto saves the last time the when the model was updated

    def __str__(self): #str = string
        return self.name #what shows up in the home section list on the admin site to denote a specific entry
    
class About(models.Model):
    heading = models.CharField(max_length = 50)
    desc = models.TextField()
    career = models.CharField(max_length = 100)
    profile_img = models.ImageField(upload_to='profile/')
    updated = models.DateTimeField(auto_now = True) #auto saves the last time the when the model was updated
    
    def __str__(self):
        return self.career

class Profile(models.Model):
    about_profile = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length = 10)
    link = models.URLField(max_length = 200)

class Category(models.Model):
    name = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now = True)

    def __str__ (self):
        return self.name
    
class Skill(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    def __str__ (self):
        return self.name

class Portfolio(models.Model):
    image = models.ImageField(upload_to = 'portfolio/')
    link = models.URLField(max_length = 200
                           )

    def __str__(self):
        return f'Portfolio {self.id}'