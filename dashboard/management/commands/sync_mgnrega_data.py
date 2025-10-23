import requests
import pandas as pd
from django.core.management.base import BaseCommand
from dashboard.models import MgnregaRecord

class Command(BaseCommand):
    help = "Sync MGNREGA data from data.gov.in API and local CSV file"

    def handle(self, *args, **kwargs):
        self.sync_from_api()
        self.sync_from_csv()

    def sync_from_api(self):
        url = "https://api.data.gov.in/resource/ee03643a-ee4c-48c2-ac30-9f2ff26ab722"
        params = {
            "api-key": "579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b",
            "format": "json",
            "filters[state_name]": "KERALA",
            "limit": 1000
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json().get("records", [])
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"API fetch failed: {e}"))
            return

        count = 0
        for item in data:
            MgnregaRecord.objects.update_or_create(
                district_code=item.get("district_code", None),
                month=item.get("month", None),
                fin_year=item.get("fin_year", None),
                defaults={
                    "state_code": item.get("state_code", None),
                    "state_name": item.get("state_name", None),
                    "district_name": item.get("district_name", None),
                    "approved_labour_budget": item.get("approved_labour_budget", None),
                    "average_wage_rate": item.get("average_wage_rate", None),
                    "average_days_employment": item.get("average_days_employment", None),
                    "differently_abled_persons_worked": item.get("differently_abled_persons_worked", None),
                    "material_and_skilled_wages": item.get("material_and_skilled_wages", None),
                    "completed_works": item.get("number_of_completed_works", None),
                    "gps_with_nil_exp": item.get("gps_with_nil_exp", None),
                    "ongoing_works": item.get("number_of_ongoing_works", None),
                    "central_liability_persondays": item.get("central_liability_persondays", None),
                    "sc_persondays": item.get("sc_persondays", None),
                    "sc_workers_percent": item.get("sc_workers_percent", None),
                    "st_persondays": item.get("st_persondays", None),
                    "st_workers_percent": item.get("st_workers_percent", None),
                    "total_admin_expenditure": item.get("total_admin_expenditure", None),
                    "total_expenditure": item.get("total_exp", None),
                    "total_households_worked": item.get("total_households_worked", None),
                    "total_individuals_worked": item.get("total_individuals_worked", None),
                    "active_jobcards": item.get("active_jobcards", None),
                    "active_workers": item.get("active_workers", None),
                    "households_100_days": item.get("households_100_days", None),
                    "jobcards_issued": item.get("jobcards_issued", None),
                    "total_workers": item.get("total_workers", None),
                    "total_works_takenup": item.get("total_works_takenup", None),
                    "wages": item.get("wages", None),
                    "women_persondays": item.get("women_persondays", None),
                    "percent_category_b_works": item.get("percent_category_b_works", None),
                    "percent_agriculture_expenditure": item.get("percent_agriculture_expenditure", None),
                    "percent_nrm_expenditure": item.get("percent_nrm_expenditure", None),
                    "percent_payments_within_15_days": item.get("percent_payments_within_15_days", None),
                    "remarks": item.get("remarks", "")
                }
            )
            count += 1
        self.stdout.write(self.style.SUCCESS(f"✅ Synced {count} records from API"))

    def sync_from_csv(self):
        try:
            df = pd.read_csv("dashboard/data/mgnrega_kerala.csv")
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"CSV read failed: {e}"))
            return

        count = 0
        for _, row in df.iterrows():
            MgnregaRecord.objects.update_or_create(
                district_code=str(row.get("district_code", "")).strip(),
                month=str(row.get("month", "")).strip(),
                fin_year=str(row.get("fin_year", "")).strip(),
                defaults={
                    "state_code": row.get("state_code", ""),
                    "state_name": row.get("state_name", ""),
                    "district_name": row.get("district_name", ""),
                    "approved_labour_budget": row.get("Approved_Labour_Budget", None),
                    "average_wage_rate": row.get("Average_Wage_rate_per_day_per_person", None),
                    "average_days_employment": row.get("Average_days_of_employment_provided_per_Household", None),
                    "differently_abled_persons_worked": row.get("Differently_abled_persons_worked", None),
                    "material_and_skilled_wages": row.get("Material_and_skilled_Wages", None),
                    "completed_works": row.get("Number_of_Completed_Works", None),
                    "gps_with_nil_exp": row.get("Number_of_GPs_with_NIL_exp", None),
                    "ongoing_works": row.get("Number_of_Ongoing_Works", None),
                    "central_liability_persondays": row.get("Persondays_of_Central_Liability_so_far", None),
                    "sc_persondays": row.get("SC_persondays", None),
                    "sc_workers_percent": row.get("SC_workers_against_active_workers", None),
                    "st_persondays": row.get("ST_persondays", None),
                    "st_workers_percent": row.get("ST_workers_against_active_workers", None),
                    "total_admin_expenditure": row.get("Total_Adm_Expenditure", None),
                    "total_expenditure": row.get("Total_Exp", None),
                    "total_households_worked": row.get("Total_Households_Worked", None),
                    "total_individuals_worked": row.get("Total_Individuals_Worked", None),
                    "active_jobcards": row.get("Total_No_of_Active_Job_Cards", None),
                    "active_workers": row.get("Total_No_of_Active_Workers", None),
                    "households_100_days": row.get("Total_No_of_HHs_completed_100_Days_of_Wage_Employment", None),
                    "jobcards_issued": row.get("Total_No_of_JobCards_issued", None),
                    "total_workers": row.get("Total_No_of_Workers", None),
                    "total_works_takenup": row.get("Total_No_of_Works_Takenup", None),
                    "wages": row.get("Wages", None),
                    "women_persondays": row.get("Women_Persondays", None),
                    "percent_category_b_works": row.get("percent_of_Category_B_Works", None),
                    "percent_agriculture_expenditure": row.get("percent_of_Expenditure_on_Agriculture_Allied_Works", None),
                    "percent_nrm_expenditure": row.get("percent_of_NRM_Expenditure", None),
                    "percent_payments_within_15_days": row.get("percentage_payments_gererated_within_15_days", None),
                    "remarks": row.get("Remarks", "")
                }
            )
            count += 1
        self.stdout.write(self.style.SUCCESS(f"✅ Synced {count} records from CSV"))