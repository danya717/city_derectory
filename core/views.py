from django.shortcuts import render

# Create your views here.
def main(request):
    path = request.path
    path = path.replace('/', '')
    print(path)
    if path == '':
        path = 'main'
    cities = ['Москва', 'Алматы', 'Астана', 'Порвоо', 'Рим', 'Таллин']
    context = {'cities' : cities}
    return render(request, f"{path}.html", context=context)