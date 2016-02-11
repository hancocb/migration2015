if (!google.maps.Polygon.prototype.getBounds) {

        google.maps.Polygon.prototype.getBounds = function(latLng) {

                var bounds = new google.maps.LatLngBounds();
                var paths = this.getPaths();
                var path;
                
                for (var p = 0; p < paths.getLength(); p++) {
                        path = paths.getAt(p);
                        for (var i = 0; i < path.getLength(); i++) {
                                bounds.extend(path.getAt(i));
                        }
                }

                return bounds;
        }

}

if(!Array.prototype.indexOf){
    Array.prototype.indexOf = function(obj, start) {
         for (var i = (start || 0), j = this.length; i < j; i++) {
             if (this[i] === obj) { return i; }
         }
         return -1;
    }
}


//The following are "constants" that are used to locate the MapLayers in the MapLayerOverlay
//array. They need to start at 0 and be sequential, but the order is unimportant
var STALOC = 0;
var WTRLOC = 1;
var SEDLOC = 2;
var EROLOC = 3;
var SOILOC = 4;
var DRALOC = 5;
var HYDLOC = 6;
var GLWLOC = 7;

//These are the locations of the Esri REST layers that are shown on the map
//the other four variables are used to store the map layer objects
var urlHuc = 'http://watersgeo.epa.gov/ArcGIS/rest/services/OW/WBD_WMERC/MapServer';
var tileoverlayHuc;
var urlSediment = 'http://35.8.121.83/AGS/rest/services/hit_sediment/MapServer';
var tileoverlaySediment;
var urlErosion = 'http://35.8.121.83/AGS/rest/services/hit_erosion/MapServer';
var tileoverlayErosion;
//var urlStreams = 'http://watersgeo.epa.gov/ArcGIS/rest/services/OW/NHD_Med_Basic_WMERC/MapServer';
//var tileoverlayStreams; 
var urlSoilType = 'http://geodata.epa.gov/ArcGIS/rest/services/ORD/ROE_NLCD/MapServer';
var tileoverlaySoilType;
var urlDrainage = 'http://soils.esri.com/ArcGIS/rest/services/soils/DrainageClass-DominantCondition/MapServer';
var tileoverlayDrainage;
var urlSoilHydro = 'http://soils.esri.com/ArcGIS/rest/services/soils/HydrologicGroup-DominantCondition/MapServer';
var tileoverlaySoilHydro;
var tileStateOverlay;
var tileGLWMSOverlay;

//mode is used to track which sort of delineation is being performed
//or more specifically, which action should be performed when the Google map is clicked
var mode = 0;
//0: nothing
//1: Point Delineation
//2: HUC based delineation
//3: Manual area delineation
//4: Landuse change

var map; //The Google map object

//watershedOverlay stores the overlay object for the user's delineated object
//this is a geoserver wms based ImageMapLayer
var watershedOverlay

var sessionid; //the current sessionid, set after any delineation is done

var huctype = 12; //tracks the size(type) of HUC being delineated

var loadedtools = 0; //used as bool to track if tools_minitemplate has finished loading yet
var modelstate = 0; //is 1 if a model is currently running, prevents multiple model runs at once

/**
* This just adds a leading 0 to a single digit number
* @param n  a number (usually an int)
* @return   the same number, or if n is between 0 and 10, then
*           n with a leading zero
*/
function pad(n){return n<10 && n>=0 ? '0'+n : n}

/**
*
* load is run to initialize the Google map and to set up the layers for the map
*
*/
var lat1 = 44.547200; 
var lng1 = -86.759277;
var zoom1 = 6;
 
function state_zoom(state) {
    var latlng1 = null;
    var mapzoom = 0;
    if (state == "IN") {
        latlng1 = new google.maps.LatLng(40.0716611, -86.2819752);
        mapzoom = 8;        
    } else if (state == "IL") {
        latlng1 = new google.maps.LatLng(39.739318, -89.504139);
        mapzoom = 7;    
    } else if (state == "MI") {
        latlng1 = new google.maps.LatLng(44.943563, -86.4085867);
        mapzoom = 7;    
    } else if (state == "MN") {
        latlng1 = new google.maps.LatLng(46.4410256, -93.3655146);
        mapzoom = 7;    
    } else if (state == "OH") {
        latlng1 = new google.maps.LatLng(40.2511808, -82.5703755);
        mapzoom = 8;    
    } else if (state == "WI") {
        latlng1 = new google.maps.LatLng(44.7862968, -89.8267049);
        mapzoom = 7;    
    }  else {
        latlng1 = new google.maps.LatLng(44.547200, -86.759277);
        mapzoom = 6;    
    }
    map.setCenter(latlng1);
    map.setZoom(mapzoom);
        
}
function load() {
    //set up the tabs for the user interface
    changetab('3','watershedContents');
    changetab('1','watershedResults');
    changetab('1','tbnav1');
    disabletab('watershedContents','1');
    disabletab('watershedContents','2');
    //load the tools menu
    setHTML('toolsText', 'http://lthia.agriculture.purdue.edu/scripts/tools_minitemplate.html',function(){
        loadedtools = 1;changetab('1','tooltabs');});
    
    //resize the map to the screen
    //the multiple ifs are to deal with different browsers
    element = document.getElementById(resizeelement);
    if(element){
        if (document.body && document.body.offsetWidth) {
            winW = document.body.offsetWidth;
            winH = document.body.offsetHeight;
        }
        if (document.compatMode=='CSS1Compat' &&
            document.documentElement &&
            document.documentElement.offsetWidth ) {
            winW = document.documentElement.offsetWidth;
            winH = document.documentElement.offsetHeight;
        }
        if (window.innerWidth && window.innerHeight) {
            winW = window.innerWidth;
            winH = window.innerHeight;
        }

        element.style.left = remargins + 'px';
        element.style.top = remargins + 'px';
        element.style.width = (winW - remargins * 2) + 'px';
        element.style.height = (winH - remargins * 2) + 'px';
    }

    
    
    map = new google.maps.Map(document.getElementById("map"),{draggableCursor: 'crosshair',center: new google.maps.LatLng(lat1, lng1),
          zoom: zoom1, mapTypeId: google.maps.MapTypeId.ROADMAP,streetViewControl:false,scaleControl: true});
          
    //Add the USGS topographic layer as a map type option
    var WMS_TOPO_MAP = WMSCreateMap( 'USGS', 'http://www.terraserver-usa.com/ogcmap6.ashx', 'DRG',4, 17, 't', 'Topographic Map' );
    map.mapTypes.set('USGS', WMS_TOPO_MAP);
           
    map.setOptions({
        mapTypeControlOptions: {
            mapTypeIds: [
                  google.maps.MapTypeId.ROADMAP,
                  google.maps.MapTypeId.SATELLITE,
                  google.maps.MapTypeId.HYBRID,
                  google.maps.MapTypeId.TERRAIN,
                  'USGS'
            ],
            style: google.maps.MapTypeControlStyle.DROPDOWN_MENU
        }
    });

    //initialize the geocoder
    // the variable is only there to perform the acutal computation between address and latlng
    geocoder = new google.maps.Geocoder();
    
    // set the mouseclick function to be run when the map is clicked
    google.maps.event.addListener(map, "click", mouseclick);

    //*********************************
    //initialize the overlayMapTypes array with empty values so we can insert layers into it
    for(var i = 0 ; i < 7 ; i ++){
        map.overlayMapTypes.push(null);
    }
    
    // load the wms overlay of the huc12 watersheds
    tileStateOverlay = loadWMS("http://devdw.agriculture.purdue.edu:8080/geoserver/wms?", "maumee:huc12_cty2", '');
    tileGLWMSOverlay = loadWMS("http://devdw.agriculture.purdue.edu:8080/geoserver/wms?", "maumee:GLWMS_projects_g", '');
    //add the huc12 map to the list of visible maps
    map.overlayMapTypes.setAt(GLWLOC, tileGLWMSOverlay);
    map.overlayMapTypes.setAt(STALOC, tileStateOverlay);
    
    // create the layers based on Esri REST services
    // these use the arcgislink.js scripts that are imported at the beginning
    tileoverlayHuc = new gmaps.ags.MapOverlay(urlHuc);
    tileoverlaySediment = new gmaps.ags.MapType(urlSediment);
    tileoverlayErosion = new gmaps.ags.MapType(urlErosion);
    //tileoverlayStreams = new gmaps.ags.MapOverlay(urlStreams);
    
    tileoverlaySoilType = new gmaps.ags.MapType(urlSoilType,{name:'Existing Land Use',opacity:0.50});
    tileoverlayDrainage = new gmaps.ags.MapType(urlDrainage,{name:'Dominant Drainage Class',opacity:0.50});
    tileoverlaySoilHydro = new gmaps.ags.MapType(urlSoilHydro,{name:'Dominant Soil Hydrologic Group',opacity:0.50});
    
    updateLayers();
    
    //*********************************
    //initialize infowindow to be displayed when delineation points are clicked 
    //(could potentially be used for other things too)
    infowindow = new google.maps.InfoWindow({
        zIndex: 1,
        content: ""
    });
    
    
    //*********************************
    //initialize the timer that is shown when performing a delineation
    Timer('counter');
}

/**
*
* mouseclick is bound to the 'click' event of the Google map. Thus, it is called whenever someone clicks
* on the map. It must use variables to decide if the user is trying to delineate something
*
*/
function mouseclick(event)//overlay, mousePt)
{
    if(!event){
        return;
    }
    var mycoord = event.latLng;
    var zoom = map.getZoom();
    
    //when delineating by point or by HUC
    if(mode==1 || mode == 2){
        var mainform = document.getElementById('mainform');
        
        var oldmode = mode;
        clearstate();
        
        var latitude = mycoord.lat();
        var longitude = mycoord.lng();
        
        mainform.latitude.value=latitude;
        mainform.longitude.value=longitude;
        
        var lbbox;
        
        //convert the input data into something Geoserver understands
        var mousePx=latlngToContainerPixel(map, mycoord);
        var mapsize=map.getDiv();
        var bounds = map.getBounds();
        var SW = bounds.getSouthWest();
        var NE = bounds.getNorthEast();
        lbbox=SW.lng().toFixed(6) + "," + SW.lat().toFixed(6) + "," + NE.lng().toFixed(6) + "," + NE.lat().toFixed(6);
        //and create the url to request info from Geoserver
        urls = "http://lthia.agriculture.purdue.edu/geoserver/wms?" + "SRS=EPSG:4326&styles=&SERVICE=WMS";

        urls += "&WIDTH=" + mapsize.offsetWidth + "&Height=" + mapsize.offsetHeight;
        urls += "&FORMAT=text/html";
        urls += "&REQUEST=GetFeatureInfo";
        urls += "&BBOX=" + lbbox;
        urls += "&X=" + mousePx.x + "&Y=" + mousePx.y;
        urls += "&INFO_FORMAT=text/html&FEATURE_COUNT=1";

        var urls2 = urls + "&LAYERS=maumee:huc12_cty2&QUERY_LAYERS=maumee:huc12_cty2";
        
        //downloadURL works like the old GDownloadURL, getting the response from a page
        //and passing into the inner function as "data"
        downloadURL(urls2, function(data, responseCode) {
            if (responseCode == 200) {
                //parse the input data
                data = data.split('<tr>');
                var data2 = data[2].replace(/(\t| |\r\n|<td>)/g,"");
                var outdata = data2.split('</td>');
                
                var form = document.getElementById('mainform');
                form.county.value = trim(outdata[10].replace(/(| )(c|C)ounty/g,''));
                form.state.value = trim(outdata[17]);
                form.huc12.value = trim(outdata[5]);
                form.hucarea.value = trim(outdata[6]);
                form.huc8.value = trim(outdata[3]);
                
                //show the Timer and hide the user tools
                var timediv = document.getElementById('watershedTimer');
                var textdiv = document.getElementById('watershedSpan');
                timediv.style.display = 'inline';
                timediv.style.visibility = 'visible';
                textdiv.style.display = 'none';
                textdiv.style.visibility = 'hidden';
                resetTimer('counter');
                openControl('watershed');
                
                var estimatespan = document.getElementById('estimate');
                
                var url 
                if(oldmode == 1){
                    //if this is a point delineation
                    url = trim(urlFromForm('mainform'));
                    estimatespan.innerHTML = '50';
                } else {
                    //if this is a HUC delineation
                    url = 'http://lthia.agriculture.purdue.edu/cgi-bin/del_multihuc.py?huc='+trim(form.huc12.value)+'&huctype='+huctype+'&state='+trim(outdata[17])+'&county='+trim(outdata[10].replace(/(| )(c|C)ounty/g,'')) + '&latitude=' + latitude + '&longitude=' + longitude;
                    if(huctype == 12){
                        estimatespan.innerHTML = '15';
                    } else if(huctype == 10){
                        estimatespan.innerHTML = '25';
                    } else if(huctype == 8){
                        estimatespan.innerHTML = '45';
                    }
                }
                
                //call the del_point or del_multihuc script and put the results in the 'watershedLanduse' div
                if(oldmode == 1){
                    runDelineation(url,mycoord);
                }
                else{
                    if(pointMarker){
                       pointMarker.setMap(null); 
                    }
                    runDelineation(url);
                }
      
            }
        });
        
 

    } else if(mode == 3){//clicking on the map in region delineate mode
        var mainform = document.getElementById('mainform');
        mainform.mode.value = "box";
        if (mycoord){
            addMarker(mycoord);
        }
    } else if(mode == 4){//clicking on the map in landuse change mode
        if (mycoord){
            addMarkerLU(mycoord);
        }
    }
    var mousePx=latlngToContainerPixel(map, mycoord);
}

function runDelineation(url, mycoord){
    var point;
    if (typeof mycoord == 'undefined') {
        // mycoord was not passed
        point = 0;
    }else{
        point = mycoord;
    }
    
    var timediv = document.getElementById('watershedTimer');
    var textdiv = document.getElementById('watershedSpan');
    setHTML('watershedLanduse',url,function(){
    timediv.style.display = 'none';
    textdiv.style.display = 'inline';
    timediv.style.visibility = 'hidden';
    textdiv.style.visibility = 'visible';
    
    //store the new sessionid
    sessionid = document.getElementById('resultsform').sessionid.value;
    addWatershed(sessionid);
    enabletab('1','watershedContents');
    enabletab('2','watershedContents');
    changetab('1','watershedResults');
    changetab('1','watershedContents');
    
    //call the HIT script, though there is only data for the Maumee region
    setHTML('watershedHIT',"http://lthia.agriculture.purdue.edu/main/wait.html",function(){
        setHTML('watershedHIT',"http://lthia.agriculture.purdue.edu/cgi-bin/hit.py" + trim(dataFromForm('mainform')) + '&sessionid=' + sessionid,null);
    });
    
    //load the Landuse spreadsheet
    revertLU();
    
    //load the impervious surface calculator
    loadImpervTable();
    
    //move the export to lthia-lid button to the tools->models tab
    exportbutton_Watershed = document.getElementById('exportLID');
    if(exportbutton_Watershed){
        exportbutton_Tools = document.getElementById('exportLIDTool');
        exportbutton_Tools.setAttribute( 'action', exportbutton_Watershed.getAttribute('action') );
        exportbutton_Tools.innerHTML = exportbutton_Watershed.innerHTML;
    }
    
    if(point != 0){
        //if optional parameter is set
        addDelineateMarker(point);
    }
    alert("sessionid: " + sessionid);
    
});
}

/**
*
* opens the curve number table and allows users to edit the curve numbers that will be used for the model
*
*/
function cntable()
{
    setHTML('entryText', 'cntable.html?sessionid=' + sessionid,function(){
        openControl('entry');
    });

}

/**
*
* opens the emc table and allows users to edit the emc values that will be used for the model
*
*/
function emctable()
{
    setHTML('entryText', 'emctable.html?sessionid=' + sessionid,function(){
        openControl('entry');
    });
}

/**
*
* closes the entry window, which contains either the emc table or the cn table
*
*/
function closeEntry()
{
    var e = document.getElementById('entryText');
    e.innerHTML = '';
    killDiv('entry');
}

/**
*
* Starts HUC delineation with the given huctype
*
* @param htype  The size of the HUC to delineate
*
*/
function setHUC(htype){
    if(mode == 2 && huctype == htype){
        mode = 0;
    } else {
        mode = 2;
    }
    huctype = htype;
    changeButtons();
}

/**
*
* Starts point-based delineation
*
*/
function delineate()
{
    if( mode == 1){
        mode = 0;
    } else {
        mode = 1;
    }
    changeButtons();
}

/**
*
* ends all delineation
*
*/
function clearstate()
{
    mode = 0;
    changeButtons();
}

/**
*
* Sets all of the delineation buttons based on the current mode
* If the users is doing a delineation, the respective button becomes "Stop" or "Stop Delineating"
*
*/
function changeButtons(){
    if(mode==1){
        document.getElementById('DelineateButton').value = "Stop Delineating";
    } else {
        document.getElementById('DelineateButton').value = "Delineate";
    }
    
    if(mode == 2){
        if(huctype == 12){
            document.getElementById('HUC12Button').value = "Stop";
            document.getElementById('HUC10Button').value = "HUC 10";
            document.getElementById('HUC8Button').value = "HUC 8";
        } else if (huctype == 10){
            document.getElementById('HUC12Button').value = "HUC 12";
            document.getElementById('HUC10Button').value = "Stop";
            document.getElementById('HUC8Button').value = "HUC 8";
        } else {
            document.getElementById('HUC12Button').value = "HUC 12";
            document.getElementById('HUC10Button').value = "HUC 10";
            document.getElementById('HUC8Button').value = "Stop";
        }
    } else {
        document.getElementById('HUC12Button').value = "HUC 12";
        document.getElementById('HUC10Button').value = "HUC 10";
        document.getElementById('HUC8Button').value = "HUC 8";
    }
    
    if(mode == 3){
        document.getElementById('switchtextarea').innerHTML = "Click <input type='button' id='switch' value='Stop' onClick='manual();' /> to switch back to viewing mode";

    } else {
        document.getElementById('switchtextarea').innerHTML = "Click " +
            "<input type='button' id='switch' value='Start' onClick='manual();' />" +  
            " to begin digitization.";
    }
    
    if(loadedtools == 1){
        lut = document.getElementById('switchlandusetext');
        if(mode == 4){
                lut.innerHTML =  "Click to create corners for your desired area. Hover your" +
                    " mouse over a point, and when a hand appears, press and drag the point for better fit, or click to remove the point.<br /><br />" +
                    "Click <input type='button' id='switch' value='Stop' onClick='manualLanduse();' /> to switch back to viewing mode";
        } else {
                lut.innerHTML = "Click " +
                    "<input type='button' id='switch' value='Start' onClick='manualLanduse();' />" +  
                    " to begin digitization.";
        }
    }
}

/**
*
* Starts manually selected region delineation
*
*/
function manual() {
    // switch manual watershed area on/off
    if(mode == 3) {
        mode = 0;
    }else{
        mode = 3;
    }
    changeButtons();
}

/**
*
* Starts a map-based landuse change
*
*/
function manualLanduse() {
    // switch manual landuse area selection on/off
    if(mode == 4) {
        mode = 0;
    }else{
        mode = 4;
    }
    changeButtons();
}

/**
*
* Runs a delineation based on the latlng pair entered for the latlng based method
*
*/
function ChkCS() 
{
    //this function works very similarly to the mouseclick function
    //refer to that function for general comments
    var dataform = document.getElementById('ztwdbypoint');
    var mainform = document.getElementById('mainform');
    var latitude = parseFloat(dataform.cy.value);
    var longitude = parseFloat(dataform.cx.value);
    
    mainform.latitude.value=latitude;
    mainform.longitude.value=longitude;
    mainform.mode.value = "latlng";
    
    var mycoord = new google.maps.LatLng(latitude, longitude);
    
    map.setCenter(mycoord);
        
    var lbbox;
        
    var mousePx=latlngToContainerPixel(map, mycoord);
    var mapsize=map.getDiv();
    var bounds = map.getBounds();
    var SW = bounds.getSouthWest();
    var NE = bounds.getNorthEast();
    lbbox=SW.lng().toFixed(6) + "," + SW.lat().toFixed(6) + "," + NE.lng().toFixed(6) + "," + NE.lat().toFixed(6);
    urls = "http://lthia.agriculture.purdue.edu/geoserver/wms?" + "SRS=EPSG:4326&styles=&SERVICE=WMS";

    urls += "&WIDTH=" + mapsize.offsetWidth + "&Height=" + mapsize.offsetHeight;
    urls += "&FORMAT=text/html";
    urls += "&REQUEST=GetFeatureInfo";
    urls += "&BBOX=" + lbbox;
    urls += "&X=" + mousePx.x + "&Y=" + mousePx.y;
    urls += "&INFO_FORMAT=text/html&FEATURE_COUNT=1";

    var urls2 = urls + "&LAYERS=maumee:huc12_cty2&QUERY_LAYERS=maumee:huc12_cty2";
    
    downloadURL(urls2, function(data, responseCode) {
        if (responseCode == 200) {
            data = data.split('<tr>');
            var data2 = data[2].replace(/(\t| |\r\n|<td>)/g,"");
            var outdata = data2.split('</td>');
            
            var form = document.getElementById('mainform');
            form.county.value = trim(outdata[10].replace(/(| )(c|C)ounty/g,''));
            form.state.value = trim(outdata[17]);
            form.huc12.value = trim(outdata[5]);
            form.hucarea.value = trim(outdata[6]);
            form.huc8.value = trim(outdata[3]);
            
            var timediv = document.getElementById('watershedTimer');
            var textdiv = document.getElementById('watershedSpan');
            timediv.style.display = 'inline';
            timediv.style.visibility = 'visible';
            textdiv.style.display = 'none';
            textdiv.style.visibility = 'hidden';
            resetTimer('counter');
            openControl('watershed');
            
            var estimatespan = document.getElementById('estimate');
            
            var url 
            url = trim(urlFromForm('mainform'));
            estimatespan.innerHTML = '50';
            
            runDelineation(url,mycoord);
        }
    });
    
    
    
}

/**
*
* Uses the sessionid to load the watershed's outline from geoserver and put it on the map
* 
* @param session    the sessionid
*
*/
function addWatershed (session) {
    if(watershedOverlay != null){
        map.overlayMapTypes.setAt(WTRLOC, null);
        watershedOverlay = null;
    }
    watershedOverlay = loadWMS("http://lthia.agriculture.purdue.edu:8080/geoserver/wms?", "maumee:watersheds", "&cql_Filter=session_id='" + session + "'");
    map.overlayMapTypes.setAt(WTRLOC, watershedOverlay);
}

/**
*
* Use Google's Geocoder to turn an address or location name into a latlng, then zoom the map to that point
*
*/
function codeAddress() {
  var address = document.getElementById('geoaddress').value;
  geocoder.geocode( { 'address': address}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      map.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
          map: map,
          position: results[0].geometry.location
      });
    } else {
      alert('Geocode was not successful for the following reason: ' + status);
    }
  });
}

//######################################################################################
//layer functions
//######################################################################################

/**
*
* Toggles a MapLayer on and off
*
* @param layer  The layer object
*
*/
function toggleLayer(layer) {
    if (layer.getMap()) {
        layer.setMap(null);
    } else {
        layer.setMap(map);

    }
} 

/**
*
* Toggles a OverlayMapType entry on and off
*
* @param layer  The overlay object
* @param loc    The index in the array
*
*/
function toggleOverlay(layer, loc) {
    if (map.overlayMapTypes.getAt(loc) != null) {
        map.overlayMapTypes.setAt(loc, null);
    } else {
        map.overlayMapTypes.setAt(loc, layer);
    }
} 

/**
*
* Sets the MapLayer's visibility to state
*
* @param layer  The layer object
* @param state  A boolean of the new visiblity state
*
*/
function setLayer(layer, state) {
    if (state) {
        layer.setMap(map);
    } else {
        layer.setMap(null);
    }
} 

/**
*
* Sets the OverlayMapType entry's visibility to state
*
* @param layer  The overlay object
* @param loc    The index in the array
* @param state  A boolean of the new visiblity state
*
*/
function setOverlay(layer, loc, state) {
    if (state) {
        map.overlayMapTypes.setAt(loc, layer);
    } else {
        map.overlayMapTypes.setAt(loc, null);
    }
}

/**
*
* Sets the visibility of the streams layer when the corresponding checkbox changes state
*
*//*
function switchstreams()
{
    setLayer(tileoverlayStreams, document.getElementById("stream").checked);
}*/

/**
*
* Sets the visibility of the HUCs layer when the corresponding checkbox changes state
*
*/
function switchHuc()
{
    setLayer(tileoverlayHuc, document.getElementById("hucWI").checked);
}

/**
*
* Sets the visibility of the Maumee HUC12 layer when the corresponding checkbox changes state
*
*/
function set_stateslayer()
{
    setOverlay(tileStateOverlay,STALOC,document.getElementById("setstates").checked);
}

/**
*
* Sets the visibility of the HIT Sediment layer when the corresponding checkbox changes state
*
*/
function switchHitSediment()
{
    setOverlay(tileoverlaySediment, SEDLOC, document.getElementById("hitSediment").checked);
}

/**
*
* Sets the visibility of the HIT Erosion layer when the corresponding checkbox changes state
*
*/
function switchHitErosion()
{
    setOverlay(tileoverlayErosion, EROLOC, document.getElementById("hitErosion").checked);
}

/**
*
* Sets the visibility of the Hydro Soil layer when the corresponding checkbox changes state
*
*/
function switchHydroGroup()
{
    setOverlay(tileoverlaySoilHydro, HYDLOC, document.getElementById("hydroGroup").checked);
} 

/**
*
* Sets the visibility of the Drainage layer when the corresponding checkbox changes state
*
*/
function switchDrainage()
{
    setOverlay(tileoverlayDrainage, DRALOC, document.getElementById("drainage").checked);
}

/**
*
* Sets the visibility of the Soil Type layer when the corresponding checkbox changes state
*
*/
function switchSoilType()
{
    setOverlay(tileoverlaySoilType, SOILOC, document.getElementById("soilType").checked);
}

/**
*
* Sets the visibility of the GLWMS layer when the corresponding checkbox changes state
*
*/
function switchGLWMS()
{
    setOverlay(tileGLWMSOverlay, GLWLOC, document.getElementById("GLWMS").checked);
}

function updateLayers(){
    switchSoilType();
    switchDrainage();
    switchHydroGroup();
    switchHitErosion();
    switchHitSediment();
    set_stateslayer();
    switchHuc();
    //switchstreams();
    switchGLWMS();
}
 
/**
*
* Run the L-THIA model with the information the user has given it
*
*/
function runmodel()
{
    if(modelstate){
        alert("Another model is being run.\nPlease Wait.");
        return;
    }
    modelstate = 1;
    changetab('1','watershedContents');
    changetab('4','watershedResults');
    sessionid = document.getElementById('resultsform').sessionid.value;
    setHTML('wRGdiv','http://lthia.agriculture.purdue.edu/main/wait.html',function(){
        var form = document.getElementById('mainform');
        setHTML('wRGdiv','model_edit.py?state=' + form.state.value + '&county=' + form.county.value + '&sessionid=' + sessionid,function(){
        //setHTML('wRGdiv','model_edit.py?state=' + form.state.value + '&county=' + form.county.value + '&sessionid=' + sessionid,function(){
            setHTML('watershedResultsTables','http://lthia.agriculture.purdue.edu/main/wait.html',function(){
                var form = document.getElementById('mainform');
                setHTML('watershedResultsTables','modeltables.py?state=' + form.state.value + '&county=' + form.county.value + '&sessionid=' + sessionid,function(){
                    modelstate = 0;
                }); 
            });
        }); 
    });
    
}
 
//######################################################################################
// The following functions are for the graph outputs of the L-THIA Model
//######################################################################################
/**
* Change the flow type that will be drawn on the graph
*/
function FlowSelect() {
    var form = document.getElementById("graphMain");
    var FlowType = form.FlowSelection.options[form.FlowSelection.selectedIndex].value ; 
 
    document.getElementById("graphData").FlowType.value = FlowType ; 
} 
/**
* Change the units of the flow type that will be drawn on the graph
*/
function FlowUnitSelect() {
    var form = document.getElementById("graphMain");
    var FlowUnit = form.FlowUnitSelection.options[form.FlowUnitSelection.selectedIndex].value ; 
    document.getElementById("graphData").FlowUnit.value = FlowUnit ; 
} 
/**
* Change the load values that will be drawn on the graph
*/
function LoadSelect() {
    var form = document.getElementById("graphMain");
    var graph = document.getElementById("graphData");
    var LoadType = form.LoadSelection.options[form.LoadSelection.selectedIndex].value ; 
    graph.LoadType.value = LoadType ; 
    if (LoadType == "graph_Ec") {
        form.LoadUnitSelection.value = "mpn" ;
        graph.LoadUnit.value = form.LoadUnitSelection.value ; 
    } else {
        form.LoadUnitSelection.value = "ton" ;
        graph.LoadUnit.value = form.LoadUnitSelection.value ; 
    }
} 
/**
* Change the units of the load values that will be drawn on the graph
*/
function LoadUnitSelect() {
    var form = document.getElementById("graphMain");
    var graph = document.getElementById("graphData");
    var LoadUnit = form.LoadUnitSelection.options[form.LoadUnitSelection.selectedIndex].value ; 
    graph.LoadUnit.value = LoadUnit ; 
    if (LoadUnit == "mpn") { ;
        form.LoadSelection.value = "graph_Ec" ;
        graph.LoadType.value = form.LoadSelection.value ; 
    } else { 
/*     form.LoadSelection.value = "graph_TS" ;
      document.rstFrame.LoadType.value = form.LoadSelection.value ; */
    }
}
/**
* Change the period of the graph (Day Month or Year)
*/
function FlowUnitSelect2() {
    var form = document.getElementById("graphMain");
    var graph = document.getElementById("graphData");
    var FlowUnit2 = form.FlowUnitSelection2.options[form.FlowUnitSelection2.selectedIndex].value ; 
    graph.Interval.value = FlowUnit2 ; 
} 
/**
* Draw/Update the graph with the newest selections
*/
function graphSubmit() {
    frame = document.getElementById("rstFrame");
    frame.innerHTML = " ";
    setHTML('rstFrame','http://lthia.agriculture.purdue.edu/main/wait.html',function(){
        setHTML('rstFrame',trim(urlFromForm("graphData")),null);
    });
}

//######################################################################################
// The following functions run the Landuse Spreadsheet
//###################################################################################### 
/**
* Add a new row to the Landuse spreadsheet
* Duplicate rows are not allowed
*/
function addNewLU(){
    var luSelection = document.getElementById('addlanduse');
    var val = pad(luSelection.options[luSelection.selectedIndex].value);
    var name = luSelection.options[luSelection.selectedIndex].text;
    
    var existTest = document.getElementById('lu'+val);
    if(existTest){
        alert("That landuse is already present in the table");
        return;
    }
    
    var lutable = document.getElementById('lutable');
    lutable.innerHTML = lutable.innerHTML.replace("<!-- extension -->", 
            '<tr><td width="200" id="lu'+val+'">'+name+'</td>'+
            '<td width="100"><input class="luVal" onchange="updateTotal();" type="text" name="lu'+val+'A" size="4" style="text-align:right;" value="0.0"></td>'+
            '<td width="100"><input class="luVal" onchange="updateTotal();" type="text" name="lu'+val+'B" size="4" style="text-align:right;" value="0.0"></td>'+
            '<td width="100"><input class="luVal" onchange="updateTotal();" type="text" name="lu'+val+'C" size="4" style="text-align:right;" value="0.0"></td>'+
            '<td width="100"><input class="luVal" onchange="updateTotal();" type="text" name="lu'+val+'D" size="4" style="text-align:right;" value="0.0"></td>'+
            '</tr><!-- extension -->');
 
}
/**
* update the "Total Landuse Post-Changes" value so the user knows if their changes have changed
* to total amount of land
*/
function updateTotal(){
    var elems = document.getElementsByClassName('luVal');

    var myLength = elems.length,
    total = 0;

    for (var i = 0; i < myLength; ++i) {
      total += elems[i].value * 1.0;
    }

    document.getElementById('totallu').innerHTML = total.toFixed(2);
}
/**
* Reverts the Landuse spreadsheet to the last "Updated" state
*/
function revertLU(){
    setHTML('lusheet',"http://lthia.agriculture.purdue.edu/main/wait.html",function(){
        setHTML('lusheet',"http://lthia.agriculture.purdue.edu/cgi-bin/lutable.py?sessionid=" + sessionid,function(){
            updateTotal();
        });
    });
    
}
/**
* Submit any changes made by the user, then reload the table
* the reload avoids an issue that was causing lines in the table to become empty
*/
function updateLU(){
//    callScript(urlFromForm('cnform'),closeEntry);
    var newTotal = document.getElementById('totallu').innerHTML;
    var oldTotal = document.getElementById('oldtotallu').innerHTML;

    if(Math.abs(newTotal-oldTotal) > 10){
        var r=confirm("You have made a major change to the total landuse.\nPress OK to continue or Cancel to return to editing");
        if (r==false)
        {
            return;
        } 
    }
    setHTML('changelands',urlFromForm('luform'),function(){
    revertLU()
    loadImpervTable();});
} 
 
//######################################################################################
// The following function resizes the map to fit the window as it changes sizes
//######################################################################################
/**
* As stated, this function is called on the window changing size (or shape) and resizes
*  the map to the new window size
*/
function resize(){ 
    element = document.getElementById('map');
    if(element){
        if (document.body && document.body.offsetWidth) {
            winW = document.body.offsetWidth;
            winH = document.body.offsetHeight;
        }
        if (document.compatMode=='CSS1Compat' &&
            document.documentElement &&
            document.documentElement.offsetWidth ) {
            winW = document.documentElement.offsetWidth;
            winH = document.documentElement.offsetHeight;
        }
        if (window.innerWidth && window.innerHeight) {
            winW = window.innerWidth;
            winH = window.innerHeight;
        }
        
        element.style.left = remargins + 'px';
        element.style.top = remargins + 'px';
        element.style.width = (winW - remargins * 2) + 'px';
        element.style.height = (winH - remargins * 2) + 'px';
    }
}

google.maps.event.addDomListener(window, 'resize', resize);

//######################################################################################
// The following functions run the Impervious Surface Calculator
//###################################################################################### 
/**
* Calculates the impervious surface area 
* to a specific row of the table
*/
function updateImperviousRow(rowID){
    var rowArea = document.getElementById('landUseArea'+rowID);
    var percentImpervious = document.getElementById('imperviousPercent'+rowID);
    if(percentImpervious.value > 100.0 || percentImpervious.value < 0.0){
        alert("Invalid percentage entered: either less than 0 or greater than 100.");
        percentImpervious.value = 0;
    }
    if(isNaN(percentImpervious.value)){
        alert("Invalid percentage entered: not a legal number.\nBe sure to remove any commas or other symbols (besides possibly a single decimal point).");
        percentImpervious.value = 0;
    }
    var impervArea = rowArea.value * percentImpervious.value * .01;
   
    
    //alert("rowarea=" + rowArea.value + " percentimperv=" + percentImpervious.value + " impervArea=" + impervArea);
    document.getElementById('imperviousArea'+rowID).innerHTML = impervArea.toFixed(2);
    //alert("the value of the imperviousrow+rowid element is" + document.getElementById('imperviousArea'+rowID).innerHTML);
    updateImperviousTotal();
}

/**
* Calculates the total impervious surface area
* by summing the totals from each row
*/
function updateImperviousTotal(){
    var elems = document.getElementsByClassName('imperviousArea');

    var myLength = elems.length;
    total = 0;

    for (var i = 0; i < myLength; ++i) {
      total += elems[i].innerHTML * 1.0;
    }

    document.getElementById('imperviousAreaTotal').innerHTML = total.toFixed(2);
}
/**
* Loads the Landuse spreadsheet to the last "Updated" state
*/
function loadImpervTable(){
    setHTML('impervSheet',"http://lthia.agriculture.purdue.edu/main/wait.html",function(){
        setHTML('impervSheet',"http://lthia.agriculture.purdue.edu/cgi-bin/impervious.py?sessionid=" + sessionid,function(){
            updateImperviousTotal();
        });
    });
}





//////////////for google analytics//////////
<!--
 var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
 document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
-->
 </script>

<script type="text/javascript">
<!--
 try {
    var pageTracker = _gat._getTracker("UA-9568803-1");
    pageTracker._trackPageview();
}
catch(err) 
{}
-->



