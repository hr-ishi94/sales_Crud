from django.shortcuts import render, get_object_or_404, redirect
from .models import Sales
from django.contrib import messages
from django.db.models import Q
from django.utils.dateparse import parse_date

def index(request):
    sales = Sales.objects.filter(is_active=True)
    search_query = request.POST.get("query", "")

    if request.method == "POST":
        # Add New Sale Record
        if "create" in request.POST:
            product_id = request.POST.get('product_id')
            category = request.POST.get('category')
            date = parse_date(request.POST.get('date'))
            price = request.POST.get('price')
            discount = request.POST.get('discount', 0.00)
            units_sold = request.POST.get('units_sold', 0)

            # Check if product_ID already exists
            if Sales.objects.filter(product_ID=product_id, is_active=True).exists():
                messages.error(request, "A sale with this Product ID already exists.")
            else:
                Sales.objects.create(
                    product_ID=product_id,
                    category=category,
                    date=date,
                    price=price,
                    discount=discount,
                    units_sold=units_sold
                )
                messages.success(request, "Data added successfully.")
            return redirect('index')

        # Update Sale Record
        elif "update" in request.POST:
            sale_id = request.POST.get("sale_id")
            sale = get_object_or_404(Sales, id=sale_id)

            product_id = request.POST.get("product_id")

            # Check if product_ID already exists for another sale
            if Sales.objects.filter(product_ID=product_id, is_active=True).exclude(id=sale_id).exists():
                messages.error(request, "A sale with this Product ID already exists.")
            else:
                sale.product_ID = product_id
                sale.category = request.POST.get("category")
                sale.date = parse_date(request.POST.get("date"))
                sale.price = request.POST.get("price")
                sale.discount = request.POST.get("discount")
                sale.units_sold = request.POST.get("units_sold")
                sale.save()
                messages.success(request, "Data updated successfully.")
            return redirect('index')

        # Delete Sale Record
        elif "delete" in request.POST:
            sale_id = request.POST.get("sale_id")
            sale = get_object_or_404(Sales, id=sale_id)
            sale.is_active = False
            sale.save()
            messages.success(request, "Data deleted successfully.")
            return redirect('index')

        # Search Sale Records
        elif "search" in request.POST:
            search_query = request.POST.get("query")
            sales = Sales.objects.filter(
                Q(product_ID__icontains=search_query) |
                Q(category__icontains=search_query),
                is_active=True
            )

    context = {
        "sales": sales,
        "search_query": search_query
    }
    return render(request, "index.html", context)
