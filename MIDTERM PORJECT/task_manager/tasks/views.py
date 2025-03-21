from django.shortcuts import render, redirect
from .models import Field

# Create your views here.

def index(request):
            fields = Field.objects.all()
            return render(request, 'index.html', {'fields': fields})

 
def add_field(request):
            if request.method == 'POST':
                title = request.POST.get('title')
                description = request.POST.get('description')
                due_date = request.POST.get('due_date')
                status = request.POST.get('status')
                field = Field(title=title, description=description, due_date=due_date, status=status)
                field.save()
            return redirect('/tasks/')


def update_field(request, id):
            field = Field.objects.get(id=id)
            if request.method == 'POST':
                field.title = request.POST.get('title')
                field.description = request.POST.get('description')
                field.due_date = request.POST.get('due_date')
                field.status = request.POST.get('status')
                field.save()
                return redirect('/tasks/')
            return render(request, 'update.html', {'field': field})

    
def deleteField(request, id):
            field = Field.objects.get(id=id)
            field.delete()
            return redirect('/tasks/')

