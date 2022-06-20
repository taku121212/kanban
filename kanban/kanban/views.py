from django.shortcuts import render

#kanaban.index仮のトップ
def index(request):
    return render(request, "kanban/index.html") # このように変更する


 