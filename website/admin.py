from django.contrib import admin

from .models import Home, About, Profile, Portfolio, Category, Skill

admin.site.register(Home)

class ProfileInline(admin.TabularInline): #allows me to add profile section data in the about section
    model = Profile #name of the model to access the fields from
    extra = 1 # extra = 1 means it will show one empty slot for the social media name and link by default

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [ProfileInline,]

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SkillInline,]
    
admin.site.register(Portfolio)

