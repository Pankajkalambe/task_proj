from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import StudentForm
from .models import Student
import logging


logger = logging.getLogger('loggers')

class Student_view(View):
    template_name = 'crud_app/student.html'

    def get(self, request):
        form = StudentForm()
        context = {'form':form}
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("New student Added")

        else:
            return redirect('show_urls')
        context = {'form':form}
        return render(request, self.template_name,context)
    
class student_list_view(View):
    template_name = 'crud_app/show.html'

    def get(self, request):
        object = Student.objects.all()
        logger.debug("All Student list are display")
        context = {'object': object}
        return render(request,self.template_name, context)
    
class Student_update_view(View):
    template_name = 'crud_app/student.html'

    def get(self, request, pk):
        obj = Student.objects.get(s_id=pk)
        form = StudentForm(instance=obj)
        context = {'form':form}
        return render(request,self.template_name,context)


    def post(self, request, pk):
        obj = Student.objects.get(s_id=pk)
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_urls')
        context = {'obj':obj}
        return render(request,self.template_name,context)

class student_delete(View):
    template_name = 'crud_app/confirmation.html'

    def get(self, request, pk):
        obj = Student.objects.get(s_id=pk)
        context = {"obj":obj}
        return render(request,self.template_name,context)
    
    def post(self, request, pk):
        obje = Student.objects.get(s_id=pk)
        obje.delete()
        return redirect('show_urls')
  