from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.
def post_job(request):
    if request.method == 'POST':
        form = jobRecordForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('login')
            return redirect('post_job')
            # return render(request, 'admin/record_book.html')
    else:
        form = jobRecordForm()

    context = {'form': form}
    return render(request, 'job/post_job.html', context)
