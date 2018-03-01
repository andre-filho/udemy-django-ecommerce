from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    # def get_context_data(self, *args, **kwargs):    # args are common args and kwargs are arg=value
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

# these lines above makes the same as these below
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
    'object_list': queryset
    }
    return render(request, 'products/list.html', context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):    # args are common args and kwargs are arg=value
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

# these lines above makes the same as these below
def product_detail_view(request, pk=None,*args, **kwargs):  # pk is a **kwarg
    # product = Product.objects.get(pk=pk) # pk is the primary key of the database (id)
    product = get_object_or_404(Product, pk=pk)
    print('incoming')
    print(product)
    context = {
    'product': product
    }
    return render(request, 'products/detail.html', context)
