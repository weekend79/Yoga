from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from courses.models import Course


# Create your views here.
def view_bag(request):
    """ A view that renders the shopping bag """

    return render(request, "bag.html")


def add_to_bag(request, item_id):
    """ A view that adds courses to the bag"""

    course = get_object_or_404(Course, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'{course.name} er oppdatert i din kurv')
    else:
        bag[item_id] = quantity
        messages.success(request, f'{course.name} er lagt til i din kurv')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specific course"""

    course = get_object_or_404(Course, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'{course.name} har blitt oppdatert')
    else:
        bag.pop(item_id)
        messages.success(request, f'{course.name} har blitt fjernet')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove an Item from the bag"""

    try:
        course = get_object_or_404(Course, pk=item_id)
        bag = request.session.get('bag', {})

        del bag[item_id]
        if not bag[item_id]:
            bag.pop(item_id)
        else:
            bag.pop(item_id)
            messages.success(request, f'{course.name} har blitt fjernet fra din kurv')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error i forsøket på å fjerne produktet')
        return HttpResponse(status=500)
