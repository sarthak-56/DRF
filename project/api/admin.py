from django.contrib import admin
from api.models import Company,Employee

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','your_field')
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','position')

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)