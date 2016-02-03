
    var lonlat;
    var lonlat2;
    var map;
    var untiled;
    var tiled;
    var pureCoverage = false;
    var url_string;
    var deg_buffer;
    var partype_filter='';
    var server_url = "/geoserver"
    // pink tile avoidance
    OpenLayers.IMAGE_RELOAD_ATTEMPTS = 5;
    // make OL compute scale according to WMS spec
    OpenLayers.DOTS_PER_INCH = 25.4 / 0.28;

    function init(){
        // if this is just a coverage or a group of them, disable a few items,
        // and default to jpeg format
        format = 'image/png';
        if(pureCoverage) {
            document.getElementById('filterType').disabled = true;
            document.getElementById('filter').disabled = true;
            document.getElementById('antialiasSelector').disabled = true;
            document.getElementById('updateFilterButton').disabled = true;
            document.getElementById('resetFilterButton').disabled = true;
            document.getElementById('jpeg').selected = true;
            format = "image/jpeg";
        }

        var options = {
          //projection: new OpenLayers.Projection("EPSG:900913"),
          projection: new OpenLayers.Projection("EPSG:3857"),
          units: "m",
          controls: [new OpenLayers.Control.Navigation(), 
                     new OpenLayers.Control.PanZoomBar()],
                    
          numZoomLevels: 20,
          zoomMethod: null,
          maxResolution: 156543.0339,
          maxExtent: new OpenLayers.Bounds(
            -20037500,
            -20037500,
            20037500,
            20037500
          )
        };          
        
        map = new OpenLayers.Map('map', options);
        var button_1 = new OpenLayers.Control.Button({
            displayClass: "MyButton_1", trigger: resize_map
            });
        var button_2 = new OpenLayers.Control.Button({
            displayClass: "MyButton_2", trigger: orig_sze_map
            });

        panel = new OpenLayers.Control.Panel({defaultControl: button_2});
        panel.addControls([button_1, button_2]);
        map.addControl(panel);      
        
        tiled = new OpenLayers.Layer.WMS(
            "inwater - Tiled", server_url+"/wms",
            {
                projection: new OpenLayers.Projection("EPSG:4326"),
                height: '330',
                width: '624',
                layers: 'inwater:inwater',
                styles: '',
                srs: 'EPSG:4326',
                format: format,
                tiled: 'true',
                transparent: 'true',
                tilesOrigin : map.maxExtent.left + ',' + map.maxExtent.bottom
            },
            {
                buffer: 0,
                displayOutsideMaxExtent: true
            } 
        );
        
        // setup single tiled layer
        //seems that it won't be used anymore
        untiled = new OpenLayers.Layer.WMS(
            "Monitoring Sites", server_url+"/wms",
            {
            projection: new OpenLayers.Projection("EPSG:4326"),
                
                layers: 'inwater:inwater',
                styles: '',
                srs: 'EPSG:4326',                        
                transparent: 'true'
            },
            {singleTile: true, ratio: 1, buffer: 50} 
        );

        var gphy = new OpenLayers.Layer.Google(
            "Google Physical",
            {type: google.maps.MapTypeId.TERRAIN}
            // used to be {type: G_PHYSICAL_MAP}
        );
        var gmap = new OpenLayers.Layer.Google(
            "Google Streets", // the default
            {numZoomLevels: 20}
            // default type, no change needed here
        );
        var ghyb = new OpenLayers.Layer.Google(
            "Google Hybrid",
            {type: google.maps.MapTypeId.HYBRID, numZoomLevels: 20}
            // used to be {type: G_HYBRID_MAP, numZoomLevels: 20}
        );
        var gsat = new OpenLayers.Layer.Google(
            "Google Satellite",
            {type: google.maps.MapTypeId.SATELLITE, numZoomLevels: 22}
            // used to be {type: G_SATELLITE_MAP, numZoomLevels: 22}
        );

        var wms = new OpenLayers.Layer.WMS( "OpenLayers WMS",
                  "http://vmap0.tiles.osgeo.org/wms/vmap0",
                  {layers: 'basic'} );

        layerMapnik = new OpenLayers.Layer.OSM.Mapnik("Mapnik");

        untiled.setVisibility(false);
        
        aliasproj = new OpenLayers.Projection("EPSG:3857");
        gmap.projection=gsat.projection=ghyb.projection=gphy.projection=layerMapnik.projection=untiled.projection=aliasproj;           
        map.addLayers([ gmap, gsat, ghyb, gphy, layerMapnik, untiled]); 

        var lat=39.7690048218;
        var lon=-86.157333374;
        var zoom=7;
        var lonLat = new OpenLayers.LonLat(lon, lat).transform(new OpenLayers.Projection("EPSG:4326"), map.getProjectionObject());
        map.setCenter (lonLat, zoom);           
        map.addControl(new OpenLayers.Control.LayerSwitcher());

        
        // wire up the option button
        var options = document.getElementById("options");
        var popup;
        OpenLayers.Control.Click = OpenLayers.Class( OpenLayers.Control, {                
            defaultHandlerOptions: {
                'single': true,
                'double': false,
                'pixelTolerance': 0,
                'stopSingle': false,
                'stopDouble': false
            },

            initialize: function(options) {
                this.handlerOptions = OpenLayers.Util.extend(
                    {}, this.defaultHandlerOptions
                );
                OpenLayers.Control.prototype.initialize.apply(
                    this, arguments
                ); 
                this.handler = new OpenLayers.Handler.Click(
                    this, {
                        'click': this.trigger
                    }, this.handlerOptions
                );
            }, 

            trigger: function(e) {
                if( map.getLayersByName('Monitoring Sites')[0].visibility==true ){
                    document.body.style.cursor = 'default';
                    if(popup){
                        map.removePopup(popup);                                   
                    }               

                    lonlat = map.getLonLatFromViewPortPx(e.xy);
                    var EPSG4326 = new OpenLayers.Projection("EPSG:4326");
                    var EPSG900913 = new OpenLayers.Projection("EPSG:900913");
                    lonlat = lonlat.transform(EPSG900913, EPSG4326);                    
                    lonlat2 = map.getLonLatFromViewPortPx(e.xy);
                
                    if(map.getZoom()<11){
                        deg_buffer=0.05;
                    }else if(map.getZoom()>=11 && map.getZoom()<13){
                        deg_buffer=0.01;
                    }else if(map.getZoom()>=13 && map.getZoom()<16){
                        deg_buffer=0.005;
                    }else{
                        deg_buffer=0.001;
                    }
                
                    var site_info;
            
                    var Agency_name=document.getElementById('Agency').value;
                        Agency_name=Agency_name.replace("&","&amp;");
                    var Dataset_name=document.getElementById('dataset').value;
                        Dataset_name=Dataset_name.replace("&","&amp;");                         
                    var huc_ln=document.getElementsByName('huc').length;
                    var huc_type = '' ;
                    var huc_number = '' ;

                    for (i=0;i<huc_ln;i++){
                        if(document.getElementsByName('huc')[i].checked==true && document.getElementById('huc_code').value!=''){
                            huc_type=document.getElementsByName('huc')[i].value;
                            huc_number=document.getElementById('huc_code').value;
                        }
                    }    

                    if(huc_type == '' && huc_number == ''){
                        var wfs_url=server_url+"/wfs?service=wfs&version=1.0.0&request=GetFeature&outputFormat=application/json&typeName=inwater:inwater&propertyName=gid,agency_type,agency_organization,name,description,site_no,parameter,parameter_type,frequency,publicly_available,quality,start_date,end_date,huc_12,contact_url&Filter="+escape("<ogc:Filter xmlns:gml='http://www.opengis.net/gml' xmlns:ogc='http://www.opengis.net/ogc'><ogc:And><ogc:And><ogc:DWithin><ogc:PropertyName>clipped_geom</ogc:PropertyName><gml:Point><gml:coordinates>"+lonlat.lon+","+lonlat.lat+"</gml:coordinates></gml:Point><Distance units='deg'>"+deg_buffer+"</Distance></ogc:DWithin><ogc:PropertyIsEqualTo><ogc:PropertyName>agency_type</ogc:PropertyName><ogc:Literal>"+document.getElementById('High_Agency').value+"</ogc:Literal></ogc:PropertyIsEqualTo><ogc:PropertyIsEqualTo><ogc:PropertyName>agency_organization</ogc:PropertyName><ogc:Literal>"+Agency_name+"</ogc:Literal></ogc:PropertyIsEqualTo><ogc:PropertyIsEqualTo><ogc:PropertyName>name</ogc:PropertyName><ogc:Literal>"+Dataset_name+"</ogc:Literal></ogc:PropertyIsEqualTo><ogc:PropertyIsLike wildCard='*' singleChar='.' escape='!'><ogc:PropertyName>description</ogc:PropertyName><ogc:Literal>*"+document.getElementById('loc').value+"*</ogc:Literal></ogc:PropertyIsLike></ogc:And>"+partype_filter+"</ogc:And></ogc:Filter>");
                                            
                    }else{
                        var wfs_url=server_url+"/wfs?service=wfs&version=1.0.0&request=GetFeature&outputFormat=application/json&typeName=inwater:inwater&propertyName=gid,agency_type,agency_organization,name,description,site_no,parameter,parameter_type,frequency,publicly_available,quality,start_date,end_date,huc_12,contact_url&Filter="+escape("<ogc:Filter xmlns:gml='http://www.opengis.net/gml' xmlns:ogc='http://www.opengis.net/ogc'><ogc:And><ogc:And><ogc:DWithin><ogc:PropertyName>clipped_geom</ogc:PropertyName><gml:Point><gml:coordinates>"+lonlat.lon+","+lonlat.lat+"</gml:coordinates></gml:Point><Distance units='deg'>"+deg_buffer+"</Distance></ogc:DWithin><ogc:PropertyIsEqualTo><ogc:PropertyName>agency_type</ogc:PropertyName><ogc:Literal>"+document.getElementById('High_Agency').value+"</ogc:Literal></ogc:PropertyIsEqualTo><ogc:PropertyIsEqualTo><ogc:PropertyName>agency_organization</ogc:PropertyName><ogc:Literal>"+Agency_name+"</ogc:Literal></ogc:PropertyIsEqualTo><ogc:PropertyIsEqualTo><ogc:PropertyName>name</ogc:PropertyName><ogc:Literal>"+Dataset_name+"</ogc:Literal></ogc:PropertyIsEqualTo><ogc:PropertyIsEqualTo><ogc:PropertyName>"+huc_type+"</ogc:PropertyName><ogc:Literal>"+huc_number+"</ogc:Literal></ogc:PropertyIsEqualTo><ogc:PropertyIsLike wildCard='*' singleChar='.' escape='!'><ogc:PropertyName>description</ogc:PropertyName><ogc:Literal>*"+document.getElementById('loc').value+"*</ogc:Literal></ogc:PropertyIsLike></ogc:And>"+partype_filter+"</ogc:And></ogc:Filter>");
                    }
                
                    wfs_url=wfs_url.replace(escape("<ogc:PropertyIsEqualTo><ogc:PropertyName>agency_type</ogc:PropertyName><ogc:Literal>all</ogc:Literal></ogc:PropertyIsEqualTo>"), escape(""));
                    wfs_url=wfs_url.replace(escape("<ogc:PropertyIsEqualTo><ogc:PropertyName>agency_organization</ogc:PropertyName><ogc:Literal>all</ogc:Literal></ogc:PropertyIsEqualTo>"), escape(""));
                    wfs_url=wfs_url.replace(escape("<ogc:PropertyIsEqualTo><ogc:PropertyName>name</ogc:PropertyName><ogc:Literal>all</ogc:Literal></ogc:PropertyIsEqualTo>"), escape(""));
                    wfs_url=wfs_url.replace(escape("<ogc:PropertyIsEqualTo><ogc:PropertyName>parameter_type</ogc:PropertyName><ogc:Literal>all</ogc:Literal></ogc:PropertyIsEqualTo>"), escape(""));
                
                    //for test only
                    //wfs_url = "/static/inwater/js/mockgeoserver.js"
                    
                    $.getJSON( wfs_url, function( data ) {
                        if(data['totalFeatures']<=0){
                            site_info = "<html><body><font size=\"2\">There is no result within " + 100000 * deg_buffer + " meters from the click. Please zoom in and click again !</font></body></html>";
                        }else{
                            site_data = data['features'][0]['properties']
                            if (site_data['contact_url'].substring(0,4)!="http"){
                                    site_data['contact_url']
                            }

                            site_info = 
                                  "Agency: "+site_data['agency_organization']+"<br/>"+
                                  "Dataset: "+site_data['name']+"<br/>"+
                                  "Site #: "+site_data['site_no']+"<br/>"+
                                  "Parameter(s) sampled: "+site_data['parameter']+"<br/>"+
                                  "Parameter Type: "+site_data['parameter_type']+"<br/>"+
                                  "Monitoring Frequency: "+site_data['frequency']+"<br/>"+
                                  "Publicly Available?: "+site_data['publicly_available']+"<br/>"+
                                  "Data Quality Information: "+site_data['quality']+"<br/>"+
                                  "Date of record: "+site_data['start_date']+" to "+site_data['end_date']+"<br/>"+
                                  "HUC12: "+site_data['huc_12']+"<br/>"+
                                  "For more information: <a title=\"Click URL\" onClick=\"window.open('"+site_data['contact_url']+"')\">"+site_data['contact_url']+"</a><br/>"+
                                  "<hr style=\"color: 'black'; height: '2'; width: '300'\"><br/>";  
                        }
                        popup = new OpenLayers.Popup.FramedCloud("featurePopup", lonlat2,
                                    new OpenLayers.Size(300, 300),
                                    site_info,
                                    null, true);
                        popup.autoSize = false;
                        map.addPopup(popup);
                    });
                    OpenLayers.Event.stop(e);               
                }               
            }
        }); //end of OpenLayers.Control.Click
    
        var click = new OpenLayers.Control.Click();
        map.addControl(click);
        click.activate();
    
        // From here to the end of init(), display agency type
        var xmlHttp;
        try {
            // Firefox, Opera 8.0+, Safari
            xmlHttp = new XMLHttpRequest();
        } catch (e) {
            // Internet Explorer
            try {
                xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
            } catch (e) {
                try {
                    xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
                } catch (e) {
                    alert("Your browser does not support AJAX!");
                    return false;
                }
            }
        }

        $.getJSON( "agency/all/all/", function( data ) {
            
            $.each( data["all_agency_types"], function( key, val ) {
                var option = '<option value="'+val+'">'+val+'</option>'
                $(option).appendTo($("#High_Agency"))
            });
            $.each( data["all_agencies"], function( key, val ) {
                var option = '<option value="'+val+'">'+val+'</option>'
                $(option).appendTo($("#Agency"))
            });
            $.each( data["all_datasets"], function( key, val ) {
                var option = '<option value="'+val+'">'+val+'</option>'
                $(option).appendTo($("#dataset"))
            });
        });

    } //end of init!!!!!!!!!!!!!!!
    
    function showall() {
        document.getElementById('High_Agency').value = 'all';
        document.getElementById('Agency').value = 'all';
        document.getElementById('dataset').value = 'all';
        document.getElementById('loc').value = '';
        document.getElementById("cAll").checked = true;
        uck_par();
        document.getElementsByName('huc')[0].checked = false;
        document.getElementsByName('huc')[1].checked = false;
        document.getElementsByName('huc')[2].checked = false;
        document.getElementById('huc_code').value = '';
        url_string = "";
        updateFilter();
        map.getLayersByName('Monitoring Sites')[0].setVisibility(true);

    }

    // sets the HTML provided into the nodelist element
    function setHTML(response) {
        document.getElementById('nodelist').innerHTML = response.responseText;
    };

    // shows/hide the control panel
    function toggleControlPanel(event) {
        event.stopPropagation();
        map.updateSize()
    }

    // Tiling mode, can be 'tiled' or 'untiled'            
    function setTileMode(tilingMode) {
        if (tilingMode == 'tiled') {
            untiled.setVisibility(false);
            tiled.setVisibility(true);
            map.setBaseLayer(tiled);
        } else {
            untiled.setVisibility(true);
            tiled.setVisibility(false);
            map.setBaseLayer(untiled);
        }
    }

    // changes the current tile format
    function setImageFormat(mime) {
        // we may be switching format on setup
        if (tiled == null)
            return;

        tiled.mergeNewParams({
            format: mime
        });
        untiled.mergeNewParams({
            format: mime
        });
    }

    // sets the chosen style
    function setStyle(style) {
        // we may be switching style on setup
        if (tiled == null)
            return;

        tiled.mergeNewParams({
            styles: style
        });
        untiled.mergeNewParams({
            styles: style
        });
    }

    function setAntialiasMode(mode) {
        tiled.mergeNewParams({
            format_options: 'antialias:' + mode
        });
        untiled.mergeNewParams({
            format_options: 'antialias:' + mode
        });
    }

    function setPalette(mode) {
        if (mode == '') {
            tiled.mergeNewParams({
                palette: null
            });
            untiled.mergeNewParams({
                palette: null
            });
        } else {
            tiled.mergeNewParams({
                palette: mode
            });
            untiled.mergeNewParams({
                palette: mode
            });
        }
    }

    function setWidth(size) {
        var mapDiv = document.getElementById('map');
        var wrapper = document.getElementById('wrapper');

        if (size == "auto") {
            // reset back to the default value
            mapDiv.style.width = null;
            wrapper.style.width = null;
        } else {
            mapDiv.style.width = size + "px";
            wrapper.style.width = size + "px";
        }
        // notify OL that we changed the size of the map div
        map.updateSize();
    }

    function setHeight(size) {
        var mapDiv = document.getElementById('map');

        if (size == "auto") {
            // reset back to the default value
            mapDiv.style.height = null;
        } else {
            mapDiv.style.height = size + "px";
        }
        // notify OL that we changed the size of the map div
        map.updateSize();
    }

    function updateFilter() {

        if (pureCoverage)
            return;

        var filterType = "cql";//document.getElementById('filterType').value;
        var filter = url_string;

        // by default, reset all filters                
        var filterParams = {
            filter: null,
            cql_filter: null,
            featureId: null
        };
        if (OpenLayers.String.trim(filter) != "") {
            if (filterType == "cql")
                filterParams["cql_filter"] = filter;
            if (filterType == "ogc")
                filterParams["filter"] = filter;
            if (filterType == "fid")
                filterParams["featureId"] = filter;
        }
        // merge the new filter definitions

        mergeNewParams(filterParams);
        map.getLayersByName('Monitoring Sites')[0].setVisibility(true);
    }


    function resetFilter() {
        if (pureCoverage)
            return;

        document.getElementById('filter').value = "";
        updateFilter();
    }

    function mergeNewParams(params) {
        tiled.mergeNewParams(params);
        untiled.mergeNewParams(params);
    }

    function seek_query() {

        var num = 0;
        url_string = '';
        var check_ln = document.getElementsByName('type').length;
        // High Agency
        if (document.getElementById('High_Agency').value != 'all') {
            url_string = url_string + "agency_type='" + document.getElementById('High_Agency').value + "'";
        }


        // Agency
        if (document.getElementById('Agency').value == 'all') {
            // don't include agency_organization
        } else {
            url_string = url_string + " and agency_organization='" + document.getElementById('Agency').value + "'";
            url_string = url_string.replace("Tippecanoe County Surveyor's office", "Tippecanoe County Surveyor''s office");
        }

        //dataset
        if (document.getElementById('dataset').value == 'all') {
            // don't include name
        } else {
            url_string = url_string + " and name='" + document.getElementById('dataset').value + "'";
        }

        //location
        if (document.getElementById('loc').value == '') {
            // don't include description
        } else {
            url_string = url_string + " and description LIKE '%" + document.getElementById('loc').value + "%'";
        }

        //huc

        var huc_ln = document.getElementsByName('huc').length;
        //alert(huc_ln);
        for (i = 0; i < huc_ln; i++) {
            if (document.getElementsByName('huc')[i].checked == true && document.getElementById('huc_code').value != '') {
                url_string = url_string + " and " + document.getElementsByName('huc')[i].value + "='" + document.getElementById('huc_code').value + "'";
            }
        }


        //parameter type
        if (document.getElementsByName('type')[0].checked == true) {
            partype_filter = "";
            // don't include parameter type
        } else {
            partype_filter = "";
            for (i = 0; i < check_ln; i++) {
                if (document.getElementsByName('type')[i].checked == true) {

                    if (num == 0) {
                        url_string = url_string + " and (parameter_type LIKE '%" + document.getElementsByName('type')[i].value + "%'";
                        partype_filter = partype_filter + "<ogc:Or><ogc:PropertyIsLike wildCard='*' singleChar='.' escape='!'><ogc:PropertyName>parameter_type</ogc:PropertyName><ogc:Literal>%" + document.getElementsByName('type')[i].value + "%</ogc:Literal></ogc:PropertyIsLike>";
                    } else {
                        url_string = url_string + " or parameter_type LIKE '%" + document.getElementsByName('type')[i].value + "%'";
                        partype_filter = partype_filter + "<ogc:PropertyIsLike wildCard='*' singleChar='.' escape='!'><ogc:PropertyName>parameter_type</ogc:PropertyName><ogc:Literal>%" + document.getElementsByName('type')[i].value + "%</ogc:Literal></ogc:PropertyIsLike>";
                    }
                    num++;
                }
            }
            if (num > 0) {
                partype_filter = partype_filter + "</ogc:Or>";
            }

            url_string = url_string + ")";
        }
        if (url_string.substr(1, 3) == 'and') {
            url_string = url_string.substr(5);
        }

        if (url_string == "") {
            updateFilter();
        } else {

            updateFilter(url_string);
        }

    }

    function agency_select() {
        $.getJSON( "agency/"+escape(document.getElementById('High_Agency').value)+"/all/", function( data ) {
            $("#Agency").empty()
            $.each( data["all_agencies"], function( key, val ) {
                var option = '<option value="'+val+'">'+val+'</option>'
                $(option).appendTo($("#Agency"))
            });
            $("#dataset").empty()
            $.each( data["all_datasets"], function( key, val ) {
                var option = '<option value="'+val+'">'+val+'</option>'
                $(option).appendTo($("#dataset"))
            });
        });
    }

    function org_select() {
        $.getJSON( "agency/"+escape(document.getElementById('High_Agency').value)+"/"+escape(document.getElementById('Agency').value)+"/", function( data ) {
            $("#dataset").empty()
            $.each( data["all_datasets"], function( key, val ) {
                var option = '<option value="'+val+'">'+val+'</option>'
                $(option).appendTo($("#dataset"))
            });
        });
    }


    function viewall() {
        var lat = 39.7690048218;
        var lon = -86.157333374;
        var zoom = 7;
        var lonLat = new OpenLayers.LonLat(lon, lat).transform(new OpenLayers.Projection("EPSG:4326"), map.getProjectionObject());
        map.setCenter(lonLat, zoom);
    }

    function showAddress(address) {
        $.getJSON( "http://maps.googleapis.com/maps/api/geocode/json?address="+address+"&sensor=false", function( data ) {
            
                var lat = data['results'][0]['geometry']['location']['lat']
                var lon = data['results'][0]['geometry']['location']['lng']
                var zoom = 11;
                var lonLat = new OpenLayers.LonLat(lon, lat).transform(new OpenLayers.Projection("EPSG:4326"), map.getProjectionObject());
                map.setCenter(lonLat, zoom);
        });
    }

    var huc_layer = new OpenLayers.Layer.WMS(
        "huc", "http://watersgeo.epa.gov/ArcGIS/services/OW/WBD_WMERC/MapServer/WMSServer", {
            projection: new OpenLayers.Projection("EPSG:3857"),
            layers: '0,1,2,3,4,5',
            styles: '',
            srs: 'EPSG:3857',
            transparent: 'true'
        }, {
            singleTile: true,
            ratio: 1
        }
    );




    var stream_layer = new OpenLayers.Layer.WMS(
        "stream", "http://watersgeo.epa.gov/ArcGIS/services/OW/NHD_Med_Basic_WMERC/MapServer/WMSServer", {
            projection: new OpenLayers.Projection("EPSG:3857"),
            layers: '0,1,2,3,4,5,6',
            styles: '',
            srs: 'EPSG:3857',
            transparent: 'true'
        }, {
            singleTile: true,
            ratio: 1
        }
    );

    function addHucWILayer() {
        map.addLayers([huc_layer]);

    }

    function removeHucWILayer() {
        map.removeLayer(huc_layer);
    }

    function addstreamsLayer() {
        map.addLayers([stream_layer]);
    }

    function removestreamsLayer() {
        map.removeLayer(stream_layer);
    }

    function switchHuc() {
        if (document.getElementById("hucWI").checked) {
            addHucWILayer();
        } else {
            removeHucWILayer();
        }
    }

    function switchstreams() {
        if (document.getElementById("stream").checked) {
            addstreamsLayer();
        } else {
            removestreamsLayer();
        }
    }

    function resize_map() {
        var dim = document.viewport.getDimensions(); // get the viewport dimensions
        map.div.setStyle({
            width: dim.width + 'px',
            height: dim.height + 'px'
        }); // change OpenLayers map *container* size
        document.documentElement.style.overflow = 'hidden';
        document.body.scroll = "no";
        map.size.width = dim.width;
        map.size.height = dim.height; // adjust the map's size
        map.updateSize(); // tell the map to adjust itself
        document.getElementById('overlay').style.visibility = 'hidden';

    }

    function orig_sze_map() {

        var dim = document.viewport.getDimensions(); // get the viewport dimensions
        map.div.setStyle({
            width: '550px',
            height: '680px'
        }); // change OpenLayers map *container* size
        document.documentElement.style.overflow = 'visible';
        document.body.scroll = "yes";
        map.size.width = '550px';
        map.size.height = '680px'; // adjust the map's size
        map.updateSize(); // tell the map to adjust itself
        document.getElementById('overlay').style.visibility = 'visible';

    }

    function dn_query() {
        var Agency_name = document.getElementById('Agency').value;
        Agency_name = Agency_name.replace("&", "&amp;");
        var Dataset_name = document.getElementById('dataset').value;
        Dataset_name = Dataset_name.replace("&", "&amp;");
        var huc_ln = document.getElementsByName('huc').length;
        var huc_type = '';
        var huc_number = '';
        for (i = 0; i < huc_ln; i++) {
            if (document.getElementsByName('huc')[i].checked == true && document.getElementById('huc_code').value != '') {
                huc_type = document.getElementsByName('huc')[i].value;
                huc_number = document.getElementById('huc_code').value;
            }
        }
        if (huc_type == '' && huc_number == '') {
            var dl_url = server_url+"/wfs?service=wfs&version=1.1.0&request=GetFeature&typeName=inwater:inwater&outputFormat=csv&propertyName=agency_type,agency_organization,name,description,site_no,parameter,parameter_type,frequency,publicly_available,quality,start_date,end_date,contact_url,huc_8,huc_10,huc_12,clipped_geom&Filter=" + escape("<ogc:Filter xmlns:gml='http://www.opengis.net/gml' xmlns:ogc='http://www.opengis.net/ogc'><ogc:And><ogc:And><ogc:PropertyIsEqualTo><ogc:PropertyName>agency_type</ogc:PropertyName><ogc:Literal>" + document.getElementById('High_Agency').value + "</ogc:Literal></ogc:PropertyIsEqualTo><ogc:PropertyIsEqualTo><ogc:PropertyName>agency_organization</ogc:PropertyName><ogc:Literal>" + Agency_name + "</ogc:Literal></ogc:PropertyIsEqualTo><ogc:PropertyIsEqualTo><ogc:PropertyName>name</ogc:PropertyName><ogc:Literal>" + Dataset_name + "</ogc:Literal></ogc:PropertyIsEqualTo><ogc:PropertyIsLike wildCard='*' singleChar='.' escape='!'><ogc:PropertyName>description</ogc:PropertyName><ogc:Literal>*" + document.getElementById('loc').value + "*</ogc:Literal></ogc:PropertyIsLike></ogc:And>" + partype_filter + "</ogc:And></ogc:Filter>");
        } else {
            var dl_url = server_url+"/wfs?service=wfs&version=1.1.0&request=GetFeature&typeName=inwater:inwater&outputFormat=csv&propertyName=agency_type,agency_organization,name,description,site_no,parameter,parameter_type,frequency,publicly_available,quality,start_date,end_date,contact_url,huc_8,huc_10,huc_12,clipped_geom&Filter=" + escape("<ogc:Filter xmlns:gml='http://www.opengis.net/gml' xmlns:ogc='http://www.opengis.net/ogc'><ogc:And><ogc:And><ogc:PropertyIsEqualTo><ogc:PropertyName>agency_type</ogc:PropertyName><ogc:Literal>" + document.getElementById('High_Agency').value + "</ogc:Literal></ogc:PropertyIsEqualTo><ogc:PropertyIsEqualTo><ogc:PropertyName>agency_organization</ogc:PropertyName><ogc:Literal>" + Agency_name + "</ogc:Literal></ogc:PropertyIsEqualTo><ogc:PropertyIsEqualTo><ogc:PropertyName>name</ogc:PropertyName><ogc:Literal>" + Dataset_name + "</ogc:Literal></ogc:PropertyIsEqualTo><ogc:PropertyIsEqualTo><ogc:PropertyName>" + huc_type + "</ogc:PropertyName><ogc:Literal>" + huc_number + "</ogc:Literal></ogc:PropertyIsEqualTo><ogc:PropertyIsLike wildCard='*' singleChar='.' escape='!'><ogc:PropertyName>description</ogc:PropertyName><ogc:Literal>*" + document.getElementById('loc').value + "*</ogc:Literal></ogc:PropertyIsLike></ogc:And>" + partype_filter + "</ogc:And></ogc:Filter>");
        }
        dl_url = dl_url.replace(escape("<ogc:PropertyIsEqualTo><ogc:PropertyName>agency_type</ogc:PropertyName><ogc:Literal>all</ogc:Literal></ogc:PropertyIsEqualTo>"), escape(""));
        dl_url = dl_url.replace(escape("<ogc:PropertyIsEqualTo><ogc:PropertyName>agency_organization</ogc:PropertyName><ogc:Literal>all</ogc:Literal></ogc:PropertyIsEqualTo>"), escape(""));
        dl_url = dl_url.replace(escape("<ogc:PropertyIsEqualTo><ogc:PropertyName>name</ogc:PropertyName><ogc:Literal>all</ogc:Literal></ogc:PropertyIsEqualTo>"), escape(""));
        dl_url = dl_url.replace(escape("<ogc:PropertyIsEqualTo><ogc:PropertyName>parameter_type</ogc:PropertyName><ogc:Literal>all</ogc:Literal></ogc:PropertyIsEqualTo>"), escape(""));

        //alert(document.getElementById('High_Agency').value);
        //alert(Agency_name);
        //alert(Dataset_name);
        //alert(huc_type);
        //alert(huc_number);
        //alert(document.getElementById('loc').value);
        //alert(partype_filter);

        //alert(dl_url);
        window.open(dl_url);

    }

    function downloadall() {
        var dl_url = server_url+"/wfs?request=GetFeature&version=1.1.0&typeName=inwater:inwater&outputFormat=csv";
        window.open(dl_url);
    }

    function uck_all() {
        if (document.getElementById("cAll").checked) {
            document.getElementById("cAll").checked = false;
        }

    }

    function uck_par() {

        document.getElementById("Aqu").checked = false;
        document.getElementById("Bac").checked = false;
        document.getElementById("Fis").checked = false;
        document.getElementById("Flo").checked = false;
        document.getElementById("Gen").checked = false;
        document.getElementById("Gro1").checked = false;
        document.getElementById("Gro2").checked = false;
        document.getElementById("Hab").checked = false;
        document.getElementById("Lak").checked = false;
        document.getElementById("Mac").checked = false;
        document.getElementById("Met").checked = false;
        document.getElementById("Nut").checked = false;
        document.getElementById("Org").checked = false;
        document.getElementById("Rad").checked = false;
        document.getElementById("Hoo").checked = false;
    }