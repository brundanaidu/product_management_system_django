from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import Product, Category,Search

from .forms import ProductForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# To View all the product in the showproducts.html
#@login_required(login_url='accounts/login')
def ShowAllProducts(request):
    category = request.GET.get('Category')   # Get the clicked category name : Mobile
    if category == None: #Mobile == not available
        products = Product.objects.filter(is_published=True).order_by('price')  # DB -> Table > 3 records
    else:
        products = Product.objects.filter(category__name =category)


   # number_of_products = Product.objects.all().count()
   # print("Number of Products is:", number_of_products)
    page_num = request.GET.get('page') # creating the total page
    paginator = Paginator(products, 2) # setting total number of products in a page:3

    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    category = Category.objects.all()
    context = {
        'products': products,
        'categories': category
    }
    return render(request, 'showProducts.html',context)
# To view the single product details in the productdetails.html
#@login_required(login_url='accounts/login')
def productDetail(request,pk):
    eachproduct = Product.objects.get(id=pk)

    context = {
        'eachproduct': eachproduct
    }
    return render(request, 'productDetail.html', context)

# To Add the new product from the html template page,addproduct.html
@ login_required(login_url='showProducts')
def addProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showProducts')

    context = {
        "form": form
    }
    return render(request, 'addProduct.html', context)
# To Update Product form the html template page, updateProduct.html
@login_required(login_url='showProducts')
def updateProduct(request,pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('showProducts')
    context ={
            'form': form
        }
    return render(request, 'updateProduct.html', context)
# Delete the record from the database from the table, base on the primary key or unique
@login_required(login_url='showProducts')
def deleteProduct(request,pk):
    product = Product.objects.get(id=pk)  #storing record of 1 or 2 or 3 or 4 in product
    product.delete()  # 1=> Deleted

    return redirect('showProducts')

# creating a function for searching the data from the database using the keyword
@ login_required(login_url='showProducts')
def searchBar(request):
    if request.method == 'GET':    #get = Get => True
        query = request.GET.get('query')      # query = 999
        if query:
            multi_search = Q(Q(price__icontains = query) | Q(name__icontains = query) )
            products = Product.objects.filter(multi_search)  # 999 = 4 records found

            return render(request, 'searchbar.html',{"products":products})
        else:
            print("No Products Found to show in the Database")
            return render(request,'searchbar.html',{})

# def searchPagination(request):
#     search_items = Searchpaginator.objects.all()
#     p = Paginator(search_items, 3)
#
#     page_num= request.GET.get('page',1)
#
#     try:
#          page = p.page(page_num)
#     except EmptyPage:
#         page = p.page(1)
#     context ={'search_items':page}
#     return render(request, 'searchbar.html' , context)
def searchPagination(request):
    search_items = request.GET.get('search')   # Get the clicked category name : Mobile
    if search_items == None: #Mobile == not available
        products = Product.objects.filter(is_published=True).order_by('price')  # DB -> Table > 3 records
    else:
        products = Product.objects.filter(searchpage__name =search_items)


   # number_of_products = Product.objects.all().count()
   # print("Number of Products is:", number_of_products)
    page_num1 = request.GET.get('page1') # creating the total page
    paginator = Paginator(products, 2) # setting total number of products in a page:3

    try:
        products = paginator.page1(page_num1)
    except PageNotAnInteger:
        products = paginator.page1(2)
    except EmptyPage:
        products = paginator.page1(paginator.num_pages)
    search_items = Search.objects.all()
    context = {
        'products': products,
        'search_items': search_items
    }
    return render(request, 'searchbar.html',context)






