from django.shortcuts import redirect, render
from .models import MgnregaRecord
from django.urls import reverse
from django.http import HttpResponse
from django.core.management import call_command

def dashboard(request):
    try:
        district = request.GET.get("district")
        category = request.GET.get("category")

        if district and category:
            url = reverse("district") + f"?district={district}&category={category}"
            return redirect(url)

        return render(request, "index.html")
    except Exception as e:
        import logging
        logging.error(f"Dashboard view error: {e}")
        raise


import logging

def district_view(request):
    try:
        district = request.GET.get("district", "").strip().upper()
        category = request.GET.get("category") or "employment"
        fin_year = request.GET.get("fin_year")

        logging.error(f"District view called with: district={district}, category={category}, fin_year={fin_year}")

        records = MgnregaRecord.objects.filter(district_name=district)
        if fin_year:
            records = records.filter(fin_year=fin_year)

        years = MgnregaRecord.objects.filter(district_name=district).values_list('fin_year', flat=True).distinct()
        all_districts = MgnregaRecord.objects.values_list('district_name', flat=True).distinct()

        return render(request, "district.html", {
            "district": district,
            "category": category,
            "records": records,
            "years": years,
            "all_districts": all_districts
        })
    except Exception as e:
        logging.error(f"District view error: {e}")
        raise



def run_migrations(request):
    call_command('migrate')
    return HttpResponse("Migrations applied.")