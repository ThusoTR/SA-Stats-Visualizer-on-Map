$('.province').hide();
$('#province__').hide();
var mapboxAccessToken = "pk.eyJ1IjoidGh1c29wZXJzb25hbCIsImEiOiJja2NibnRwdm8yNGJmMnFxc2xvdGwwZmV1In0.VDRARBxZIo4AEaTn0n9JRA";
var map = L.map('mapid').setView([-29.087217, 24.1596], 4);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=' + mapboxAccessToken, {
    id: 'mapbox/light-v9',
    tileSize: 512,
    zoomOffset: -1,
    maxZoom: 30,
    minZoom: 5
}).addTo(map);

L.geoJson(geoJson_data).addTo(map);

function set_layer_background(e)
{
  return {
      fillColor: "#c1c5e3",
      weight: 2,
      opacity: 1,
      color: 'white',
      dashArray: '3',
      fillOpacity: 0.7
  };
}

var high_lighted_porvince = {'Limpopo': false, 'Gauteng': false, 'Mpumalanga': false,
                  'Free State': false, 'Western Cape': false, 'Northern Cape': false,
                  'North West': false, 'Eastern Cape': false, 'KwaZulu-Natal': false,};

var stats = {'Limpopo': {'province': "Limpopo", 'popuplation': '5.8 million', 'size': '125, 755', 'per_of_SA_land': '10.2 %',
                         'population_density': '46', 'GDP': '7 %', 'id': '1', 'unemployment': '44.4 %'},

             'Gauteng': {'province': "Gauteng", 'popuplation': '15.5 million', 'size': '18, 178', 'per_of_SA_land': '1.5 %',
                        'population_density': '853', 'GDP': '34 %', 'id': '2', 'unemployment': '36.3 %'},

             'Mpumalanga': {'province': "Mpumalanga", 'popuplation': '4.7 million', 'size': '76, 495', 'per_of_SA_land': '6.3 %',
                       'population_density': '61', 'GDP': '8 %', 'id': '3', 'unemployment': '43.9 %' },

             'Free State': {'province': "Free State", 'popuplation': '2.9 million', 'size': '129, 755', 'per_of_SA_land': '10.6 %',
                        'population_density': '22', 'GDP': '5 %', 'id': '5', 'unemployment': '45 %'},

             'Western Cape': {'province': "Western Cape", 'popuplation': '7 million', 'size': '129, 462', 'per_of_SA_land': '10.6 %',
                        'population_density': '54', 'GDP': '14 %', 'id': '4', 'unemployment': '24.8 %'},

             'Northern Cape': {'province': "Northern Cape", 'popuplation': '1.3 million', 'size': '372, 889', 'per_of_SA_land': '30.5 %',
                        'population_density': '3.5', 'GDP': '2 %', 'id': '6', 'unemployment': '40.1 %'},

             'North West': {'province': "North West", 'popuplation': '4.1 million', 'size': '104, 882', 'per_of_SA_land': '8.6 %',
                        'population_density': '39', 'GDP': '6 %', 'id': '7', 'unemployment': '45.1 %'},

             'Eastern Cape': {'province': "Eastern Cape", 'popuplation': '6.7 million', 'size': '168, 966', 'per_of_SA_land': '13.8 %',
                        'population_density': '40', 'GDP': '8 %', 'id': '8', 'unemployment': '49 %'},

             'KwaZulu-Natal': {'province': "KwaZulu-Natal", 'popuplation': '11.5 million', 'size': '94, 361', 'per_of_SA_land': '7.7 %',
                        'population_density': '122', 'GDP': '16 %', 'id': '9', 'unemployment': '43 %'},};

function set_display_stats(province_name)
{
  $('#province__').show();
  $('#province').show();
  document.getElementById("province").innerHTML = "<strong>Province: </strong>" + stats[province_name]['province'];
  document.getElementById("size").innerHTML = "<strong>Size: </strong>" + stats[province_name]['size'] + " km<sup>2</sup> (" +  stats[province_name]['per_of_SA_land'] +" of total S.A. land mass)";
  document.getElementById("population").innerHTML = "<strong>Popuplation: </strong>" + stats[province_name]['popuplation'];
  document.getElementById("population_density").innerHTML = "<strong>Population Density: </strong>" + stats[province_name]['population_density'] + " per km<sup>2</sup>";
  document.getElementById("GDP").innerHTML = "<strong>% Contribution to National GDP: </strong>" + stats[province_name]['GDP'];
  document.getElementById("unemployment").innerHTML = "<strong>Expaned Unemployment Rate: </strong>" + stats[province_name]['unemployment'];

  $('.province').hide();
  province_id = "#" + stats[province_name]['id'];
  $(province_id).show();
  $('.country').hide();
}

function reset_stats_panel()
{
  $('#province__').hide();
  $('#province').hide()
  document.getElementById("size").innerHTML = "<strong>Size: </strong>" + "1, 220, 813 km<sup>2</sup></p>";
  document.getElementById("population").innerHTML = "<strong>Popuplation: </strong>" + "59 million";
  document.getElementById("population_density").innerHTML = "<strong>Population Density: </strong>" + "48 per km<sup>2</sup></p>";
  document.getElementById("GDP").innerHTML = "<strong>National GDP: </strong>" + "R 4.65 trillion";
  document.getElementById("unemployment").innerHTML = "<strong>Expaned Unemployment Rate: </strong>" + '40 %';

  $('.province').hide();
  $('.country').show();

}
var previous_layer, previous_layer_set = false;  //stores layer that was hightlighted

function resetHighlight(e) {
    geojson.resetStyle(e.target);
}

function highlightFeature(e) {
    var layer = e.target;


    if (high_lighted_porvince[layer.feature.properties.name])
    {
      resetHighlight(e)
      high_lighted_porvince[layer.feature.properties.name] = false;
      reset_stats_panel();
    }
    else{

      //if a layer was highlighted, remove the highlighting form the layer
      if(previous_layer_set)
        {
          resetHighlight(previous_layer)
          high_lighted_porvince[previous_layer.feature.properties.name] = false;
        }

      layer.setStyle({
        fillColor: "#b8c746",
          weight: 5,
          color: '#665',
          dashArray: '3',
          fillOpacity: 0.7
      });

      if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
          layer.bringToFront();
      }
      high_lighted_porvince[layer.feature.properties.name] = true;
      set_display_stats(layer.feature.properties.name)
    }

    previous_layer =  layer;
    previous_layer_set = true;
    //console.log(high_lighted_porvince);
}

function onEachFeature(feature, layer) {
    layer.on({
        click: highlightFeature,
        //mouseout: resetHighlight,
    });
}

var geojson = L.geoJson(geoJson_data, {
    onEachFeature: onEachFeature,
    style: set_layer_background
}).addTo(map);
