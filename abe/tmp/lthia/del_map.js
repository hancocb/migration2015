//#######################################
// polygon creation functions
// these functions are used for the manual deliniation of areas
// they are very similar to those used for changing land use
    
var squareMarkerImage;
var overMarkerImage;

var points = [];
var markers = [];
var pointMarker;
var poly;
var polyLineColor = "#33ff33";
var polyFillColor = "#339933";//"#0033CC#335599";

    
function addMarker(point) {
    if(!squareMarkerImage){
        // Square marker icons
        squareMarkerImage = new google.maps.MarkerImage( "/images/square.png",
        // This marker is 11 pixels wide by 11 pixels tall.
        new google.maps.Size(11, 11),
        // The origin for this image is 0,0.
        new google.maps.Point(0,0),
        // The anchor for this image is at 0,11.
        new google.maps.Point(6, 6));
    }
    if(!overMarkerImage){
        // Square marker icons
        overMarkerImage = new google.maps.MarkerImage( "/images/m-over-square.png",
        // This marker is 11 pixels wide by 11 pixels tall.
        new google.maps.Size(11, 11),
        // The origin for this image is 0,0.
        new google.maps.Point(0,0),
        // The anchor for this image is at 0,11.
        new google.maps.Point(6, 6));
    }

    /*
    square.image = "/images/square.png";
    square.iconSize = new google.maps.Size(11, 11);
    square.dragCrossSize = new google.maps.Size(0, 0);
    square.shadowSize = new google.maps.Size(11, 11);
    square.iconAnchor = new google.maps.Point(5, 5);
    */
    
    var shape = {
        coord: [1, 1, 1, 10, 10, 10, 10 , 1],
        type: 'poly'
    };
    
    var newMarker = new google.maps.Marker({
        position: point,
        map: map,
        icon: squareMarkerImage,
        shape: shape,
        title: "delineation point",
        zIndex: 1
    });
    newMarker.setDraggable(true);
    
    markers.push(newMarker);
    
    google.maps.event.addListener(newMarker, "drag", function() {
        drawPoly();
    });
    
    google.maps.event.addListener(newMarker, "mouseover", function() {
        newMarker.setIcon(overMarkerImage);
    });

    google.maps.event.addListener(newMarker, "mouseout", function() {
        newMarker.setIcon(squareMarkerImage);
    });
    
     // Second click listener to remove the square
    google.maps.event.addListener(newMarker, "click", function() {
        // Find out which square to remove
        for(var n = 0; n < markers.length; n++) {
            if(markers[n] == newMarker) {
                markers[n].setMap(null);
                break;
            }
        }
        markers.splice(n, 1);  // remove the clicked square
        drawPoly();
    });
    
    drawPoly();

    /*
    // Make markers draggable
    var newMarker =new google.maps.Marker(point, {icon:square, draggable:true, bouncy:false, dragCrossMove:true});
    
    //map.addOverlay(newMarker);
    */
}

function addDelineateMarker(point) {
  
    //First, previous delineation marker (if any)
    //This DEPENDS on the title for these icons being unique,
    //otherwise unintended marker could be removed
    
    if(pointMarker){
        pointMarker.setMap(null); 
    }
    
    var newMarker = new google.maps.Marker({
        position: point,
        map: map,
        title: "Delineation Point",
        zIndex: 1
    });
    
        
    var thisSession = sessionid;
    var baseRequest = "http://lthia.agriculture.purdue.edu:8080/geoserver/wfs?request=GetFeature&version=1.0.0&srs=EPSG:4326&outputFormat=shape-zip&typeName=maumee:watersheds";
    var sidFilter = "&cql_Filter=session_id=%27"+thisSession+"%27";
    var text = "<input type=\"button\" name=\"viewwtrshd\" class=\"greenbutton\" value=\"Download Shapefile\" onclick=\"window.open('"+baseRequest+sidFilter+"');\" /><br />";

    
     // Second click listener to remove the square
    google.maps.event.addListener(newMarker, "click", function() {       
        infowindow.setContent(text);
        infowindow.open(map,newMarker);        
    });
    
    pointMarker = newMarker;
}


function drawPoly() {

    if(poly){
        poly.setMap(null);
    }
    points = [];

    for(i = 0; i < markers.length; i++) {
        points.push(markers[i].getPosition());
     }

     
     
     
    poly = new google.maps.Polygon({
        paths: points,
        strokeColor: polyLineColor,
        strokeOpacity: 0.8,
        strokeWeight: 3,
        fillColor: polyFillColor,
        fillOpacity: 0.35
    });
    poly.setMap(map);
    
     
    // Close the shape with the last line or not
    //poly = new google.maps.Polygon(points, polyLineColor, 3, .8, polyFillColor,.3);
    //var newUnit = " acres";
    
    var newArea = google.maps.geometry.spherical.computeArea(poly.getPath()); //poly.getArea()/4046.85642;
    
    // hard coded area display
    document.getElementById('mypolyarea').innerHTML = (newArea/4046.85642).toFixed(3);
    document.getElementById('mypolyarea2').innerHTML = (newArea/(1000*1000)).toFixed(3);
     
    
    //map.addOverlay(poly);
}



function removeMarkers() {
    // Clear all markers from the map
    for(var n = 0; n < markers.length; n++) {
        markers[n].setMap(null);                
    }
    // remove original shape
    if(poly) poly.setMap(null);
    // reset markers.
    markers = [];
    points = []
}


function submitPoly() {
    if(markers.length < 3){
        alert("You must have at least three points.");
        return;
    }
    if(pointMarker){
        pointMarker.setMap(null); 
    }
    
    clearstate();
    coords = '';
    points = [];
    for (i=0;i<markers.length;i++){
        var ptLatLng = markers[i].getPosition();
        if(coords == "" ) {
            coords = ptLatLng.lng() + "," + ptLatLng.lat();
        }else{
            coords += "|" + ptLatLng.lng() + "," + ptLatLng.lat(); 
        }
        points.push(markers[i].getPosition());

        markers[i].setMap(null);
    }
     
    // Close the shape with the last line or not
    if(poly){
        poly.setMap(null);
    }
    poly = new google.maps.Polygon({
        paths: points,
        strokeColor: polyLineColor,
        strokeOpacity: 0.8,
        strokeWeight: 3,
        fillColor: polyFillColor,
        fillOpacity: 0.35
    });
    //poly.setMap(map);    - this was removed so points could be placed directly within the delineation area (for del_modify)  
    
    var polyx = poly;
    poly = null;
    
    var lbbox;
    var mousePx=latlngToContainerPixel(map, points[0]);
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
    
    markers = [];
    points = [];
    
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
            
            
            url = "http://lthia.agriculture.purdue.edu/cgi-bin/del_region.py?";
            url += "&coords="+coords;
            url += "&state="+trim(outdata[17]);
            url += "&county="+form.county.value;
            url += "&huc8="+trim(outdata[3]);
            
            var timediv = document.getElementById('watershedTimer');
            var textdiv = document.getElementById('watershedSpan');
            timediv.style.display = 'inline';
            timediv.style.visibility = 'visible';
            textdiv.style.display = 'none';
            textdiv.style.visibility = 'hidden';
            resetTimer('counter');
            openControl('watershed');
        
            runDelineation(url);
        }
    });
}




/**
* From Stackoverflow user "Engineer"
*
* Returns the zoom level at which the given rectangular region fits in the map view. 
* The zoom level is computed for the currently selected map type. 
* @param {google.maps.Map} map
* @param {google.maps.LatLngBounds} bounds 
* @return {Number} zoom level
**/
function getZoomByBounds( map, bounds ){
  var MAX_ZOOM = map.mapTypes.get( map.getMapTypeId() ).maxZoom || 21 ;
  var MIN_ZOOM = map.mapTypes.get( map.getMapTypeId() ).minZoom || 0 ;

  var ne= map.getProjection().fromLatLngToPoint( bounds.getNorthEast() );
  var sw= map.getProjection().fromLatLngToPoint( bounds.getSouthWest() ); 

  var worldCoordWidth = Math.abs(ne.x-sw.x);
  var worldCoordHeight = Math.abs(ne.y-sw.y);

  //Fit padding in pixels 
  var FIT_PAD = 40;

  for( var zoom = MAX_ZOOM; zoom >= MIN_ZOOM; --zoom ){ 
      if( worldCoordWidth*(1<<zoom)+2*FIT_PAD < map.getDiv().offsetWidth && 
          worldCoordHeight*(1<<zoom)+2*FIT_PAD < map.getDiv().offsetHeight )
          return zoom;
  }
  return 0;
}


function zoomToPoly() {
     if(poly && points.length > 0) {
        var bounds = poly.getBounds();
        map.setCenter(bounds.getCenter());
        map.setZoom(getZoomByBounds(map, bounds));
     }
}

/*
 *  These functions are run by the watershed manipulation tools
 *  most of these functions run L-Thia models using the watershed/defined area
 *  others are just general use functions
 *
 *  All functions were created by 
 *  Karl Theller, Purdue University
 *
 *
 */
 
 landusestate = 0;
 changed = false;
 polys = [];

function zoomToWatershed(){
    var bounds = document.getElementById('resultsform').bounds.value;
    var boundpoints = bounds.split("|");
    var newbounds = new google.maps.LatLngBounds();
    
    for(var i = 0 ; i < boundpoints.length ; i++){
        var xy = boundpoints[i].split(',');
        newbounds.extend( new google.maps.LatLng(xy[1],xy[0]));
    }
   
    map.setZoom(getZoomByBounds(map, newbounds));
    map.setCenter(newbounds.getCenter());
}

//###########################################
// The following are the functions used to change land use in an area

var pointsLU = [];
var markersLU = [];
var polyLU;
var polyLineColorLU = "#ffff33";
var polyFillColorLU = "#999933";//"#0033CC#335599";
var polyLineColorLUX = "#bbbb22";
var polyFillColorLUX = "#777722";
var LUMarkerImage;
var LUOverMarkerImage;
var LUDarkMarkerImage;

function addMarkerLU(point) {
    if(!LUMarkerImage){
        // Square marker icons
        LUMarkerImage = new google.maps.MarkerImage( "/images/square-landuse.png",
        // This marker is 11 pixels wide by 11 pixels tall.
        new google.maps.Size(11, 11),
        // The origin for this image is 0,0.
        new google.maps.Point(0,0),
        // The anchor for this image is at 0,11.
        new google.maps.Point(5, 5));
    }
    if(!LUOverMarkerImage){
        // Square marker icons
        LUOverMarkerImage = new google.maps.MarkerImage( "/images/m-over-square-landuse.png",
        // This marker is 11 pixels wide by 11 pixels tall.
        new google.maps.Size(11, 11),
        // The origin for this image is 0,0.
        new google.maps.Point(0,0),
        // The anchor for this image is at 0,11.
        new google.maps.Point(5, 5));
    }
    if(!LUDarkMarkerImage){
        // Square marker icons
        LUDarkMarkerImage = new google.maps.MarkerImage( "/images/square-landuse-dark.png",
        // This marker is 11 pixels wide by 11 pixels tall.
        new google.maps.Size(11, 11),
        // The origin for this image is 0,0.
        new google.maps.Point(0,0),
        // The anchor for this image is at 0,11.
        new google.maps.Point(5, 5));
    }
    
    var shape = {
        coord: [1, 1, 1, 10, 10, 10, 10 , 1],
        type: 'poly'
    };

    // Make markers draggable
    var newMarker = new google.maps.Marker({
        position: point,
        map: map,
        icon: LUMarkerImage,
        shape: shape,
        title: "Land use point",
        zIndex: 1
    });
    newMarker.setDraggable(true);
    
    //var newMarker =new google.maps.Marker(point, {icon:square, draggable:true, bouncy:false, dragCrossMove:true});
    markersLU.push(newMarker);
    
    google.maps.event.addListener(newMarker, "drag", function() {
        drawPolyLU();
    });
    
    google.maps.event.addListener(newMarker, "mouseover", function() {
        newMarker.setIcon(LUOverMarkerImage);
    });

    google.maps.event.addListener(newMarker, "mouseout", function() {
        newMarker.setIcon(LUMarkerImage);
    });
    
     // Second click listener to remove the square
    google.maps.event.addListener(newMarker, "click", function() {
        // Find out which square to remove
        for(var n = 0; n < markersLU.length; n++) {
            if(markersLU[n] == newMarker) {
                markersLU[n].setMap(null);
                break;
            }
        }
        markersLU.splice(n, 1);  // remove the clicked square
        drawPolyLU();
    });

    drawPolyLU();
}

function drawPolyLU() {

    if(polyLU){ 
        polyLU.setMap(null);
    }
    pointsLU = [];

    for(i = 0; i < markersLU.length; i++) {
        pointsLU.push(markersLU[i].getPosition());
     }
     
    // Close the shape with the last line or not
    //polyLU = new google.maps.Polygon(pointsLU, polyLineColorLU, 3, .8, polyFillColorLU,.3);
    
    polyLU = new google.maps.Polygon({
        paths: pointsLU,
        strokeColor: polyLineColorLU,
        strokeOpacity: 0.8,
        strokeWeight: 3,
        fillColor: polyFillColorLU,
        fillOpacity: 0.35
    });
    polyLU.setMap(map);
    
    //var newUnit = " acres";
    var newArea = google.maps.geometry.spherical.computeArea(polyLU.getPath()); //poly.getArea()/4046.85642;
    
    // hard coded area display
    document.getElementById('mypolyareaL').innerHTML = (newArea/4046.85642).toFixed(3);
    document.getElementById('mypolyarea2L').innerHTML = (newArea/(1000*1000)).toFixed(3);
}

function zoomToPolyLU() {
     if(polyLU && pointsLU.length > 0) {
        var bounds = polyLU.getBounds();
        map.setCenter(bounds.getCenter());
        map.setZoom(getZoomByBounds(map, bounds));
     }
}

function removeMarkersLU() {
    // Clear all markers from the map
    for(var n = 0; n < markersLU.length; n++) {
        markersLU[n].setMap(null);        
    }
    // remove original shape
    if(polyLU) polyLU.setMap(null);
    // reset markers.
    markersLU = [];
    pointsLU = []
}

function submitPolyLU() {
    if(landusestate != 0){
        alert('You cannot do that while another land use change is in progress.\nPlease try again in a few seconds');
        return;
    }
    
    if(markersLU.length < 3){
        alert("You must have at least three points.");
        return;
    }
    landusestate++;
    
    
    
    clearstate();
    var coords = '';
    pointsLU = [];
    for (i=0;i<markersLU.length;i++){   
        var ptLatLng = markersLU[i].getPosition();
        if(coords == "" ) {
            coords = ptLatLng.lng() + "," + ptLatLng.lat();
        }else{
            coords += "|" + ptLatLng.lng() + "," + ptLatLng.lat(); 
        }
        pointsLU.push(ptLatLng);
        markersLU[i].setMap(null);
    }
    
    if(polyLU){ 
        polyLU.setMap(null);
    }
    polyLU = new google.maps.Polygon({
        paths: pointsLU,
        strokeColor: polyLineColorLUX,
        strokeOpacity: 0.8,
        strokeWeight: 3,
        fillColor: polyFillColorLUX,
        fillOpacity: 0.35
    });
    polyLU.setMap(map);
     
    // Close the shape with the last line or not
    polys.push(polyLU);
    polyLU = null;
    markersLU = [];
    pointsLU = [];
    
    typeselect = document.getElementById('manualland');
    var estimatespan = document.getElementById('estimate');
    estimatespan.innerHTML = '20';
    
    sessionid = document.getElementById('resultsform').sessionid.value;
    
    changetab('1','watershedContents');
    changetab('1','watershedResults');
    setHTML('changelands',"http://lthia.agriculture.purdue.edu/main/wait.html",function(){
        setHTML('changelands','http://lthia.agriculture.purdue.edu/cgi-bin/del_modify.py?usetype='+(typeselect.options[typeselect.selectedIndex].value)+'&sessionid='+sessionid+'&utmzone='+'17'+'&coords='+coords,function(){
            landusestate--;
            changed = true;
            revertLU();
            loadImpervTable()
        
            //move the export to lthia-lid button to the tools->models tab
            exportbutton_Watershed = document.getElementById('exportLID');
            if(exportbutton_Watershed){
                exportbutton_Tools = document.getElementById('exportLIDTool');
                exportbutton_Tools.setAttribute( 'action', exportbutton_Watershed.getAttribute('action') );
                exportbutton_Tools.innerHTML = exportbutton_Watershed.innerHTML;
            }
        });
    });
}

function removeAreas(){
    for(var i = 0; i < polys.length; i++) {
        polys[i].setMap(null);
    }
}