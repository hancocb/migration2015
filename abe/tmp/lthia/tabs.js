//a single simple yet very important function that is required for the tabs to work
//adjusts the parent's (div's) class to change the current tab
tb_recursable = ['div', 'span', 'form', 'ul'];

function addClass(element, classname){
    if(element.className.toLowerCase().indexOf(classname)==-1){
        element.className = element.className + " " + classname;
    }
}

function addOrReplaceClass(element, oldClsName, newClsName){
    if(containsClass(element, oldClsName)){
        element.className = element.className.toLowerCase().replace(oldClsName, newClsName);
    } else {
        addClass(element, newClsName);
    }
}

function removeClass(element, classname){
    var x = element.className.toLowerCase().indexOf(classname);
    if(x != -1){
        element.className = element.className.replace(element.className.substring(x, x+classname.length), "");
    }
}

function containsClass(element, classname){
    var cn = element.className.toLowerCase()
    var i = cn.indexOf(classname);
    while(i != -1){
    //if(i != -1){
        var prev;
        if(i==0){
            prev = '';
        } else {
            prev = cn.substring(i - 1, i)
        }
        if(prev == '' || prev == ' '){
            var j = 0;
            var after = cn.substring(i + classname.length, i + classname.length +1);
            while (after != "" && after !=" "){
                j++;
                after = cn.substring(i + classname.length + j, i + classname.length + j + 1);
            }
            return cn.substring(i, i + classname.length + j);
        }
        cn =cn.substring(i + classname.length)
        i = cn.indexOf(classname);
    }
    return false;
}

function containsClassExact(element, classname){
    var cn = element.className.toLowerCase()
    var i = cn.indexOf(classname);
    while(i != -1){
    //if(i != -1){
        var prev;
        if(i==0){
            prev = '';
        } else {
            prev = cn.substring(i - 1, i)
        }
        var after = cn.substring(i + classname.length, i + classname.length +1);
        if((after == "" || after ==" ") && (prev == '' || prev == ' ')){
            return true;
        }
        cn =cn.substring(i + classname.length)
        i = cn.indexOf(classname);
    }
    return false;
}

function getClassLoc(element, classname){
    var cn = element.className.toLowerCase()
    var i = cn.indexOf(classname);
    var x = i;
    while(i != -1){
        var prev;
        if(i==0){
            prev = '';
        } else {
            prev = cn.substring(i - 1, i)
        }
        if(prev == '' || prev == ' '){
            return x;
        }
        cn =cn.substring(i + classname.length)
        i = cn.indexOf(classname);
        x += i;
    }
    return -1;
}

function getClassExtension(element, classname){
    // var cn = element.className.toLowerCase()
    // var x = cn.indexOf(classname);
    // if(x==-1){return "";}
        
    // var i = 0;
    // var after = cn.substring(x + classname.length, x + classname.length +1);
    // while (after != "" && after !=" "){
        // i++;
        // after = cn.substring(x + classname.length + i, x + classname.length + i + 1);
    // }
    return containsClass(element, classname).substring(classname.length);
}

function getClassWithExtension(element, classname){
    // var cn = element.className.toLowerCase()
    // var x = cn.indexOf(classname);
    // if(x==-1){return "";}
        
    // var i = 0;
    // var after = cn.substring(x + classname.length, x + classname.length +1);
    // while (after != "" && after !=" "){
        // i++;
        // after = cn.substring(x + classname.length + i, x + classname.length + i + 1);
    // }
    return containsClass(element, classname);
}

function changetab(newtab, parentid)
{
    var supertab = document.getElementById(parentid);
    
    if(supertab.className.indexOf("distab" + newtab) != -1){
        return;
    }
 
    var x = supertab.className.indexOf("utab");
    if(x == -1){
        supertab.className = supertab.className + " utab"+newtab;
    } else {
        var y = getClassWithExtension(supertab, 'utab');
        addOrReplaceClass(supertab, y, 'utab' + newtab);
        //supertab.className = supertab.className.replace(supertab.className.substring(x, x+5), "utab"+newtab);
    }
    
    propagate(supertab, -1);
}

function disabletabOld(tabnum, parentid){
    var supertab = document.getElementById(parentid);
    
    addClass(supertab, "distab" + tabnum);
}

function disabletabsub(div, tabnum){
    if(!div){return;}
    
    for ( var count = 0; count < div.childNodes.length; count++ )
    {
        var child = div.childNodes[count]
        if(!child || !child.tagName){continue;}
        if (child.tagName.toLowerCase() == "li" &&
                child.className.indexOf("tab" + tabnum) != -1)
        {
                addClass(child, " distb");
            
        }
        else if(tb_recursable.indexOf(child.tagName.toLowerCase()) !=-1 && child.className.indexOf("tab") == -1)/* == "div" || 
                child.tagName.toLowerCase() == "span" || 
                child.tagName.toLowerCase() == "form" || 
                child.tagName.toLowerCase() == "ul")*/
        {
            disabletabsub(child, tabnum);
        }
    }
}

function disabletab(elementId, tabnum){
    var e = document.getElementById(elementId);
    addClass(e, "distab" + tabnum);
    disabletabsub(e, tabnum);
}

function enabletabsub(div, tabnum){
    if(!div){return;}
    
    for ( var count = 0; count < div.childNodes.length; count++ )
    {
        var child = div.childNodes[count]
        if(!child || !child.tagName){continue;}
        if (child.tagName.toLowerCase() == "li" &&
                child.className.indexOf("tab" + tabnum) != -1)
        {
                removeClass(child, " distb");
            
        }
        else if(tb_recursable.indexOf(child.tagName.toLowerCase()) !=-1 && child.className.indexOf("tab") == -1)/* == "div" || 
                child.tagName.toLowerCase() == "span" || 
                child.tagName.toLowerCase() == "form" || 
                child.tagName.toLowerCase() == "ul")*/
        {
            enabletabsub(child, tabnum);
        }
    }
}

function enabletab(tabnum, parentid){
    var supertab = document.getElementById(parentid);
    removeClass(supertab, "distab" + tabnum);
    enabletabsub(supertab, tabnum);
}

// Deprecated version of the propagate function
//recurse over sub divs and set visibility as needed
function propagate2(div, subvis){
    var n = div.className.toLowerCase().indexOf("utab");
    var divnum = -1;
    if(n != -1){
        divnum = div.className.toLowerCase().substring(n + 4, n + 5);
    }
    for ( var count = 0; count < div.childNodes.length; count++ )
    {
        var child = div.childNodes[count]
        if(!child || !child.tagName){continue;}
        if(child.tagName.toLowerCase() == "div" || child.tagName.toLowerCase() == "span" || child.tagName.toLowerCase() == "form"){
            if(!divnum){propagate(child, subvis);}
            var i = child.className.toLowerCase().indexOf("utab");
            var j = child.className.toLowerCase().indexOf("tab");
            if(n != -1){//parent is a utab
                if(j!=-1){//child is a tab
                    var chldnum = child.className.toLowerCase().substring(j + 3, j + 4);
                    if(chldnum == divnum && (div.style.display=="inline" || div.style.display=="") && subvis){
                        child.style.visibilty = "visible";
                        child.style.display = "inline";
                        propagate(child, true);
                    } else {
                        child.style.visibilty = "hidden";
                        child.style.display = "none";
                        propagate(child, false);
                    }
                 
                    
                } else {
                    propagate(child, subvis);
                }
            } else {
                propagate(child, subvis);
            }
            
        }
    }
}

//recurse over sub divs and set visibility as needed
// this version should work more cleanly and not require
// that child tabs be direct descendents of the utab
function propagate(div, tabnum ){
    if( ! div.style.displayx){
        if( div.style.display != "none"){
            div.style.displayx = div.style.display;
        } else {
            div.style.displayx = "inline";
        }
    }
    var m = div.className.toLowerCase().indexOf("tab");
    var n = div.className.toLowerCase().indexOf("utab");
    var o = div.className.toLowerCase().indexOf("distab");
    if(n != -1){
        tabnum = getClassExtension(div, "utab");//div.className.toLowerCase().substring(n + 4, n + 5);
        var str = div.className.toLowerCase();
        while( (n!=-1 && m == n+1) || (o!=-1 && m == o + 3)){
            if(m == n+1){
                str = str.substring(n + 5);
                m = str.indexOf("tab");
                n = str.indexOf("utab");
                o = str.indexOf("distab");
            } else {
                str = str.substring(o + 7);
                m = str.indexOf("tab");
                n = str.indexOf("utab");
                o = str.indexOf("distab");
            }
        }
    }
    
    if(m==-1){
        divnum = -1;
    }else{
        divnum = getClassExtension(div, 'tab');
        // divnum = div.className.toLowerCase().substring(m + 3, m + 4);
    }
    
    if(tabnum == -10 || (m != -1 && tabnum != divnum)){
        div.style.visibilty = "hidden";
        div.style.display = "none";
        addOrReplaceClass(div, "ontb", "offtb");
        tabnum = -10;
    } else {
        div.style.visibilty = "visible";
        div.style.display = div.style.displayx;
        addOrReplaceClass(div, "offtb", "ontb");
    }

    for ( var count = 0; count < div.childNodes.length; count++ )
    {
        var child = div.childNodes[count]
        if(!child || !child.tagName){continue;}
        if(tb_recursable.indexOf(child.tagName.toLowerCase()) != -1){// == "div" || child.tagName.toLowerCase() == "span" || child.tagName.toLowerCase() == "form"){
            propagate(child, tabnum);
        }
        else if(child.tagName.toLowerCase() == 'li'){
            var i = getClassLoc(child, "tab"+tabnum);
            var j = child.className.toLowerCase().indexOf("distb");
            if(j!=-1){continue;}
            if(containsClassExact(child, "tab"+tabnum)){
                addOrReplaceClass(child, "offtb", 'ontb');
            } else {
                addOrReplaceClass(child, "ontb", 'offtb');
            }
        }
    }
}