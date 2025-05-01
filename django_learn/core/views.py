from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Item
# from django.views.generic.edit import CreateView
# from django.views.generic.edit import UpdateView
# from django.views.generic.edit import DeleteView

from django.core.mail import send_mail
from django.conf import settings

#### import paginator #######
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

### Basic Email sending Example ###
def send_test_email(request):
    send_mail(
        'Test Subject',
        'Here is the message body.',
        settings.EMAIL_HOST_USER,
        ['recipient@example.com'],
        fail_silently=False,
    )
    return render(request, 'email_sent.html')

##### Class-Based Views (CBVs)
# replaced FBVs with CBVs to handle CRUD operations cleanly.

# Use ListView to Show a Single Item
class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'


# Use DetailView to Show a Single Item
class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'
    context_object_name = 'item'


############# CREATE ITEMS  ##################

# class ItemCreateView(CreateView):
#     model = Item
#     fields = ['name', 'description', 'price'
#     template_name = 'item_from.html'
#     success_url = reverse_lazy('item-list')


############### UPDATE ITEM #######################

# class ItemUpdateView(UpdateView):
#     model = Item
#     fields = ['name', 'description', 'price'
#     template_name = 'item_from.html'
#     success_url = reverse_lazy('item-list')


###################33 DELETE ITEM ###################
# class ItemDeleteView(DeleteView):
#     model = Item
#     template_name = 'item_confirm_delete.html'
#     success_url = reverse_lazy('item-list')

## Paginate OuerySet
# def product_list(request):
#     product_list = Product.objects.all()
#     paginator = Paginator(product_list, 5) #Show 5 products per page

#     page_number = request.GET.get('page') #get ?page=2 from the URL
#     page_obj = paginator.get_page(page_number)

#     return render(request, 'product_list.html', {'page_obj':page_obj})