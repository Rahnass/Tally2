from django.contrib import admin

from TallyAPp2.models import  unit_compound ,unit_simple ,uqcs , currencyAlteration ,Currency_alt ,Create_attendence,emp_category , Create_employeegroup , Employee

# Register your models here.


admin.site.register(Employee)
admin.site.register(Create_employeegroup)
admin.site.register(emp_category)
admin.site.register(Create_attendence)
admin.site.register(Currency_alt)
admin.site.register(currencyAlteration)
admin.site.register(uqcs)
admin.site.register(unit_simple)
admin.site.register(unit_compound)


