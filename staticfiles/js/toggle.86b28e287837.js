let currentLang = 'en';

const labels = {
  en: {
    button: 'Switch to Malayalam',
    sections: {
      employment: 'Employment & Participation',
      budget: 'Budget & Wages',
      jobcards: 'Job Cards & Workers',
      works: 'Works & Progress',
      performance: 'Performance Indicators'
    },
    fields: {
      total_households_worked: 'Total Households Worked',
      total_individuals_worked: 'Total Individuals Worked',
      average_days_employment: 'Average Days of Employment',
      women_persondays: 'Women Persondays',
      sc_persondays: 'SC Persondays',
      st_persondays: 'ST Persondays',
      sc_workers_percent: 'SC Workers %',
      st_workers_percent: 'ST Workers %',
      differently_abled_persons_worked: 'Differently Abled Worked',
      households_100_days: '100 Days Households',
      approved_labour_budget: 'Approved Labour Budget',
      average_wage_rate: 'Average Wage Rate',
      material_and_skilled_wages: 'Material & Skilled Wages',
      wages: 'Total Wages',
      total_admin_expenditure: 'Admin Expenditure',
      total_expenditure: 'Total Expenditure',
      active_jobcards: 'Active Job Cards',
      active_workers: 'Active Workers',
      jobcards_issued: 'Job Cards Issued',
      total_workers: 'Total Workers',
      completed_works: 'Completed Works',
      ongoing_works: 'Ongoing Works',
      total_works_takenup: 'Works Taken Up',
      gps_with_nil_exp: 'GPs with NIL Expenditure',
      central_liability_persondays: 'Central Liability Persondays',
      percent_category_b_works: '% Category B Works',
      percent_agriculture_expenditure: '% Agriculture Expenditure',
      percent_nrm_expenditure: '% NRM Expenditure',
      percent_payments_within_15_days: '% Payments Within 15 Days'
    }
  },
  ml: {
    button: 'Switch to English',
    sections: {
      employment: 'തൊഴിൽ & പങ്കാളിത്തം',
      budget: 'ബജറ്റ് & വേതനം',
      jobcards: 'ജോബ് കാർഡുകളും തൊഴിലാളികളും',
      works: 'ജോലികളും പുരോഗതിയും',
      performance: 'പ്രകടന സൂചികകൾ'
    },
    fields: {
      total_households_worked: 'ജോലി ചെയ്ത കുടുംബങ്ങൾ',
      total_individuals_worked: 'ജോലി ചെയ്ത വ്യക്തികൾ',
      average_days_employment: 'ഒരു കുടുംബത്തിന് ശരാശരി ജോലി ദിവസങ്ങൾ',
      women_persondays: 'സ്ത്രീകളുടെ ജോലി ദിവസങ്ങൾ',
      sc_persondays: 'എസ്.സി. ജോലി ദിവസങ്ങൾ',
      st_persondays: 'എസ്.ടി. ജോലി ദിവസങ്ങൾ',
      sc_workers_percent: 'എസ്.സി. തൊഴിലാളികൾ %',
      st_workers_percent: 'എസ്.ടി. തൊഴിലാളികൾ %',
      differently_abled_persons_worked: 'വ്യത്യസ്ത കഴിവുള്ളവർ ജോലി ചെയ്തത്',
      households_100_days: '100 ദിവസം പൂർത്തിയാക്കിയ കുടുംബങ്ങൾ',
      approved_labour_budget: 'അംഗീകരിച്ച തൊഴിൽ ബജറ്റ്',
      average_wage_rate: 'ശരാശരി ദിവസ വേതനം',
      material_and_skilled_wages: 'മെറ്റീരിയൽ & സ്കിൽ വേതനം',
      wages: 'മൊത്തം വേതനം',
      total_admin_expenditure: 'അഡ്മിനിസ്ട്രേറ്റീവ് ചെലവ്',
      total_expenditure: 'മൊത്തം ചെലവ്',
      active_jobcards: 'ആക്ടീവ് ജോബ് കാർഡുകൾ',
      active_workers: 'ആക്ടീവ് തൊഴിലാളികൾ',
      jobcards_issued: 'ഇഷ്യൂ ചെയ്ത ജോബ് കാർഡുകൾ',
      total_workers: 'മൊത്തം തൊഴിലാളികൾ',
      completed_works: 'പൂർത്തിയാക്കിയ ജോലികൾ',
      ongoing_works: 'നടക്കുന്നതായ ജോലികൾ',
      total_works_takenup: 'തുടങ്ങിയ ജോലികൾ',
      gps_with_nil_exp: 'ചെലവില്ലാത്ത ഗ്രാമപഞ്ചായത്തുകൾ',
      central_liability_persondays: 'സെൻട്രൽ ലൈബിലിറ്റിയുടെ ജോലി ദിവസങ്ങൾ',
      percent_category_b_works: 'ശ്രേണി B ജോലികളുടെ ശതമാനം',
      percent_agriculture_expenditure: 'കൃഷി & അനുബന്ധ ജോലികളിലെ ചെലവിന്റെ ശതമാനം',
      percent_nrm_expenditure: 'NRM ചെലവിന്റെ ശതമാനം',
      percent_payments_within_15_days: '15 ദിവസത്തിനുള്ളിൽ പേയ്മെന്റുകൾ'
    }
  }
};

function toggleLanguage() {
  const lang = currentLang === 'en' ? 'ml' : 'en';
  document.getElementById('langToggle').innerText = labels[lang].button;

  document.querySelectorAll('[data-label]').forEach(el => {
    const key = el.getAttribute('data-label');
    if (labels[lang].fields[key]) {
      el.innerText = labels[lang].fields[key];
    }
  });

  document.querySelectorAll('[data-section]').forEach(el => {
    const key = el.getAttribute('data-section');
    if (labels[lang].sections[key]) {
      el.innerText = labels[lang].sections[key];
    }
  });

  currentLang = lang;
}
function suggestDistrict() {
  if (!navigator.geolocation) return;

  navigator.geolocation.getCurrentPosition(pos => {
    const lat = pos.coords.latitude;
    const lon = pos.coords.longitude;

    fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`)
      .then(res => res.json())
      .then(data => {
        const districtRaw = data.address.county || data.address.state_district || data.address.state;
        if (!districtRaw) return;

        const district = districtRaw.toUpperCase();

        // List of supported districts in your database
        const validDistricts = [
          "THIRUVANANTHAPURAM", "KOLLAM", "PATHANAMTHITTA", "ALAPPUZHA", "KOTTAYAM",
          "IDUKKI", "ERNAKULAM", "THRISSUR", "PALAKKAD", "MALAPPURAM",
          "KOZHIKODE", "WAYANAD", "KANNUR", "KASARGOD"
        ];

        if (validDistricts.includes(district)) {
          const url = new URL(window.location.href);
          url.searchParams.set("district", district);
          url.searchParams.set("category", "employment");
          window.location.href = url.toString();
        } else {
          console.log("District not supported:", districtRaw);
        }
      });
  });
}