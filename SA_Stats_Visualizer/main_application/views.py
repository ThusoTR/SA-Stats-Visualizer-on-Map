from django.shortcuts import render
from main_application import stats_picture_names
# Create your views here.
def home_page(request):
    names_of_provinces = stats_picture_names.province_names()
    return render(request, 'index.html', names_of_provinces)

def load_south_african_stats(request):
    stats_pictures = stats_picture_names.SA_PICTURES_AND_STATS_VALUES()
    
    return render(request, 'view_SA_stats.html', stats_pictures)
def loaf_provincial_stats(request, name):
    province_stats_values_dict = {
        'province_name': name
    }
    stats_pictures = stats_picture_names.SA_PICTURES_AND_STATS_VALUES()
    provincial_stats_pictures = stats_picture_names.PROVINCIAL_PICTURES_AND_STATS_VALUES(name)

    main_context_dict = {'province_name': name}
    #main_context_dict.update(stats_pictures)
    main_context_dict.update(provincial_stats_pictures)

    print(main_context_dict)
    return render(request, 'view_provincial_stats.html', main_context_dict)
