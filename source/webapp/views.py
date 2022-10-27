from django.shortcuts import render

# Create your views here.


def calculation_view(request):
    if request.method == 'GET':
        return render(request, 'calculation_create_view.html')
    elif request.method == 'POST':
        first = request.POST.get('first')
        second = request.POST.get('second')
        calc = request.POST.get('calculation')
        first = int(first)
        second = int(second)
        if calc == 'add':
            answer = first + second
            context = {'answer': answer}
            return render(request, 'calculation_made_view.html', {'context': context})
        elif calc == 'subtract':
            answer = first - second
            context = {'answer': answer}
            return render(request, 'calculation_made_view.html', {'context': context})
        elif calc == 'multiply':
            answer = first * second
            context = {'answer': answer}
            return render(request, 'calculation_made_view.html', {'context': context})
        elif calc == 'divide':
            try:
                answer = first / second
                context = {'answer': answer}
                return render(request, 'calculation_made_view.html', {'context': context})
            except ZeroDivisionError:
                answer = 'Cannot divide by zero'
                context = {'answer': answer}
                return render(request, 'calculation_made_view.html', {'context': context})

