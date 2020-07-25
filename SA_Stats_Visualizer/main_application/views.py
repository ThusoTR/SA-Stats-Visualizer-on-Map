from django.shortcuts import render
from main_application import stats_picture_names
# Create your views here.
def home_page(request):
    names_of_provinces = stats_picture_names.province_names()
    return render(request, 'index.html', names_of_provinces)

def load_south_african_stats(request, province_name):
    stats_pictures = stats_picture_names.SA_PICTURES_AND_STATS_VALUES()
    names_of_provinces = stats_picture_names.province_names()
    return render(request, 'view_SA_stats.html', [stats_pictures, names_of_provinces])
def loaf_provincial_stats(request, **kwargs):
    province_stats_values_dict = {
        'province_name': 'province_name'
    }
    stats_pictures = stats_picture_names.SA_PICTURES_AND_STATS_VALUES()
    provincial_stats_pictures = stats_picture_names.SA_PICTURES_AND_STATS_VALUES()
    return render(request, 'view_provincial_stats.html', [province_stats_values_dict, stats_pictures,
                                                          provincial_stats_pictures])
