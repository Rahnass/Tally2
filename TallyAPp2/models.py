
from django.db import models 


# Create your models here.

class Accounts(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.name




class currency_default(models.Model):
    Symbol = models.CharField(max_length=255)
    FormalName = models.CharField(max_length=255)
    ISOCurrency = models.CharField(max_length=30,null=True)
    DecimalPlace = models.IntegerField()
    showAmount = models.CharField(max_length=20)
    suffixSymbol = models.CharField(max_length=20)
    AddSpace = models.CharField(max_length=20)
    wordRep = models.CharField(max_length=255,null=True)
    DecimalWords = models.IntegerField()

    def __str__(self):
        return self.Symbol




class Compound_Units(models.Model):
    type=models.CharField(max_length=50,blank=True,null=True,default='Compound')  
    first_unit=models.CharField(max_length=50,blank=True,null=True)
    conversion=models.CharField(max_length=50,blank=True,null=True)
    second_unit=models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.first_unit      

class Simple_Units(models.Model):
    type=models.CharField(max_length=100,null=True,blank=True,default='Simple')
    symbol=models.CharField(max_length=20,null=True,blank=True)
    formal_name=models.CharField(max_length=50,blank=True,null=True)
    uqc=models.CharField(max_length=50,blank=True,null=True)
    decimal=models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return self.formal_name            

class Currency(models.Model):
    Symbol = models.CharField(max_length=255,blank=True,null=True)
    FormalName = models.CharField(max_length=255,blank=True,null=True)
    ISOCurrency = models.CharField(max_length=30,blank=True,null=True)
    DecimalPlace = models.IntegerField(blank=True,null=True)
    showAmount = models.CharField(max_length=20,blank=True,null=True)
    suffixSymbol = models.CharField(max_length=20,blank=True,null=True)
    AddSpace = models.CharField(max_length=20,blank=True,null=True)
    wordRep = models.CharField(max_length=255,blank=True,null=True)
    DecimalWords = models.IntegerField(blank=True,null=True)
    stddate=models.CharField(max_length=255,blank=True,null=True)
    stdrate=models.CharField(max_length=255,blank=True,null=True)
    selldate=models.CharField(max_length=255,blank=True,null=True)
    selvorate=models.CharField(max_length=255,blank=True,null=True)
    sellrate=models.CharField(max_length=255,blank=True,null=True)
    buydate=models.CharField(max_length=255,blank=True,null=True)
    buyvorate=models.CharField(max_length=255,blank=True,null=True)
    buyrate=models.CharField(max_length=255,blank=True,null=True)       

    def __str__(self):
        return self.Symbol



class Attendance(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    alias=models.CharField(max_length=100,null=True,blank=True)
    under_name=models.CharField(max_length=50,null=True,blank=True)
    attendance=models.CharField(max_length=50,null=True,blank=True)
    period=models.CharField(max_length=50,null=True,blank=True)
    units=models.CharField(max_length=50,null=True,blank=True)    

    def __str__(self):
        return self.name   

class P_cost_default(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    alias=models.CharField(max_length=100,null=True,blank=True)
    revenue=models.CharField(max_length=50,null=True,blank=True)
    non_revenue=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name

class Employee_Group(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    alias=models.CharField(max_length=100,null=True,blank=True)
    under_name=models.CharField(max_length=50,null=True,blank=True)
    salary_details=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    alias=models.CharField(max_length=100,null=True,blank=True)
    under_name=models.CharField(max_length=50,null=True,blank=True)
    doj=models.CharField(max_length=30,null=True,blank=True)
    salary=models.CharField(max_length=50,null=True,blank=True)
    doresig=models.CharField(max_length=50,null=True,blank=True)
    empno=models.CharField(max_length=20,null=True,blank=True)
    designation=models.CharField(max_length=20,null=True,blank=True)
    function_name=models.CharField(max_length=20,null=True,blank=True)
    location=models.CharField(max_length=20,null=True,blank=True)
    gender=models.CharField(max_length=20,null=True,blank=True)
    dob=models.CharField(max_length=20,null=True,blank=True)
    bld_grp=models.CharField(max_length=20,null=True,blank=True)
    father_mother=models.CharField(max_length=20,null=True,blank=True)
    spouse=models.CharField(max_length=20,null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    phn=models.CharField(max_length=20,null=True,blank=True)
    email=models.CharField(max_length=20,null=True,blank=True)
    bank=models.CharField(max_length=50,null=True,blank=True)
    incometax=models.CharField(max_length=20,null=True,blank=True)
    adhar=models.CharField(max_length=20,null=True,blank=True)
    uan=models.CharField(max_length=20,null=True,blank=True)
    pf=models.CharField(max_length=20,null=True,blank=True)
    pr=models.CharField(max_length=20,null=True,blank=True)
    esi=models.CharField(max_length=20,null=True,blank=True)        

    def __str__(self):
        return self.name


class payhead(models.Model):
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    payhead_type=models.CharField(max_length=100,null=True)
    income_type=models.CharField(max_length=100,null=True)
    under_name=models.CharField(max_length=100,null=True)
    net_salary=models.CharField(max_length=100,null=True)
    pay_slip_name=models.CharField(max_length=100,null=True)
    currency_ledger=models.CharField(max_length=100,null=True)
    calculation_type=models.CharField(max_length=100,null=True)
    round_method=models.CharField(max_length=100,null=True)
    limit=models.CharField(max_length=100,null=True)
    compute=models.CharField(max_length=100,null=True)
    effect_from=models.CharField(max_length=100,null=True)
    grt_than=models.CharField(max_length=100,null=True)
    amt_upto=models.CharField(max_length=100,null=True)
    slab=models.CharField(max_length=100,null=True)
    value=models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.name