from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from sc_app.filters import NameFilter
from sc_app.forms import login_form, student_register_form, complaint_form, notification_form
from sc_app.models import Student_Register, Complaint, Notification


# Create your views here.
def index(request):
    return render(request, "index.html")

@login_required(login_url='login_page')
def dashboard(request):
    return render(request, "dashboard.html")
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pass")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect("admin_base")
            if user.is_student:
                return redirect("student_base")
        else:
            messages.info(request, "Invalid Credentials")
    return render(request, "login.html")
def logout_view(request):
    logout(request)
    return redirect("login_page")

######ADMIN########
@login_required(login_url='login_page')
def admin_base(request):
    return render(request, "admin/adminbase.html")
@login_required(login_url='login_page')
def students_data(request):
    data = Student_Register.objects.all()
    nameFilter = NameFilter(request.GET, queryset=data)
    data = nameFilter.qs
    context = {
        'data': data,
        'nameFilter': nameFilter
    }
    return render(request, "admin/student_data_admin.html", context)
@login_required(login_url='login_page')
def view_complaint_admin(request):
    n = Complaint.objects.all
    return  render(request,"admin/view_complaint_admin.html",{"complaint":n})
@login_required(login_url='login_page')
def reply_complaint(request,id):
    feedback=Complaint.objects.get(id=id)
    if request.method== 'POST' :
        r = request.POST.get('reply')
        feedback.reply = r
        feedback.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('view_complaint_admin')
    return render(request,'admin/reply_complaint.html',{'feedback':feedback})

@login_required(login_url='login_page')
def add_notification(request):
    form = notification_form()
    if request.method == 'POST':
        form = notification_form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect("add_notification")
    return render(request, "admin/add_notification.html", {"form": form})
@login_required(login_url='login_page')
def view_notification_admin(request):
    data = Notification.objects.all()
    print(data)
    return render(request, "admin/view_notification_admin.html", {"data": data})
########STUDENT####
@login_required(login_url='login_page')
def student_base(request):
    return render(request, "student/studentbase.html")
def student_registration(request):
    form1 = login_form()
    form2 = student_register_form()
    if request.method == 'POST':
        form1 = login_form(request.POST)
        print(form1)
        form2 = student_register_form(request.POST)
        print(form2)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_student = True
            user.save()
            cus = form2.save(commit=False)
            cus.user = user
            cus.save()
            return redirect("login_page")
    return render(request, "student_registration.html", {'form1': form1, 'form2': form2})
@login_required(login_url='login_page')
def add_complaint_student(request):
    form = complaint_form()
    u = request.user
    if request.method == 'POST':
        form = complaint_form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            return redirect("add_complaint_student")
    return render(request, "student/add_complaint.html", {"form": form})

@login_required(login_url='login_page')
def view_complaint(request):
    data = Complaint.objects.filter(user = request.user)
    print(data)
    return render(request, "student/view_complaint.html", {"data": data})

@login_required(login_url='login_page')
def view_notification_student(request):
    data = Notification.objects.all()
    print(data)
    return render(request, "student/view_notification_student.html", {"data": data})
@login_required(login_url='login_page')
def students_dataview_student(request):
    data = Student_Register.objects.all()
    print(data)
    return render(request, "student/students_data_student.html",{"data": data})