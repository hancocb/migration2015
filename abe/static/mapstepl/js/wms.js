/* 
    Document   : wms.js
    Created on : May 10, 2013
    Author     : Karl Theller

    Defines common functions for use with WMS services
*/

function latlngToContainerPixel(map, latlng){
    var mapsize=map.getDiv();
    var bounds = map.getBounds();
    var SW = bounds.getSouthWest();
    var NE = bounds.getNorthEast();
    var wid = Math.abs(NE.lng() - SW.lng());
    var hid = Math.abs(NE.lat() - SW.lat());
    var pixelCoordinate = new google.maps.Point(Math.floor(((latlng.lng() - SW.lng()) / wid ) * mapsize.offsetWidth), Math.floor(((NE.lat() - latlng.lat()) / hid ) * mapsize.offsetHeight));
    
    return pixelCoordinate;
}

function fromPixelToLatLng(map, pixel){
    var mapsize=map.getDiv();
    var bounds = map.getBounds();
    var SW = bounds.getSouthWest();
    var NE = bounds.getNorthEast();
    var wid = Math.abs(NE.lng() - SW.lng());
    var hid = Math.abs(NE.lat() - SW.lat());
    var pixelCoordinate = new google.maps.LatLng((pixel.x / mapsize.offsetWidth) * wid + SW.lng(), NE.lat() - (pixel.y / mapsize.offsetHeight * hid));
    alert("(" + (pixel.x / mapsize.offsetWidth) * wid + "," + ((pixel.y / mapsize.offsetHeight) * hid) + ')');
    return pixelCoordinate;
}

function fromPointToLatLng(map, pixel){
    var mapsize=map.getDiv();
    var bounds = map.getBounds();
    var SW = bounds.getSouthWest();
    var NE = bounds.getNorthEast();
    var wid = Math.abs(NE.lng() - SW.lng());
    var hid = Math.abs(NE.lat() - SW.lat());
    var pixelCoordinate = new google.maps.LatLng((pixel.x / mapsize.offsetWidth) * wid + SW.lng(), NE.lat() - (pixel.y / mapsize.offsetHeight * hid));
    alert("(" + (pixel.x / mapsize.offsetWidth) * wid + "," + ((pixel.y / mapsize.offsetHeight) * hid) + ')');
    return pixelCoordinate;
} 

function loadWMS(baseUrl, layers, customArgs){
    var layerOpts = {
        getTileUrl: function(coord, zoom) {
            return WMSGetTileUrl( coord, zoom, baseUrl, layers ) + customArgs;
            //alert(coord.x + ',' + coord.y);
            //return baseUrl + "layers=" + layers +
            //"&zoom=" + zoom + "&x=" + coord.x + "&y=" + coord.y + "&format=image/png&SRS=EPSG:4326" + customArgs;
        },
        tileSize: new google.maps.Size(256, 256),
        isPng: true,
        opacity: 0.7
    };
    return new google.maps.ImageMapType(layerOpts);
}

function WMSCreateMap( mName, mBaseUrl, layer, minResolution,maxResolution, urlArg ) { 
    var wmsOptions = {
        alt: mName,
        getTileUrl: function (tile, zoom){return WMSGetTileUrl(tile, zoom, mBaseUrl, layer);},
        isPng: false,
        maxZoom: 17,
        minZoom: 6,
        name: mName,
        tileSize: new google.maps.Size(256, 256),
        credit: 'Image Credit: CT State Library, MAGIC'
    };
    return new google.maps.ImageMapType(wmsOptions);
}

function WMSGetTileUrl( tile, zoom, baseUrl, layer ) {
    var zpow = Math.pow(2, zoom);
    var southWestPixel = new google.maps.Point( tile.x * 256 / zpow, ( tile.y + 1 ) * 256 / zpow);
    var northEastPixel = new google.maps.Point( ( tile.x + 1 ) * 256 / zpow, tile.y * 256 / zpow);
    //alert(northEastPixel.x + ',' + northEastPixel.y);
    var southWestCoords = map.getProjection().fromPointToLatLng(southWestPixel);//google.maps.OverlayView().getProjection().fromContainerPixelToLatLng(southWestPixel);
    var northEastCoords = map.getProjection().fromPointToLatLng(northEastPixel);
    var bbox = southWestCoords.lng() + ',' + southWestCoords.lat() + ',' + northEastCoords.lng() + ',' + northEastCoords.lat();
    return baseUrl + '?VERSION=1.1.1&REQUEST=GetMap&LAYERS=' + layer + '&STYLES=&SRS=EPSG:4326&BBOX=' + bbox +
    '&WIDTH=256&HEIGHT=256&FORMAT=image/png&BGCOLOR=0xFFFFFF&TRANSPARENT=TRUE&EXCEPTIONS=INIMAGE';
}