
from django.db import models 


# Create your models here.

class Companies(models.Model):
    d_path=models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=255)
    mailing_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10,null=True)
    telephone = models.CharField(max_length=20,null=True)
    mobile = models.CharField(max_length=15,null=True)
    fax = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=240, null=True)
    website = models.CharField(max_length=100,null=True)
    currency_symbol = models.CharField(max_length=20)
    formal_name = models.CharField(max_length=20)
    fin_begin = models.DateField()
    books_begin = models.DateField()
    fin_end = models.DateField()
    status=models.BooleanField(default=True)


class unit_simple(models.Model):
    type=models.CharField(max_length=100)
    symbol=models.CharField(max_length=100)
    formal_name=models.CharField(max_length=100)
    uqc=models.CharField(max_length=100)
    decimal=models.IntegerField()
    
    def __str__(self):
        return self.symbol
    
class unit_compound(models.Model):
    typ=models.CharField(max_length=100)
    f_unit=models.CharField(max_length=100,null=True)
    conversion=models.IntegerField()
    s_unit=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.f_unit

class uqcs(models.Model):
    uqc_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.uqc_name


class currencyAlteration(models.Model):
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

class Currency_alt(models.Model):
    currencyAlteration=models.ForeignKey(currencyAlteration, on_delete=models.CASCADE, null=True)
    stddate=models.CharField(max_length=255,blank=True,null=True)
    stdrate=models.CharField(max_length=255,default='null')
    selldate=models.CharField(max_length=255,blank=True,null=True)
    selvorate=models.CharField(max_length=255,default='null')
    sellrate=models.CharField(max_length=255,default='null')
    buydate=models.CharField(max_length=255,blank=True,null=True)
    buyvorate=models.CharField(max_length=255,default='null')
    buyrate=models.CharField(max_length=255,default='null')
    
    def __str__(self):
        return self.currencyAlteration.Symbol

class Create_attendence(models.Model):
    name =models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    type =models.CharField(max_length=225)
    period=models.CharField(max_length=225,default='null',blank=True)
    units=models.CharField(max_length=225,default='null',blank=True)     

    def __str__(self):
        return self.name  


class emp_category(models.Model):
    cat_name= models.CharField(max_length=225)
    cat_alias= models.CharField(max_length=225)
    revenue_items=models.CharField(max_length=225)
    non_revenue_items=models.CharField(max_length=225)

    def __str__(self):
        return self.cat_name

class Create_employeegroup(models.Model):
    name =models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    define_salary=models.CharField(max_length=225) 

    def __str__(self):
        return self.name

class Employee(models.Model):

    name = models.CharField(max_length=225)
    alias= models.CharField(max_length=225)
    under= models.CharField(max_length=225)
    date_join = models.DateField()
    defn_sal = models.CharField(max_length=225)
    emp_name = models.CharField(max_length=225)
    emp_desg = models.CharField(max_length=225)
    fnctn = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    gender= models.CharField(max_length=225)
    dob = models.DateField()
    blood = models.CharField(max_length=225)
    parent_name =models.CharField(max_length=225)
    spouse_name =models.CharField(max_length=225)
    address =models.CharField(max_length=225)
    number =models.CharField(max_length=225)
    email =models.CharField(max_length=225)
    inc_tax_no =models.CharField(max_length=225)
    aadhar_no=models.CharField(max_length=225)
    uan =models.CharField(max_length=225)
    pfn =models.CharField(max_length=225)
    pran =models.CharField(max_length=225)
    esin =models.CharField(max_length=225)
    bankdtls=models.CharField(max_length=225)    

    def __str__(self):
        return self.name

class create_payhead(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    pay_type=models.CharField(max_length=225)
    income_type=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    affect_net=models.CharField(max_length=225)
    payslip=models.CharField(max_length=225)
    calculation_of_gratuity=models.CharField(max_length=225)
    cal_type=models.CharField(max_length=225)
    calculation_period=models.CharField(max_length=225)
    leave_withpay=models.CharField(max_length=225)
    leave_with_out_pay=models.CharField(max_length=225)
    production_type=models.CharField(max_length=225)
    opening_balance=models.CharField(max_length=225)

class compute_information(models.Model):
    Pay_head_id = models.ForeignKey(create_payhead, on_delete=models.CASCADE, null=True, blank=True)
    compute=models.CharField(max_length=225,default="Null")
    effective_from=models.CharField(max_length=225,default="NULL")
    amount_greater=models.CharField(max_length=225,default="NULL")
    amount_upto=models.CharField(max_length=225,default="NULL")
    slab_type=models.CharField(max_length=225,default="NULL")
    value=models.CharField(max_length=225,default="NULL")



class Rounding(models.Model):
    pay_head_id = models.ForeignKey(create_payhead, on_delete=models.CASCADE, null=True, blank=True)
    Rounding_Method =models.CharField(max_length=225,default="Null",blank=True)
    Round_limit = models.CharField(max_length=22,default="Null",blank=True)


class gratuity(models.Model):
    pay_head_id=models.ForeignKey(create_payhead, on_delete=models.CASCADE, null=True, blank=True)
    days_of_months=models.CharField(max_length=225)
    number_of_months_from=models.CharField(max_length=225)
    to=models.CharField(max_length=225)
    calculation_per_year=models.CharField(max_length=225)


class salary(models.Model):
    name=models.CharField(max_length=225)
    under=models.CharField(max_length=225) 
    effective=models.CharField(max_length=225)
    payhead=models.CharField(max_length=225)
    rate=models.CharField(max_length=225)
    per=models.CharField(max_length=225)
    pay_type=models.CharField(max_length=225)
    cal_type=models.CharField(max_length=225)

class add_bank(models.Model):
    employee_id= models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    Acount_No=models.CharField(max_length=225)
    IFSC_code=models.CharField(max_length=225)
    Bank_name=models.CharField(max_length=225)
    Branch_name=models.CharField(max_length=225)
    Transaction_type=models.CharField(max_length=225)


class E_found_trasfer(models.Model):
    employee_id= models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    Acount_No=models.CharField(max_length=225)
    IFSC_code=models.CharField(max_length=225)
    Bank_name=models.CharField(max_length=225)
    Cheque=models.CharField(max_length=225)    