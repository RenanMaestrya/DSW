from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import DisksForm
from .models import Disk


# Create your views here.
def index(request):
    context = Disk.objects.all()
    return render(request, 'index.html', {'disks': context})


def disk(request, pk):
    context = Disk.objects.get(pk=pk)
    return render(request, 'disk.html', {'disk': context})

class registerDisk(CreateView):
    model = Disk
    form_class = DisksForm
    template_name = 'registerDisk.html'
    success_url = '/'

class EditDisk(UpdateView):
    model = Disk
    form_class = DisksForm
    template_name = 'registerDisk.html'
    success_url = '/'

class DeleteDisk(DeleteView):
    model = Disk
    template_name = "delete_disk.html" 
    success_url = reverse_lazy('index')
    
    def get_object(self, queryset=None):
        return Disk.objects.get(pk=self.kwargs['pk'])