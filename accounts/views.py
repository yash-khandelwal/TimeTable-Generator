from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from dateutil.relativedelta import *
from datetime import *
from django.utils.timezone import make_aware
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from accounts.forms import SignupForm, LoginForm
from accounts import forms
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from accounts.models import User,Batch, Result, ResultTeacher
from django.db.models import Count
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.views.generic import (RedirectView, View, TemplateView,
                                    ListView, DetailView, CreateView, UpdateView,
                                    DeleteView)
from dateutil.relativedelta import relativedelta
from braces import views
from resource_data.models import Branch, Course, Teacher, Room
from django.shortcuts import render_to_response
import json
from django import template
# Create your views here.
batches = []


def fetch_data(request):
    if request.is_ajax():
        data = request.POST.get("param")
        print(data)
        # print(type(data))
        data_js = json.loads(data)
        keys = list(data_js.keys())
        # print(keys)
        # print('lalala')
        x = json.loads(data_js["CSE3"])
        # print(x)
        # print(data_js['CSE3'][0])
        size = len(x)
        # print(size)


        for i in range(size):
            if(i%5==0 and i%2!=0):
                res = Result()
                res.save()
            cse1 = '0'
            if('CSE1' in keys):
                cse1 = json.loads(data_js['CSE1'])[i]
            cse2 = '0'
            if('CSE2' in keys):
                cse2 = json.loads(data_js['CSE2'])[i]
            cse3 = '0'
            if('CSE3' in keys):
                cse3 = json.loads(data_js['CSE3'])[i]
            cse4 = '0'
            if('CSE4' in keys):
                cse4 = json.loads(data_js['CSE4'])[i]
            cse5 = '0'
            if('CSE5' in keys):
                cse5 = json.loads(data_js['CSE5'])[i]
            cse6 = '0'
            if('CSE6' in keys):
                cse6 = json.loads(data_js['CSE6'])[i]
            cse7 = '0'
            if('CSE7' in keys):
                cse7 = json.loads(data_js['CSE7'])[i]
            cse8 = '0'
            if('CSE8' in keys):
                cse8 = json.loads(data_js['CSE8'])[i]

            ece1 = '0'
            if('ECE1' in keys):
                ece1 = json.loads(data_js['ECE1'])[i]
            ece2 = '0'
            if('ECE2' in keys):
                ece2 = json.loads(data_js['ECE2'])[i]
            ece3 = '0'
            if('ECE3' in keys):
                ece3 = json.loads(data_js['ECE3'])[i]
            ece4 = '0'
            if('ECE4' in keys):
                ece4 = json.loads(data_js['ECE4'])[i]

            ece5 = '0'
            if('ECE5' in keys):
                ece5 = json.loads(data_js['ECE5'])[i]
            ece6 = '0'
            if('ECE6' in keys):
                ece6 = json.loads(data_js['ECE6'])[i]
            ece7 = '0'
            if('ECE7' in keys):
                ece7 = json.loads(data_js['ECE7'])[i]
            ece8 = '0'
            if('ECE8' in keys):
                ece8 = json.loads(data_js['ECE8'])[i]

            it1 = '0'
            if('IT1' in keys):
                it1 = json.loads(data_js['IT1'])[i]
            it2 = '0'
            if('IT2' in keys):
                it2 = json.loads(data_js['IT2'])[i]
            it3 = '0'
            if('IT3' in keys):
                it3 = json.loads(data_js['IT3'])[i]
            it4 = '0'
            if('IT4' in keys):
                it4 = json.loads(data_js['IT4'])[i]
            it5 = '0'
            if('IT5' in keys):
                it5 = json.loads(data_js['IT5'])[i]
            it6 = '0'
            if('IT6' in keys):
                it6 = json.loads(data_js['IT6'])[i]
            it7 = '0'
            if('IT7' in keys):
                it7 = json.loads(data_js['IT7'])[i]
            it8 = '0'
            if('IT8' in keys):
                it8 = json.loads(data_js['IT8'])[i]

            res = Result(cse1=cse1, cse2=cse2, cse3=cse3, cse4=cse4, cse5=cse5, cse6=cse6, cse7=cse7, cse8=cse8, ece1=ece1, ece2=ece2, ece3=ece3, ece4=ece4, ece5=ece5, ece6=ece6, ece7=ece7, ece8=ece8, it1=it1, it2=it2, it3=it3, it4=it4, it5=it5, it6=it6, it7=it7, it8=it8)

            # res.save()
        return HttpResponse("Passed")
    return HttpResponseBadRequest()

def show_data(request):
    results = list(Result.objects.all())
    teachers = []
    for i in range(len(results)):
        temp = []
        result = results[i]

        cse1 = result.cse1
        cse1_faculty = ''
        if(cse1 != '0'):
            cse1_faculty = Batch.objects.get(course_code=cse1).teacher_code.teacher_code
        temp.append(cse1_faculty)

        cse2 = result.cse2
        cse2_faculty = ''
        if(cse2 != '0'):
            cse2_faculty = Batch.objects.get(course_code=cse2).teacher_code.teacher_code
        temp.append(cse2_faculty)

        cse3 = result.cse3
        cse3_faculty = ''
        if(cse3 != '0'):
            cse3_faculty = Batch.objects.get(course_code=cse3).teacher_code.teacher_code
        temp.append(cse3_faculty)

        cse4 = result.cse4
        cse4_faculty = ''
        if(cse4 != '0'):
            cse4_faculty = Batch.objects.get(course_code=cse4).teacher_code.teacher_code
        temp.append(cse4_faculty)

        cse5 = result.cse5
        cse5_faculty = ''
        if(cse5 != '0'):
            cse5_faculty = Batch.objects.get(course_code=cse5).teacher_code.teacher_code
        temp.append(cse5_faculty)

        cse6 = result.cse6
        cse6_faculty = ''
        if(cse6 != '0'):
            cse6_faculty = Batch.objects.get(course_code=cse6).teacher_code.teacher_code
        temp.append(cse6_faculty)

        cse7 = result.cse7
        cse7_faculty = ''
        if(cse7 != '0'):
            cse7_faculty = Batch.objects.get(course_code=cse7).teacher_code.teacher_code
        temp.append(cse7_faculty)

        cse8 = result.cse8
        cse8_faculty = ''
        if(cse8 != '0'):
            cse8_faculty = Batch.objects.get(course_code=cse8).teacher_code.teacher_code
        temp.append(cse8_faculty)


        ece1 = result.ece1
        ece1_faculty = ''
        if(ece1 != '0'):
            ece1_faculty = Batch.objects.get(course_code=ece1).teacher_code.teacher_code
        temp.append(ece1_faculty)

        ece2 = result.ece2
        ece2_faculty = ''
        if(ece2 != '0'):
            ece2_faculty = Batch.objects.get(course_code=ece2).teacher_code.teacher_code
        temp.append(ece2_faculty)

        ece3 = result.ece3
        ece3_faculty = ''
        if(ece3 != '0'):
            ece3_faculty = Batch.objects.get(course_code=ece3).teacher_code.teacher_code
        temp.append(ece3_faculty)

        ece4 = result.ece4
        ece4_faculty = ''
        if(ece4 != '0'):
            ece4_faculty = Batch.objects.get(course_code=ece4).teacher_code.teacher_code
        temp.append(ece4_faculty)

        ece5 = result.ece5
        ece5_faculty = ''
        if(ece5 != '0'):
            ece5_faculty = Batch.objects.get(course_code=ece5).teacher_code.teacher_code
        temp.append(ece5_faculty)

        ece6 = result.ece6
        ece6_faculty = ''
        if(ece6 != '0'):
            ece6_faculty = Batch.objects.get(course_code=ece6).teacher_code.teacher_code
        temp.append(ece6_faculty)

        ece7 = result.ece7
        ece7_faculty = ''
        if(ece7 != '0'):
            ece7_faculty = Batch.objects.get(course_code=ece7).teacher_code.teacher_code
        temp.append(ece7_faculty)

        ece8 = result.ece8
        ece8_faculty = ''
        if(ece8 != '0'):
            ece8_faculty = Batch.objects.get(course_code=ece8).teacher_code.teacher_code
        temp.append(ece8_faculty)


        it1 = result.it1
        it1_faculty = ''
        if(it1 != '0'):
            it1_faculty = Batch.objects.get(course_code=it1).teacher_code.teacher_code
        temp.append(it1_faculty)

        it2 = result.it2
        it2_faculty = ''
        if(it2 != '0'):
            it2_faculty = Batch.objects.get(course_code=it2).teacher_code.teacher_code
        temp.append(it2_faculty)

        it3 = result.it3
        it3_faculty = ''
        if(it3 != '0'):
            it3_faculty = Batch.objects.get(course_code=it3).teacher_code.teacher_code
        temp.append(it3_faculty)

        it4 = result.it4
        it4_faculty = ''
        if(it4 != '0'):
            it4_faculty = Batch.objects.get(course_code=it4).teacher_code.teacher_code
        temp.append(it4_faculty)

        it5 = result.it5
        it5_faculty = ''
        if(it5 != '0'):
            it5_faculty = Batch.objects.get(course_code=it5).teacher_code.teacher_code
        temp.append(it5_faculty)

        it6 = result.it6
        it6_faculty = ''
        if(it6 != '0'):
            it6_faculty = Batch.objects.get(course_code=it6).teacher_code.teacher_code
        temp.append(it6_faculty)

        it7 = result.it7
        it7_faculty = ''
        if(it7 != '0'):
            it7_faculty = Batch.objects.get(course_code=it7).teacher_code.teacher_code
        temp.append(it7_faculty)

        it8 = result.it8
        it8_faculty = ''
        if(it8 != '0'):
            it8_faculty = Batch.objects.get(course_code=it8).teacher_code.teacher_code
        temp.append(it8_faculty)

        teacher = ResultTeacher(cse1_faculty=cse1_faculty, cse2_faculty=cse2_faculty,
         cse3_faculty=cse3_faculty, cse4_faculty=cse4_faculty, cse5_faculty=cse5_faculty,
          cse6_faculty=cse6_faculty, cse7_faculty=cse7_faculty,cse8_faculty=cse8_faculty,
          ece1_faculty=ece1_faculty, ece2_faculty=ece2_faculty,
           ece3_faculty=ece3_faculty, ece4_faculty=ece4_faculty, ece5_faculty=ece5_faculty,
            ece6_faculty=ece6_faculty, ece7_faculty=ece7_faculty,ece8_faculty=ece8_faculty,
            it1_faculty=it1_faculty, it2_faculty=it2_faculty,
             it3_faculty=it3_faculty, it4_faculty=it4_faculty, it5_faculty=it5_faculty,
              it6_faculty=it6_faculty, it7_faculty=it7_faculty,it8_faculty=it8_faculty)

        teachers.append(temp)

    rooms = []
    for i in range(len(results)):
        temp = []
        result = results[i]

        cse1 = result.cse1
        cse1_room = ''
        if(cse1 != '0'):
            cse1_room = Batch.objects.get(course_code=cse1).room
        temp.append(cse1_room)

        cse2 = result.cse2
        cse2_room = ''
        if(cse2 != '0'):
            cse2_room = Batch.objects.get(course_code=cse2).room
        temp.append(cse2_room)

        cse3 = result.cse3
        cse3_room = ''
        if(cse3 != '0'):
            cse3_room = Batch.objects.get(course_code=cse3).room
        temp.append(cse3_room)

        cse4 = result.cse4
        cse4_room = ''
        if(cse4 != '0'):
            cse4_room = Batch.objects.get(course_code=cse4).room
        temp.append(cse4_room)

        cse5 = result.cse5
        cse5_room = ''
        if(cse5 != '0'):
            cse5_room = Batch.objects.get(course_code=cse5).room
        temp.append(cse5_room)

        cse6 = result.cse6
        cse6_room = ''
        if(cse6 != '0'):
            cse6_room = Batch.objects.get(course_code=cse6).room
        temp.append(cse6_room)

        cse7 = result.cse7
        cse7_room = ''
        if(cse7 != '0'):
            cse7_room = Batch.objects.get(course_code=cse7).room
        temp.append(cse7_room)

        cse8 = result.cse8
        cse8_room = ''
        if(cse8 != '0'):
            cse8_room = Batch.objects.get(course_code=cse8).room
        temp.append(cse8_room)


        ece1 = result.ece1
        ece1_room = ''
        if(ece1 != '0'):
            ece1_room = Batch.objects.get(course_code=ece1).room
        temp.append(ece1_room)

        ece2 = result.ece2
        ece2_room = ''
        if(ece2 != '0'):
            ece2_room = Batch.objects.get(course_code=ece2).room
        temp.append(ece2_room)

        ece3 = result.ece3
        ece3_room = ''
        if(ece3 != '0'):
            ece3_room = Batch.objects.get(course_code=ece3).room
        temp.append(ece3_room)

        ece4 = result.ece4
        ece4_room = ''
        if(ece4 != '0'):
            ece4_room = Batch.objects.get(course_code=ece4).room
        temp.append(ece4_room)

        ece5 = result.ece5
        ece5_room = ''
        if(ece5 != '0'):
            ece5_room = Batch.objects.get(course_code=ece5).room
        temp.append(ece5_room)

        ece6 = result.ece6
        ece6_room = ''
        if(ece6 != '0'):
            ece6_room = Batch.objects.get(course_code=ece6).room
        temp.append(ece6_room)

        ece7 = result.ece7
        ece7_room = ''
        if(ece7 != '0'):
            ece7_room = Batch.objects.get(course_code=ece7).room
        temp.append(ece7_room)

        ece8 = result.ece8
        ece8_room = ''
        if(ece8 != '0'):
            ece8_room = Batch.objects.get(course_code=ece8).room
        temp.append(ece8_room)


        it1 = result.it1
        it1_room = ''
        if(it1 != '0'):
            it1_room = Batch.objects.get(course_code=it1).room
        temp.append(it1_room)

        it2 = result.it2
        it2_room = ''
        if(it2 != '0'):
            it2_room = Batch.objects.get(course_code=it2).room
        temp.append(it2_room)

        it3 = result.it3
        it3_room = ''
        if(it3 != '0'):
            it3_room = Batch.objects.get(course_code=it3).room
        temp.append(it3_room)

        it4 = result.it4
        it4_room = ''
        if(it4 != '0'):
            it4_room = Batch.objects.get(course_code=it4).room
        temp.append(it4_room)

        it5 = result.it5
        it5_room = ''
        if(it5 != '0'):
            it5_room = Batch.objects.get(course_code=it5).room
        temp.append(it5_room)

        it6 = result.it6
        it6_room = ''
        if(it6 != '0'):
            it6_room = Batch.objects.get(course_code=it6).room
        temp.append(it6_room)

        it7 = result.it7
        it7_room = ''
        if(it7 != '0'):
            it7_room = Batch.objects.get(course_code=it7).room
        temp.append(it7_room)

        it8 = result.it8
        it8_room = ''
        if(it8 != '0'):
            it8_room = Batch.objects.get(course_code=it8).room
        temp.append(it8_room)

        rooms.append(temp)
    print(rooms)
    print(len(rooms))
    print(len(teachers))
    print(batches)
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Sat']
    return render(request, 'accounts/show_data.html', {'results':results,'days':days, 'teachers':teachers, 'batches':batches, 'rooms':rooms})

def pass_value(request):
    global batches
    batches = request.GET.getlist('batches')
    batch = Batch.objects.filter(branch_sem__in=batches)
    course=[]
    teacher = []
    for i in range(batch.count()):
        my_list = []
        temp = []
        my_list.append(batch[i].branch_sem)
        my_list.append(str(batch[i].course_code))
        temp.append(str(batch[i].course_code))
        my_list.append(str(batch[i].teacher_code))
        temp.append(str(batch[i].teacher_code))
        my_list.append(str(batch[i].room))
        my_list.append(str(batch[i].no_class_week))
        my_list.append(str(batch[i].no_of_slots))

        course.append(my_list)
        teacher.append(temp)

    return render(request, 'accounts/new.html', {'course': course, 'teacher':teacher, 'batches':batches})

class Homepage(ListView):
    model = Batch
    template_name = 'accounts/home.html'
    context_object_name = 'batch_counts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        branches = Branch.objects.all().order_by('branch_code')
        print(branches)
        context['branches'] = branches
        course_schema = Course.objects.values_list("course_intro", flat=True).order_by("course_intro").distinct()
        context['course_schema'] = course_schema
        return context

    def get_queryset(self):
        batch_count = Batch.objects.all().values('branch_sem').annotate(total=Count('branch_sem'))
        return batch_count
class AddBatch(CreateView):
    model = Batch
    template_name = 'accounts/add_batch.html'
    fields = ('course_code','teacher_code','room','no_class_week','no_of_slots')
    no_of_courses=0
    success_url = reverse_lazy('accounts:home')
    branch_sem = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        branch = self.request.GET.get('branch')
        sem = self.request.GET.get('sem')
        self.branch_sem = branch+sem
        course_schema = self.request.GET.get('course_schema')
        courses = Course.objects.filter(sem=sem, branch_code=branch, course_intro=course_schema)
        teachers = Teacher.objects.all()
        cc = Course.objects.all()
        room = Room.objects.all()
        context['rooms'] = room
        context['cc'] = cc
        context['branch_sem'] = branch+sem
        context['teachers'] = teachers
        context['courses'] = courses
        self.no_of_courses = courses.count()
        print(self.no_of_courses)
        return context

    def post(self, request, *args, **kwargs):
        branch_sem = self.request.POST['branch_sem']
        print(branch_sem)
        no_of_course = self.request.POST['no_of_courses']
        no_of_course = int(no_of_course,10)
        print(no_of_course)

        for i in range(no_of_course):
            print(branch_sem)
            course_code = self.request.POST['course_code'+str(i+1)]
            print(course_code)
            course_code = Course.objects.get(course_code=course_code)
            print(course_code)
            teacher_code = self.request.POST['teacher_code'+str(i+1)]
            print(teacher_code)
            teacher_code = Teacher.objects.get(teacher_code=teacher_code)
            print(teacher_code)
            room = self.request.POST['room'+str(i+1)]
            print(room)
            no_class_week = self.request.POST['no_class_week'+str(i+1)]
            print(no_class_week)
            no_of_slots = self.request.POST['no_of_slots'+str(i+1)]
            print(no_of_slots)
            batch = Batch(branch_sem=branch_sem, course_code=course_code,
                            teacher_code=teacher_code, room=room, no_class_week=no_class_week,
                            no_of_slots=no_of_slots)
            print(batch)
            batch.save()
        return redirect('accounts:home')



class CustomLoginView(LoginView,RedirectView):
    """
    It determines the authenticatation process from log in, and redirects the user.
    This view is linked with phdadmission/templates/home.html
    """
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get_redirect_url(self):
        """
        It redirects to respective homepage of user
        """
        return reverse('accounts:home')

def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user_email = request.POST['email']
            print(user_email)
            user = form.save(commit=False)
            user.is_active = False
            user.username = user_email
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('accounts/acc_active_email.html', {
                'user':user, 'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your IIIT Portal account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration. To login go back to  Homepage')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def activate(request, uidb64, token):
    """
    It makes the unique url that is to be sent in email to user for activation
    """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
