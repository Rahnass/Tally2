from django.contrib import admin

from TallyAPp2.models import Accounts, Attendance, Compound_Units, Currency, Employee, Employee_Group, P_cost_default, Simple_Units,  currency_default

# Register your models here.
admin.site.register(currency_default)
admin.site.register(Currency)
admin.site.register(Attendance)
admin.site.register(P_cost_default)
admin.site.register(Employee_Group)
admin.site.register(Employee)
admin.site.register(Simple_Units)
admin.site.register(Compound_Units)
admin.site.register(Accounts)
