
from django.shortcuts import render,redirect

from TallyAPp2.models import  Attendance, Compound_Units,  Currency, Employee, Employee_Group, P_cost_default, Simple_Units, currency_default, payhead

# Create your views here.
def base(request):
    return render(request,'index.html')

def home(request):
    att1=Attendance.objects.count()
    uni1=Simple_Units.objects.count()
    uni2=Compound_Units.objects.count()
    uni3=uni1+uni2
    cur1=currency_default.objects.count()
    cur2=Currency.objects.count()
    cur3=cur1+cur2
    empg=Employee_Group.objects.count()
    emp=Employee.objects.count()
    context={'att1':att1,'uni3':uni3,'cur3':cur3,'empg':empg,'emp':emp}
    return render(request,'home.html',context)


def units(request):
    sunits=Simple_Units.objects.all()
    cunits=Compound_Units.objects.all()
    context={'sunits':sunits,'cunits':cunits}
    return render(request,'units.html',context)    

def currencies(request):
    currencyd=currency_default.objects.all()
    currency=Currency.objects.all()
    
    context={'currencyd':currencyd,'currency':currency}
    return render(request,'currencies.html',context)      

def atten_prod(request):
    attendance=Attendance.objects.all()
    context={'attendance':attendance}
    return render(request,'attend_prod.html',context)   

def emp_groups(request):
    p_cost=P_cost_default.objects.all()
    empg=Employee_Group.objects.all()
    context={'p_cost':p_cost,'empg':empg}
    return render(request,'employye_group.html',context)  

def employee(request):
    p_cost=P_cost_default.objects.all()
    empg=Employee_Group.objects.all()
    emp=Employee.objects.all()
    context={'p_cost':p_cost,'empg':empg,'emp':emp}
    return render(request,'employyee.html',context)      

def curr_alter(request,pk):
    curr=currency_default.objects.filter(id=pk)
    context={'curr':curr}
    return render(request,'curr_alter.html',context)      

def unit_alter(request,pk):
    uni=Simple_Units.objects.filter(id=pk)
    context={'uni':uni}
    return render(request,'unit_alter.html',context)   

def c_unit_alter(request,pk):
    uni=Compound_Units.objects.filter(id=pk)
    uuu=Simple_Units.objects.all()
    context={'uni':uni,'uuu':uuu}
    return render(request,'unitalteration.html',context)       

def curr_alter2(request,pk):
    curr=Currency.objects.filter(id=pk)
    context={'curr':curr}
    return render(request,'currency_alter2.html',context)     

def atten_alter(request,pk):
    att=Attendance.objects.filter(id=pk)
    context={'att':att}
    return render(request,'attendance_alter.html',context)     

def empg_alter(request,pk):
    empalter=Employee_Group.objects.filter(id=pk)
    context={'empalter':empalter}
    return render(request,'emp_group_alter.html',context)    

def empg_details(request,pk):
    empgd=Employee_Group.objects.filter(id=pk)
    context={'empgd':empgd}
    return render(request,'empg_details.html',context)     

def create_pay_head(request):
    return render(request,'pay_head.html')       

def p_cost(request,pk):
    pcos=P_cost_default.objects.filter(id=pk)
    context={'pcos':pcos}
    return render(request,'pcost_alter.html',context)     

def emp_alter(request,pk):
    emm=Employee.objects.filter(id=pk)
    context={'emm':emm}
    return render(request,'employee_alter.html',context)  

def simple_unit_alter(request,pk):
    if request.method=='POST':
        sgrp =Simple_Units.objects.get(id=pk)
        sgrp.symbol = request.POST.get('symbol')
        sgrp.formal_name = request.POST.get('formal_name')
        sgrp.decimal = request.POST.get('decimal')
        sgrp.uqc = request.POST.get('uqc')
        
        
        sgrp.save()
        return redirect('units')
    return render(request, 'units.html')   

def compound_unit_alter(request,pk):
    if request.method=='POST':
        cmp =Compound_Units.objects.get(id=pk)
        cmp.first_unit = request.POST.get('first_unit')
        cmp.formal_name = request.POST.get('formal_name')
        cmp.conversion = request.POST.get('conversion')
        cmp.second_unit = request.POST.get('second_unit')
        
        
        cmp.save()
        return redirect('units')
    return render(request, 'units.html')   

def curr_default_alter(request,pk):
    if request.method=='POST':
        cur =currency_default.objects.get(id=pk)
        cur.Symbol = request.POST.get('c_symbl')
        cur.FormalName = request.POST.get('fname')
        cur.ISOCurrency = request.POST.get('isocode')
        cur.DecimalPlace = request.POST.get('decimal_p')
        cur.showAmount = request.POST.get('show_amt')
        cur.suffixSymbol = request.POST.get('suffix')
        cur.AddSpace = request.POST.get('add_space')
        cur.wordRep = request.POST.get('word_rep')
        cur.DecimalWords = request.POST.get('no_decimal')
        
        
        cur.save()
        return redirect('currencies')
    return render(request, 'currencies.html')      

def currency_altern(request,pk):
    if request.method=='POST':
        calt =Currency.objects.get(id=pk)
        calt.Symbol=request.POST.get('symbol')
        calt.FormalName=request.POST.get('name')
        calt.ISOCurrency=request.POST.get('iso')
        calt.DecimalPlace=request.POST.get('numdec')
        calt.showAmount=request.POST.get('amount')
        calt.suffixSymbol=request.POST.get('suffix')
        calt.AddSpace=request.POST.get('symam')
        calt.wordRep=request.POST.get('amodec')
        calt.DecimalWords=request.POST.get('decwo')
            

        calt.stddate=request.POST.get('standate')
        calt.stdrate=request.POST.get('stdrate')
        calt.selldate=request.POST.get('selldate')
        calt.selvorate=request.POST.get('selvrate')
        calt.sellrate=request.POST.get('selsrate')
        calt.buydate=request.POST.get('buydate')
        calt.buyvorate=request.POST.get('buyvrate')
        calt.buyrate=request.POST.get('buysrate')
 
            
        calt.save()
        return redirect('currencies')
    return render(request,'currencies.html')
       
def attendance_alter(request,pk):
    if request.method=='POST':
        attend =Attendance.objects.get(id=pk)
        attend.name = request.POST.get('name')
        attend.alias = request.POST.get('alias')
        attend.under_name = request.POST.get('under_name')
        attend.attendance = request.POST.get('attendance')
        attend.period = request.POST.get('period')
        attend.units = request.POST.get('units')
        
        
        attend.save()
        return redirect('atten_prod')
    return render(request, 'atten_prod.html')          


def pcost_alter(request,pk):
    if request.method=='POST':
        pcost =P_cost_default.objects.get(id=pk)
        pcost.name = request.POST.get('name')
        pcost.alias = request.POST.get('alias')
        pcost.revenue = request.POST.get('revenue')
        pcost.non_revenue = request.POST.get('non_revenue')
        
        
        
        pcost.save()
        return redirect('emp_groups')
    return render(request, 'employye_group.html')  

def pcost_alter(request,pk):
    if request.method=='POST':
        pcost =P_cost_default.objects.get(id=pk)
        pcost.name = request.POST.get('name')
        pcost.alias = request.POST.get('alias')
        pcost.revenue = request.POST.get('revenue')
        pcost.non_revenue = request.POST.get('non_revenue')
        
        
        
        pcost.save()
        return redirect('emp_groups')
    return render(request, 'employye_group.html')      

def employee_grp_alter(request,pk):
    if request.method=='POST':
        empga =Employee_Group.objects.get(id=pk)
        empga.name = request.POST.get('name')
        empga.alias = request.POST.get('alias')
        empga.under_name = request.POST.get('under_name')
        empga.salary_details = request.POST.get('salary')
        
        
        
        empga.save()
        return redirect('emp_groups')
    return render(request, 'employye_group.html')       

def employee_alter(request,pk):
    if request.method=='POST':
        empp =Employee.objects.get(id=pk)
        empp.name =request.POST.get('name')
        empp.alias=request.POST.get('alias')
        empp.under_name=request.POST.get('under_name')
        empp.doj=request.POST.get('doj')
        empp.salary=request.POST.get('salary')
        empp.doresig=request.POST.get('doresig')
        empp.empno=request.POST.get('empno')
        empp.designation=request.POST.get('desig')
        empp.function_name=request.POST.get('func')
            

        empp.location=request.POST.get('loc')
        empp.gender=request.POST.get('gender')
        empp.dob=request.POST.get('dob')
        empp.bld_grp=request.POST.get('bld_grp')
        empp.father_mother=request.POST.get('fama')
        empp.spouse=request.POST.get('spouse')
        empp.address=request.POST.get('address')
        empp.phn=request.POST.get('phn')

        empp.email=request.POST.get('email')
        empp.bank=request.POST.get('bank')
        empp.incometax=request.POST.get('incno')
        empp.adhar=request.POST.get('adhar')
        empp.uan=request.POST.get('uan')
        empp.pf=request.POST.get('pf')
        empp.pr=request.POST.get('pr')
        empp.esi=request.POST.get('esi')
 
            
        empp.save()
        return redirect('employee')
    return render(request,'employyee.html')       

def attend_create(request):
    aaa = Attendance.objects.all()
    context = {'aaa':aaa}
    return render(request,'attend_create.html',context)    

def add_pay_head(request):
    if request.method=='POST':
        pname=request.POST.get('name')
        palias=request.POST.get('alias')    
        payhead_type=request.POST.get('pay')
        pinc_type=request.POST.get('income_type')
        punder_name=request.POST.get('under')
        pnet_salary=request.POST.get('net_salary')
        ppay_slip_name=request.POST.get('pay_slip')    
        pcurrency_ledger=request.POST.get('currency_ledger')
        pcalculation_type=request.POST.get('calculation_type')
        pround_method=request.POST.get('rounding')
        plimit=request.POST.get('round_limit')    
        pcompute=request.POST.get('compute')
        peffect_from=request.POST.get('effect_from')
        pgrt_than=request.POST.get('grt_than')
        pupto=request.POST.get('amt_upto')    
        pslab=request.POST.get('slab')
        pvalue=request.POST.get('value')
        crs=payhead()
        crs.name=pname 
        crs.alias=palias
        crs.payhead_type=payhead_type
        crs.income_type=pinc_type
        crs.under_name=punder_name 
        crs.net_salary=pnet_salary
        crs.pay_slip_name=ppay_slip_name
        crs.currency_ledger=pcurrency_ledger
        crs.calculation_type=pcalculation_type 
        crs.round_method=pround_method
        crs.limit=plimit
        crs.compute=pcompute
        crs.effect_from=peffect_from 
        crs.grt_than=pgrt_than
        crs.amt_upto=pupto 
        crs.slab=pslab
        crs.value=pvalue
        crs.save() 
        return redirect('/')     