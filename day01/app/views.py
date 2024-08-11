from django.shortcuts import render
from .models import *
from .forms import TestForm, CategoryForm, UnitForm, ItemForm, SupplierForm, OrderForm, EmployeeForm
from django.core.paginator import Paginator
from .filters import *

# Create your views here.
def unit_view(request):
    units = Unit.objects.all()
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UnitForm()
    context_uts = {'form':form, 'uts':units}
    return render(request , 'Unit.html', context_uts)

def test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
    else:
        form = TestForm()
    context_test = {'form':form}
    return render(request, 'test.html', context_test)

def category_view(request):
    page_number = request.GET.get('page')
    filter = CategoryFilter(request.GET, queryset=Category.objects.all())
    categories = filter.qs
    paginator = Paginator(categories, 3)
    page = paginator.get_page(page_number)

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoryForm()
    context = {'form':form, 'page':page}
    return render(request , 'Category.html', context)

def item_view(request):
    page_number = request.GET.get('page')
    filter = ItemFilter(request.GET, queryset=Item.objects.all())
    items = filter.qs
    paginator = Paginator(items, 3)
    page = paginator.get_page(page_number)

    if request.method == 'POST':
        form = ItemForm(request.POST)
    else:
        form = ItemForm()
    context_itms = {'form':form, 'page':page}
    return render(request , 'Item.html', context_itms)

def supplier_view(request):
    suppliers = Supplier.objects.all()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SupplierForm()
    context_supplrs = {'form':form, 'supplrs':suppliers}
    return render(request , 'supplier.html', context_supplrs)

def order_view(request):
    orders = Order.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm()
    context_ordrs = {'form':form, 'ordrs':orders}
    return render(request , 'order.html', context_ordrs)

def employee_view(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()
    context_employs = {'form':form, 'employs':employees}
    return render(request , 'employee.html', context_employs)