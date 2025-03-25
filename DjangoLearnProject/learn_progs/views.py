from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic,Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    '''Домашняя страница приложения DjangoLearnProject'''
    return render(request,'learn_progs/index.html')

def topics(request):
    '''Выводит список тем'''
    topics=Topic.objects.all().order_by('date_added')
    context={'topics':topics}
    return render(request,'learn_progs/topics.html', context)

def topic(request,topic_id):
    '''Выводит одну тему и все её записи.'''
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('-date_added')
    context={'topic':topic,'entries':entries,'conditions':[entry for entry in entries if request.user==entry.owner]}
    return render(request,'learn_progs/topic.html',context)

@login_required
def new_topic(request):
    '''Определяет новую тему'''
    if request.method!='POST':
        #Данные не отправлялись; создаётся пустая форма.
        form=TopicForm()
    else:
        #Отправлены данные POST; обработать данные.
        form=TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    context={'form':form}
    return render(request,'learn_progs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    '''Добавляет новую запись по конкретной теме.'''
    topic=Topic.objects.get(id=topic_id)
    if request.method!='POST':
    #Данные не отправлялись; создаётся пустая форма.
        form=EntryForm()
    else:
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.owner=request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('topic',args=[topic_id]))
    context={'topic':topic,'form':form}
    return render(request,'learn_progs/new_entry.html',context)

@login_required
def edit_entry(request,topic_id):
    '''Редактирует существующую запись.'''
    entry=Entry.objects.get(id=topic_id)
    topic=entry.topic
    if request.method!='POST':
        #Исходный запрос; форма заполняется данными текущей записи
        form=EntryForm(instance=entry)
    else:
        #Отправка данных POST; обработать данные
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic',args=[topic_id]))
    context={'entry':entry,'topic':topic,'form':form}
    return render(request,'learn_progs/edit_entry.html',context)
            
    
