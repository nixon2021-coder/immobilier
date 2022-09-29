
from django.contrib import admin

from .models import*
from django.utils.safestring import mark_safe

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('images_view','description' ,'titre','create_at', 'update_at' , 'statut', )
    
    def images_view(self, obj): 
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('description', 'libelle','titre', 'images_view','create_at','update_at' , 'statut',)

    def images_view(self, obj): 
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('description', 'images_view','titre', 'create_at','update_at' , 'statut',)
    def images_view(self, obj): 
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom','prix', 'Message','date','email','numero','create_at','update_at' , 'statut',)

@admin.register(Reseausocial)
class ReseausocialAdmin(admin.ModelAdmin):
    list_display = ('nom', 'Icon','lien','create_at','update_at' , 'statut',)
    

@admin.register(Properties)
class PropertiesAdmin(admin.ModelAdmin):
    list_display = ('description', 'libelle','titre','nom','date','Icon','prix', 'images_view','create_at','update_at' , 'statut',)
    def images_view(self, obj): 
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')


@admin.register(Customers)
class CustomersAmin(admin.ModelAdmin):
    list_display = ('titre','description','nom','images_view','libelle',)
    def images_view(self,obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('images_view','titre','description',)
    def images_view(self,obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')







