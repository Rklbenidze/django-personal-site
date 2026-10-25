from django.shortcuts import render

def info(request):
    context ={
        'name': 'Erekle',
        'surname': 'Benidze',
        'age': 16,
        "height": 185,
    }

    return render(request, 'info.html', context)

def hobbies(request):
    context = {
        'hobbies': ['zangebis devna', 'shaurmis wama', 'dzili'],
        'grade': 11,
    }

    return render(request, 'hobbies.html', context)