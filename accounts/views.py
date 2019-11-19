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
from accounts.models import User,Batch, Result
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
UserModel = get_user_model()
# Create your views here.



def fetch_data(request):
    if request.is_ajax():
        data = request.POST.get("param")
        print(data)
        print(type(data))
        data_js = json.loads(data)
        keys = list(data_js.keys())
        print(keys)
        print('lalala')
        x = json.loads(data_js["CSE3"])
        print(x)
        # print(data_js['CSE3'][0])
        size = len(x)
        print(size)


        for i in range(size+5):
            if(i%5==0 and i%2!=0):
                res = Result()
            else:
                cse1 = ''
                if('CSE1' in keys):
                    cse1 = json.loads(data_js['CSE1'])[i]
                cse2 = ''
                if('CSE2' in keys):
                    cse2 = json.loads(data_js['CSE2'])[i]
                cse3 = ''
                if('CSE3' in keys):
                    cse3 = json.loads(data_js['CSE3'])[i]
                cse4 = ''
                if('CSE4' in keys):
                    cse4 = json.loads(data_js['CSE4'])[i]
                cse5 = ''
                if('CSE5' in keys):
                    cse5 = json.loads(data_js['CSE5'])[i]
                cse6 = ''
                if('CSE6' in keys):
                    cse6 = json.loads(data_js['CSE6'])[i]
                cse7 = ''
                if('CSE7' in keys):
                    cse7 = json.loads(data_js['CSE7'])[i]
                cse8 = ''
                if('CSE8' in keys):
                    cse8 = json.loads(data_js['CSE8'])[i]

                ece1 = ''
                if('ECE1' in keys):
                    ece1 = json.loads(data_js['ECE1'])[i]
                ece2 = ''
                if('ECE2' in keys):
                    ece2 = json.loads(data_js['ECE2'])[i]
                ece3 = ''
                if('ECE3' in keys):
                    ece3 = json.loads(data_js['ECE3'])[i]
                ece4 = ''
                if('ECE4' in keys):
                    ece4 = json.loads(data_js['ECE4'])[i]

                ece5 = ''
                if('ECE5' in keys):
                    ece5 = json.loads(data_js['ECE5'])[i]
                ece6 = ''
                if('ECE6' in keys):
                    ece6 = json.loads(data_js['ECE6'])[i]
                ece7 = ''
                if('ECE7' in keys):
                    ece7 = json.loads(data_js['ECE7'])[i]
                ece8 = ''
                if('ECE8' in keys):
                    ece8 = json.loads(data_js['ECE8'])[i]

                it1 = ''
                if('IT1' in keys):
                    it1 = json.loads(data_js['IT1'])[i]
                it2 = ''
                if('IT2' in keys):
                    it2 = json.loads(data_js['IT2'])[i]
                it3 = ''
                if('IT3' in keys):
                    it3 = json.loads(data_js['IT3'])[i]
                it4 = ''
                if('IT4' in keys):
                    it4 = json.loads(data_js['IT4'])[i]
                it5 = ''
                if('IT5' in keys):
                    it5 = json.loads(data_js['IT5'])[i]
                it6 = ''
                if('IT6' in keys):
                    it6 = json.loads(data_js['IT6'])[i]
                it7 = ''
                if('IT7' in keys):
                    it7 = json.loads(data_js['IT7'])[i]
                it8 = ''
                if('IT8' in keys):
                    it8 = json.loads(data_js['IT8'])[i]

            res = Result(cse1=cse1, cse2=cse2, cse3=cse3, cse4=cse4, cse5=cse5, cse6=cse6, cse7=cse7, cse8=cse8, ece1=ece1, ece2=ece2, ece3=ece3, ece4=ece4, ece5=ece5, ece6=ece6, ece7=ece7, ece8=ece8, it1=it1, it2=it2, it3=it3, it4=it4, it5=it5, it6=it6, it7=it7, it8=it8)
            res.save()
        return HttpResponse("Passed")
    return HttpResponseBadRequest()

def show_data(request):
    results = list(Result.objects.all())
    return render(request, 'accounts/show_data.html', {'results':results})


def pass_value(request):
    batch = Batch.objects.filter(branch_sem__in=['CSE3','CSE5','ECE3','ECE5','IT3','IT5'])
    course=[]
    teacher = []
    if(request.is_ajax()):
        course = request.POST.get('courses',None)
        print(course)
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

        # my_list= [ , str(batch[i].course_code), str(batch[i].teacher_code), batch[i].room, str(batch[i].no_class_week), str(batch[i].no_of_slots ]
        course.append(my_list)
        teacher.append(temp)

    return render(request, 'accounts/new.html', {'course': course, 'teacher':teacher})

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
    success_url = reverse_lazy('index')
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
        return redirect('index')



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
        return reverse('index')

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
