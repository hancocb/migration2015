/*
 *  This is a collection of functions that are fairly simple and straightfoward in use
 *
 *  Timer() comes from an earlier version of L-Thia
 *
 *  All other functions were written by Karl Theller
 *
 *
 */
  

var hour = "0"
var min = "00"
var sec = "0"

function Timer(counter_id){
    var counter = document.getElementById(counter_id);
    if ((min < 10) && (min != "00")){
        dismin = "0" + min
    }
    else{
        dismin = min
    }

    dissec = (sec < 10) ? sec = "0" + sec : sec
    counter.value = hour + ":" + dismin + ":" + dissec

    if (sec < 59){
        sec++
    }
    else{
        sec = "0"
        min++
        if (min > 59){
            min = "00"
            hour++
        }
    }

    window.setTimeout("Timer('"+counter_id+"')",1000)
}

function resetTimer(counter_id){
    var counter = document.getElementById(counter_id);
    hour = "0";
    min = "00";
    sec = "0";
    counter.value = hour + ":" + min + ":" + sec + '0'
}

function findInputs(e){
    if(!e || !e.tagName){return [];}
    var a = [];
    if(e.tagName.toLowerCase() == "input" && ((e.type.toLowerCase() != "radio" && e.type.toLowerCase() != "checkbox") || e.checked)){// && (e.type.toLowerCase() == "hidden" || e.type.toLowerCase() == "text")){
        a.push(e.name + "=" + e.value);//encodeURIComponent(trim(e.value)));
    }
    if(e.tagName.toLowerCase() == "select" || e.tagName.toLowerCase() == "textarea"){
        a.push(e.name + "=" + e.value);//encodeURIComponent(trim(e.value)));
    }
    for ( var count = 0; count < e.childNodes.length; count++ )
    {
        var child = e.childNodes[count]
        a = a.concat(findInputs(child));
    }
    return a;
}

function urlFromForm(formid){
    var form = document.getElementById(formid);
    var url = form.action + '?';
    url += findInputs(form).join("&");
    return url;
}

function dataFromForm(formid){
    var form = document.getElementById(formid);
    var url = '?';
    url += findInputs(form).join("&");
    return url;
}
/*
function callScript( uri, func ){
    if(uri.substring(0,4) != "http"){
        uri = 'http://lthia.agriculture.purdue.edu/cgi-bin/' + uri
    }
    
    var req = new XMLHttpRequest();
    var question = uri.indexOf("?");
    var params = '';
    
    if(question >-1){
        req.open("POST",uri.substring(0,question));
        params = uri.substring(question+1, uri.length);
    } else {
        req.open("POST",uri);
    }
    
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    req.setRequestHeader("Content-length", params.length);
    req.setRequestHeader("Connection", "close");
    
    req.onreadystatechange = function() {
        // in case of network errors this might not give reliable results
        if(this.readyState == 4){
            if(func){
                func(req.responseText);
            }
        }
     }
    req.send(params);
}
*/

function callScript( uri, func ){
    if(uri.substring(0,4) != "http"){
        uri = 'http://lthia.agriculture.purdue.edu/cgi-bin/' + uri
    }
    
    var req = new XMLHttpRequest();
    req.open("GET",uri);
    req.onreadystatechange = function() {
        // in case of network errors this might not give reliable results
        if(this.readyState == 4){
            if(func){
                func();
            }
        }
     }
    req.send(null);
}

/*
function setHTML( container, uri, func ){
    if(uri.substring(0,4) != "http"){
        uri = 'http://lthia.agriculture.purdue.edu/cgi-bin/' + uri
    }
    
    var req = new XMLHttpRequest();
    var question = uri.indexOf("?");
    var params = '';
    
    if(question >-1){
        req.open("POST",uri.substring(0,question));
        params = uri.substring(question+1, uri.length);
    } else {
        req.open("POST",uri);
    }
    
    req.onreadystatechange = function() {
        // in case of network errors this might not give reliable results
        if(this.readyState == 4){
            document.getElementById(container).innerHTML = req.responseText;
            if(func){
                func();
            }
        }
     }
    req.send(params);
}
*/

function setHTML( container, uri, func ){
    if(uri.substring(0,4) != "http"){
        uri = 'http://lthia.agriculture.purdue.edu/cgi-bin/' + uri
    }
    
    var req = new XMLHttpRequest();
    req.open("GET",uri);
    req.onreadystatechange = function() {
        // in case of network errors this might not give reliable results
        if(this.readyState == 4){
            var domobj = document.getElementById(container);
            domobj.innerHTML = req.responseText;
            if(func){
                func();
            }
        }
     }
    req.send(null);
}

function downloadURL( uri, func ){
    if(uri.substring(0,4) != "http"){
        uri = 'http://lthia.agriculture.purdue.edu/cgi-bin/' + uri
    }
    
    var req = new XMLHttpRequest();
    req.open("GET",uri);
    req.onreadystatechange = function() {
        // in case of network errors this might not give reliable results
        if(this.readyState == 4){
            if(func){
                func(req.responseText,  req.status);
            }
        }
     }
    req.send(null);
}


/* left over from using iframes 
* 
function setSrc( control, uri ){
    openControl(control);
    
    if(uri.substring(0,4) != "http"){
        uri = 'http://lthia.agriculture.purdue.edu/cgi-bin/' + uri
    }
    
    var frame = document.getElementById(control + "Frame");
    frame.src = uri;
}*/

function clearText(control){
    var text = document.getElementById(control + "Text");
    text.innerHTML = '';
}

function trim(s) {
    return s.replace( /^\s*/, "" ).replace( /\s*$/, "" );
}

function getIEVer()
// Returns the version of Internet Explorer or a -1
// (indicating the use of another browser).
{
    var rv = -1; // Return value assumes failure.
    if (navigator.appName == 'Microsoft Internet Explorer')
    {
        var ua = navigator.userAgent;
        var re  = new RegExp("MSIE ([0-9]{1,}[\.0-9]{0,})");
        if (re.exec(ua) != null)
            rv = parseFloat( RegExp.$1 );
    }
    return rv;
}