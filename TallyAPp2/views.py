

from django.shortcuts import render,redirect

from TallyAPp2.models import  Create_attendence, Create_employeegroup, Currency_alt, E_found_trasfer, Employee, Rounding, add_bank, compute_information, create_payhead,currencyAlteration, emp_category, gratuity, salary, unit_compound, unit_simple

# Create your views here.
def base(request):
    return render(request,'index.html')

def home(request):
    att1=Create_attendence.objects.count()
    uni1=unit_simple.objects.count()
    uni2=unit_compound.objects.count()
    uni3=uni1+uni2
    cur3=currencyAlteration.objects.count()
    empg=Create_employeegroup.objects.count()
    emp=Employee.objects.count()
    context={'att1':att1,'uni3':uni3,'cur3':cur3,'empg':empg,'emp':emp}
    return render(request,'st_home.html',context)

#  units------

def statistics_units(request):
    sunits=unit_simple.objects.all()
    cunits=unit_compound.objects.all()
    uni1=unit_simple.objects.count()
    uni2=unit_compound.objects.count()
    uni3=uni1+uni2
    context={'sunits':sunits,'cunits':cunits,'uni3':uni3}
    return render(request,'st_units.html',context) 

def statistics_unit_alter(request,pk):
    uni=unit_simple.objects.filter(id=pk)
    context={'uni':uni}
    return render(request,'st_unit_alter.html',context)   

def statistics_su_alter(request,pk):
    if request.method=='POST':
        sgrp =unit_simple.objects.get(id=pk)
        sgrp.symbol = request.POST.get('symbol')
        sgrp.formal_name = request.POST.get('formal_name')
        sgrp.decimal = request.POST.get('decimal')
        sgrp.uqc = request.POST.get('uqc')
        sgrp.save()
        return redirect('statistics_units')
    return render(request, 'st_units.html')     

def statistics_cunit_alter(request,pk):
    uni=unit_compound.objects.filter(id=pk)
    uuu=unit_simple.objects.all()
    context={'uni':uni,'uuu':uuu}
    return render(request,'st_unitalteration.html',context)     

def statistics_cu_alter(request,pk):
    if request.method=='POST':
        cmp =unit_compound.objects.get(id=pk)
        cmp.f_unit = request.POST.get('first_unit')
        cmp.conversion = request.POST.get('conversion')
        cmp.s_unit = request.POST.get('second_unit')
        cmp.save()
        return redirect('statistics_units')
    return render(request, 'st_units.html')   



#  currencies-----           

def statistics_currencies(request):
    currencyd=currencyAlteration.objects.filter(id=1)
    currencydff=currencyAlteration.objects.all().exclude(id=1)
    currency=Currency_alt.objects.all()
    cur3=currencyAlteration.objects.count()
    context={'currencyd':currencyd,'cur3':cur3,'currency':currency,'currencydff':currencydff}
    return render(request,'st_currencies.html',context)  

def statistics_curr_alter(request,pk):
    curr=currencyAlteration.objects.filter(id=pk)
    context={'curr':curr}
    return render(request,'st_curr_alter.html',context)    

def statistics_cdef_alt(request,pk):
    if request.method=='POST':
        cur =currencyAlteration.objects.get(id=pk)
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
        return redirect('statistics_currencies')
    return render(request, 'st_currencies.html')       

def statistics_curr_alter2(request,pk):
    curr=currencyAlteration.objects.filter(id=pk)
    curr1=Currency_alt.objects.filter(currencyAlteration_id=pk)
    context={'curr':curr,'curr1':curr1}
    return render(request,'st_currency_alter2.html',context)    



def statistics_curr_alt(request,pk):
    if request.method=='POST':
        curr = currencyAlteration.objects.get(id=pk)
        curr.Symbol=request.POST.get('symbol')
        curr.FormalName=request.POST.get('name')
        curr.ISOCurrency=request.POST.get('iso')
        curr.DecimalPlace=request.POST.get('numdec')
        curr.showAmount=request.POST.get('amount')
        curr.suffixSymbol=request.POST.get('suffix')
        curr.AddSpace=request.POST.get('symam')
        curr.wordRep=request.POST.get('amodec')
        curr.DecimalWords=request.POST.get('decwo')

        curr.stddate=request.POST.get('standate')
        curr.stdrate=request.POST.get('stdrate')
        curr.selldate=request.POST.get('selldate')
        curr.selvorate=request.POST.get('selvrate')
        curr.sellrate=request.POST.get('selsrate')
        curr.buydate=request.POST.get('buydate')
        curr.buyvorate=request.POST.get('buyvrate')
        curr.buyrate=request.POST.get('buysrate')
         
        curr.save()                     
        return redirect('statistics_currencies')
    return render(request,'currencies.html')      

#  Attendence / Production types -----       

def statistics_atten_prod(request):
    attendance=Create_attendence.objects.all()
    att1=Create_attendence.objects.count()
    context={'att1':att1,'attendance':attendance}
    return render(request,'st_attend_prod.html',context)   

def statistics_atten_alt(request,pk):
    att=Create_attendence.objects.filter(id=pk)
    attendance=Create_attendence.objects.all()
    context={'att':att,'attendance':attendance}
    return render(request,'st_attendance_alter.html',context)    

def statistics_atten_alter(request,pk):
    if request.method=='POST':
        attend =Create_attendence.objects.get(id=pk)
        attend.name = request.POST.get('name')
        attend.alias = request.POST.get('alias')
        attend.under = request.POST.get('under_name')
        attend.type = request.POST.get('attendance')
        attend.period = request.POST.get('period')
        attend.units = request.POST.get('units')
        attend.save()
        return redirect('statistics_atten_prod')
    return render(request, 'st_attend_prod.html')    

def statistics_att_create(request):
    aaa = Create_attendence.objects.all()
    context = {'aaa':aaa}
    return render(request,'st_attend_create.html',context)    

def statistics_add_attend(request):
    if request.method=='POST':
        name = request.POST.get('name')
        alias = request.POST.get('alias')
        under_name = request.POST.get('show_amt')
        attendance = request.POST.get('attendance')
        period = request.POST.get('period')
        atten = Create_attendence(name=name,
                                   alias=alias,
                                   under=under_name,
                                   type=attendance,
                                   period=period)
        atten.save()
        return redirect('statistics_atten_prod')
    return render(request, 'st_attend_prod.html')


#  Employee Groups---------

def statistics_emp_groups(request):
    p_cost=emp_category.objects.all()
    empg=Create_employeegroup.objects.all()
    cost=emp_category.objects.count()
    empg1=Create_employeegroup.objects.count()
    context={'p_cost':p_cost,'empg':empg,'empg1':empg1,'cost':cost}
    return render(request,'st_employee_group.html',context)  

  
def statistics_p_cost(request,pk):
    pcos=emp_category.objects.filter(id=pk)
    context={'pcos':pcos}
    return render(request,'st_pcost_alter.html',context)  

def statistics_pcost_alt(request,pk):
    if request.method=='POST':
        pcost =emp_category.objects.get(id=pk)
        pcost.cat_name = request.POST.get('name')
        pcost.cat_alias = request.POST.get('alias')
        pcost.revenue_items = request.POST.get('revenue')
        pcost.non_revenue_items = request.POST.get('non_revenue')
        pcost.save()
        return redirect('statistics_emp_groups')
    return render(request, 'st_employee_group.html')      
     

def statistics_eg_alt(request,pk):
    empalter=Create_employeegroup.objects.filter(id=pk)
    emp=Create_employeegroup.objects.all()
    context={'empalter':empalter,'emp':emp}
    return render(request,'st_emp_group_alter.html',context)    

def statistics_empgrp_alt(request,pk):
    if request.method=='POST':
        empga =Create_employeegroup.objects.get(id=pk)
        empga.name = request.POST.get('name')
        empga.alias = request.POST.get('alias')
        empga.under_name = request.POST.get('under_name')
        empga.salary_details = request.POST.get('salary')
        empga.save()
        return redirect('statistics_emp_groups')
    return render(request, 'st_employee_group.html')      

def statistics_empg_dtls(request,pk):
    empgd=Create_employeegroup.objects.filter(id=pk)
    epay=create_payhead.objects.all()
    if request.method=='POST':
        name1=request.POST['name']
        under=request.POST['under']
        effect=request.POST['effective']
        pay=request.POST['payhead']
        rate=request.POST['rate']
        per=request.POST['per']
        payhead=request.POST['payheaad_type']
        calculation=request.POST['calculation_type']
        #save salary
        std=salary(name=name1,
                   under=under,
                   effective=effect,
                   payhead=pay,
                   rate=rate,
                   per=per,
                   pay_type=payhead,
                   cal_type=calculation,
        )
        std.save()
        return redirect('statistics_emp_groups')
    return render(request,'st_empg_details.html',{'epay':epay,'empgd':empgd}) 


def statistics_create_payhd(request):
    ph=Create_attendence.objects.filter(type="Attendance/Leave with pay")
    ph2=Create_attendence.objects.filter(type="Production")
    std=Create_attendence.objects.all()
    return render(request,'st_pay_head.html',{'std':std,'ph':ph,'ph2':ph2}) 


def statistics_add_payhead(request):
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        pay_head_type=request.POST['payhead']
        income_type=request.POST['income']
        under=request.POST['under']
        affect_net_salary=request.POST['netsalary']
        payslip=request.POST['payslip']
        calculation_of_gratuity=request.POST['caltype']
        calculation_period=request.POST['ctype']
        calculation_type=request.POST['caltype']
        attendence_leave_withpay=request.POST['attendence with pay']
        attendence_leave_with_outpay=request.POST['Attendance with out pay']
        production_type=request.POST['ptype']
        opening_balance=request.POST['balance']

        #compute information
        compute=request.POST['compute']
        effective_from=request.POST['effective_from']
        # amount_greaterthan=request.POST['', False]
        amount_upto=request.POST['amount_upto']
        value=request.POST['value']

        #Rounding
        round_method=request.POST['roundmethod']
        limit=request.POST['limit']

        #Gratuity
        days_of_months=request.POST['days_of_months']
        from_date=request.POST['from']
        to=request.POST['to']
        calculation_per_year=request.POST['eligiibility']

        std=create_payhead(name=name,
                           alias=alias,
                           pay_type=pay_head_type,
                           income_type=income_type,
                           under=under,
                           affect_net=affect_net_salary,
                           payslip=payslip,
                           calculation_of_gratuity=calculation_of_gratuity,
                           cal_type=calculation_type,
                           calculation_period=calculation_period,
                           leave_withpay=attendence_leave_withpay,
                           leave_with_out_pay=attendence_leave_with_outpay,
                           production_type=production_type,
                           opening_balance=opening_balance,
                           
        )
        std.save()
        idd=std

        std2=compute_information(Pay_head_id=idd,
                                 compute=compute,
                                 effective_from=effective_from,
                                #  amount_greater=amount_greaterthan,
                                 amount_upto=amount_upto,
                                 value=value,
        )
        std2.save()

        std3=Rounding(pay_head_id=idd,
                     Rounding_Method=round_method,
                     Round_limit=limit,
        )
        std3.save()

        std4=gratuity(pay_head_id=idd,
                     days_of_months=days_of_months,
                     number_of_months_from=from_date,
                     to=to,
                     calculation_per_year=calculation_per_year,
        )
        std4.save()
        return redirect('/')
    return render(request,'st_pay_head.html')  

def statistics_add_salaryd(request,pk):
    if request.method=='POST':
        empga =Create_employeegroup.objects.get(id=pk)
        empga.name = request.POST.get('name')
        empga.alias = request.POST.get('alias')
        empga.under_name = request.POST.get('under_name')
        empga.salary_details = request.POST.get('salary')
        empga.save()
        return redirect('statistics_emp_groups')
    return render(request, 'st_employee_group.html')   


def statistics_empg_create(request):
    aaa = Create_employeegroup.objects.all()
    context = {'aaa':aaa}
    return render(request,'st_create_empg.html',context)     

def statistics_add_empg(request):
    if request.method=='POST':
        name = request.POST.get('name')
        alias = request.POST.get('alias')
        under_name = request.POST.get('show_amt')
        salary_details = request.POST.get('salary')
        atten = Create_attendence(name=name,
                                   alias=alias,
                                   under=under_name,
                                   type=salary_details)
        atten.save()
        return redirect('statistics_emp_groups')
    return render(request, 'st_employee_group.html')    



# Employee -------


def statistics_employee(request):
    p_cost=emp_category.objects.all()
    empg=Create_employeegroup.objects.all()
    emp=Employee.objects.all()
    cost=emp_category.objects.count()
    empg1=Create_employeegroup.objects.count()
    empg2=Employee.objects.count()
    context={'p_cost':p_cost,'empg':empg,'emp':emp,'cost':cost,'empg1':empg1,'empg2':empg2}
    return render(request,'st_employee.html',context)

    
def statistics_emp_alt(request,pk):
    emm=Employee.objects.filter(id=pk)
    empg=Create_employeegroup.objects.all()
    context={'emm':emm,'empg':empg}
    return render(request,'st_employee_alter.html',context)  

  
def statistics_employee_alt(request,pk):
    if request.method=='POST':
        empp =Employee.objects.get(id=pk)
        empp.name =request.POST.get('name')
        empp.alias=request.POST.get('alias')
        empp.under=request.POST.get('under')
        empp.defn_sal=request.POST.get('sal')
        empp.emp_name=request.POST.get('empname')
        empp.emp_desg=request.POST.get('desig')
        empp.fnctn=request.POST.get('fn')
            

        empp.location=request.POST.get('loc')
        empp.gender=request.POST.get('gen')
        empp.blood=request.POST.get('blood')
        empp.parent_name=request.POST.get('prnts')
        empp.spouse_name=request.POST.get('spouse')
        empp.address=request.POST.get('adrs')
        empp.number=request.POST.get('phone')

        empp.email=request.POST.get('email')
        empp.bankdtls=request.POST.get('bank')
        empp.inc_tax_no=request.POST.get('incno')
        empp.aadhar_no=request.POST.get('adhar')
        empp.uan=request.POST.get('uan')
        empp.pfn=request.POST.get('pf')
        empp.pran=request.POST.get('pr')
        empp.esin=request.POST.get('esi')

 
            
        empp.save()
        return redirect('statistics_employee')
    return render(request,'st_employee.html')  
    
 

    
