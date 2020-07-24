from django.shortcuts import render
from main_application import stats_picture_names
# Create your views here.
def home_page(request):
    return render(request, 'index.html')

def load_south_african_stats(request):
    states_pictures = stats_picture_names.SA_PICTURES_AND_STATS_VALUES()

    return render(request, 'view_SA_stats.html', states_pictures)
