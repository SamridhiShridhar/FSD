from .forms import StudentForm, CourseForm 
from .models import Student, Course, Meeting
from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponse

# Create your views here.
def add_student(request): 
    if request.method == 'POST': 
        form = StudentForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('students_list') 
    else: 
        form = StudentForm() 
    return render(request, 'course_registration/add_student.html', {'form': form})

def add_course(request):     
    if request.method == 'POST': 
        form = CourseForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('course_registration')
    else: 
        form = CourseForm() 
    return render(request, 'course_registration/add_course.html', {'form': form}) 
 
def register_student(request):
    if request.method == 'POST': 
        student_name = request.POST.get('student_name')
        course_id = request.POST.get('course_id') 
        if not student_name or not course_id: 
            return render(request, 'course_registration/register_student.html', {'courses': Course.objects.all(), 'error_message': 'Please provide both student name and select a course.'})         
        try: 
            course = get_object_or_404(Course, pk=course_id)
            student = Student.objects.filter(name=student_name).first()
            if not student: 
                return render(request, 'course_registration/register_student.html', {'courses': Course.objects.all(), 'error_message': 'Student does not exist in the database.'}) 
            course.students.add(student)             
            return redirect('course_registration')         
        except Course.DoesNotExist: 
            return render(request, 'course_registration/register_student.html', {'courses': Course.objects.all(), 'error_message': 'Invalid course ID. Please select a valid course.'}) 
    return render(request, 'course_registration/register_student.html', {'courses': Course.objects.all()}) 
 
def course_registration(request): 
    courses = Course.objects.all() 
    return render(request, 'course_registration/course_registration.html', {'courses': courses})

def students_list(request, course_id): 
    course = get_object_or_404(Course, course_id=course_id) 
    students = course.students.all() 
    return render(request, 'course_registration/students_list.html', {'course': course, 'students': students})

def insert_demo(request):
    m=Meeting(meeting_code="m001",meeting_dt="2024-04-10",meeting_subject="WTA",meeting_np=150)
    m=Meeting(meeting_code="m002",meeting_dt="2024-04-10",meeting_subject="WTW",meeting_np=500)
    m.save()
    m=Meeting(meeting_code="m003",meeting_dt="2024-04-10",meeting_subject="Parent Meet",meeting_np=100)
    m.save()
    m=Meeting(meeting_code="m004",meeting_dt="2024-04-10",meeting_subject="Course Attainment",meeting_np=150)
    m.save() 
    m=Meeting(meeting_code="m005",meeting_dt="2024-04-10",meeting_subject="Infrastructure",meeting_np=150)
    m.save()
    return HttpResponse("<h1>Record inserted successfully</h1>")

def update_demo(request):
    m=Meeting.objects.get(meeting_code="m002")
    m.meeting_dt="2024-04-11"
    m.meeting_np=250
    m.save()
    return HttpResponse("<h1>Record updated successfully</h1>")  

def delete_demo(request):
    m=Meeting.objects.get(meeting_code="m004")
    m.delete()
    return HttpResponse("<h1>Record deleted successfully</h1>")

def retreive_demo(request): 
    m=Meeting.objects.filter(Q(meeting_subject__contains = "Meet") & Q(meeting_np__gte = 250))
    result=""
    for meeting in m:
        result+="<p>%s,%s,%s,%d</p>"%(meeting.meeting_code, meeting.meeting_subject,meeting.meeting_dt,meeting.meeting_np)
    return HttpResponse(result)