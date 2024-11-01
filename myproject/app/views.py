
from django.shortcuts import render
from .models import Sales
from django.contrib import messages
from django.db.models import Q


def index(request):
    sale = Sales.objects.filter(is_active=True)
    search_query = ""
    if request.method == "POST": 
        if "create" in request.POST:
            product_id = request.POST['product_id']
            category = request.POST['category']
            date = request.POST['date']
            price = request.POST['price']
            discount = request.POST['discount']
            units_sold = request.POST['units_sold']
            
            Sales.objects.create(
                product_ID=product_id,
                category=category,
                date=date,
                price=price,
                discount=discount,
                units_sold=units_sold
            )
            messages.success(request, "data added successfully")
    
        elif "update" in request.POST:
            product_id = request.POST.get("product_id")
            category = request.POST.get("category")
            date = request.POST.get("date")
            price = request.POST.get("price")
            discount = request.POST.get("discount")
            units_sold = request.POST.get("units_sold")
            sale = Sales.objects.get(product_ID=product_id)
            sale.product_ID = product_id
            sale.category = category
            sale.date=  date
            sale.price = price
            sale.discount= discount
            sale.units_sold = units_sold
            sale.save()
            messages.success(request, "data updated successfully")
    
        elif "delete" in request.POST:
            p_id = request.POST.get("id")
            #Sales.objects.get(id=p_id).delete()
            sale= Sales.objects.get(id=p_id)
            #sale.is_active=False
            print(sale.product_ID)
            messages.success(request, "data deleted successfully")
        
        elif "search" in request.POST:
            search_query = request.POST.get("query")
            sale = Sales.objects.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))

    context = {"sales": sale, "search_query": search_query}
    return render(request, "index.html", context=context)