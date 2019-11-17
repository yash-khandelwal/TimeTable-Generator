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
from accounts.models import User,Batch
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
UserModel = get_user_model()
# Create your views here.

class Homepage(ListView):
    template_name = 'accounts/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        branches = Branch.objects.all().order_by('branch_code')
        print(branches)
        context['branches'] = branches
        return context

    def get_queryset(self):
        branch = self.request.GET.get('branch')
    #     sem = self.request.GET.get('sem')

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
        return render(request, 'accounts/home.html')



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
