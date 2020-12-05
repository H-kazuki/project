from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo, Category
from . import forms
from .forms import TodoForm
import requests #html取得のライブラリ
from bs4 import BeautifulSoup #html解析ライブラリ
import datetime #現在の日時取得のライブラリ


def index(request):
	user = request.user
	todo = Todo.objects.all().filter(username = user)
	day = this_day()
	weather = today_weather()
	form = forms.TodoForm()

	context = {
		'todo' : todo,
		'day' : day,
		'weather' : weather,
		}
	return render(request, 'todo/index.html', context)


def create(request):
	if (request.method == 'POST'):
		form = TodoForm(request.POST)
		if form.is_valid():
			todo = form.save(commit = False)
			todo.username = request.user
			todo.save()

		return redirect(to = '/todo')

	context = {
		'title' : 'TODO',
		'form' : TodoForm()
	}
	return render(request, 'todo/create.html', context)


def edit(request, id):
	obj = Todo.objects.get(id = id)
	if (request.method == 'POST'):
		todo = TodoForm(request.POST, instance = obj)
		if todo.is_valid():
			todo.save()
		return redirect(to = '/todo')

	context = {
		'title' : 'TODO',
		'id' : id,
		'form' : TodoForm(instance = obj)
	}
	return render(request, 'todo/edit.html', context)


def delete(request, id):
	todo = get_object_or_404(Todo,pk=id)
	todo.delete()
	return redirect('todo:index')


def todo_category(request, category):
	category = Category.objects.get(title = category)
	todo = Todo.objects.filter(category = category).order_by('title')
	day = this_day()
	weather = today_weather()
	form = forms.TodoForm()
	if request.method == 'POST':
		form = forms.TodoForm(request.POST)
		if form.is_valid():
			form.save()

	context = {
		'todo' : todo,
		'category' : category,
		'day' : day,
		'weather' : weather,
		'form' : form
		}
	return render(request, 'todo/index.html', context)


def today_weather():
	weatherDate = [] #天気を格納する空リスト
	load_url = "https://weather.yahoo.co.jp/weather/jp/27/6200.html" #ホームページを指定
	html = requests.get(load_url) #上記のURLを取得
	soup = BeautifulSoup(html.content, "html.parser") #htmlを解析する
	for element in soup.find_all(class_ = "pict"): #今日と明日の"天気"をリスト化
		weatherDate.append(element.text)
	weather = weatherDate[0]
	return weather


def this_day():
	dayDate = [] #日付を格納する空リスト
	day = str(datetime.date.today()) #今日の年月日の文字列取得
	day_list = day.split("-") #上記の文字列をリスト化
	resultDay = day_list[0] + '年' + day_list[1] + '月' + day_list[2] + '日'
	return resultDay
