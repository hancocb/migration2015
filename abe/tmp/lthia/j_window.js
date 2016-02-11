/*

The original moveMapControl, stopMoveLayer, and hideDiv scripts were created by:
Institute of Water Research, Michigan State University


Those scripts were edited by:
Karl Theller, Purdue University

All other functions were created by:
Karl Theller, Purdue University

Slight improvements and adjustments were made to the original code
Several new functions were created, including one allowing the resizing of the controls
Comments were added for clarity

divs intended to be used as floating controls need to match certain specifications:

 */
 var ButtonPath = "/images/"; //the path the button images are located at
 var ExpandButton = "expand.png"; //name of the expand button
 var RestoreButton = "restore.png";
 var ContractButton = "contract.png";
 var MinimizeButton = "minimize.png";
 var MaximizeButton = "maximize.png";
 var MinimizeToTop = true;
 var MinimizeLeftMargin = 80;
 var currenttop = 10001;
 var maxIndex = 9999999;

//Global Variables
var MoveLayer = false; //Is a control being moved?
var GetLayerOnce = false; //Is the user starting to drag a control (check for first time)
var ResizeLayer = false; //Is a control being resized?
var GetLayerResizeOnce = false; //Is the user starting to resize a control (check for first time)
var difx, dify; //used in moveMapControl, the difference between the mouse location and the upper left of the control
var difx2, dify2, difx3, dify3; //used int resizeMapControl, the difference between the mouse position and the upper left of the resize image

var movecontrol = null;
var borders = null;

//set the window's onresize event
window.onresize = adjustcontrols;
var resizeelement = 'map'; //an element to resize to the window
var remargins = 6; //margins around the above element

/* Allows a control to be dragged around the screen
     Activated by onmousedown or onmouseclick by the title bar

     takes the div that is moving (or another element type if desired)
        that moving element must have "position: absolute;" in its style
        or it will not move properly
*/

function moveMapControl(element, aBorders) {
    movecontrol = document.getElementById(element);
    borders = aBorders
    if(!movecontrol){
        return false;
    }
    
    GetLayerOnce = true;
    MoveLayer = true;

    var IE = document.all?true:false;
    
    /*if (!IE) {
        document.captureEvents(Event.MOUSEMOVE);
    }*/
    
    savecontrol(element);
    
    
    if (document.addEventListener) {
        document.addEventListener('mousemove', getMouseCoord, false);
        document.addEventListener('mouseup', stopMoveLayer, false);
    } else if (document.attachEvent)  {
        document.attachEvent('onmousemove', getMouseCoord);
        document.attachEvent('onmouseup', stopMoveLayer);//detach
    }
    
    var tempX = 0;
    var tempY = 0;
    
    function getMouseCoord(e) {
        if (IE) { // grab the x-y pos.s if browser is IE
            tempX = event.clientX + document.body.scrollLeft;
            tempY = event.clientY + document.body.scrollTop;
        } else {  // grab the x-y pos.s if browser is not IE
            tempX = e.pageX;
            tempY = e.pageY;
        }  

        //no negative mouse positions
        if (tempX < 0) {
            tempX = 0;
        }
        
        if (tempY < 0) {
            tempY = 0;
        }  

        //run once when the mouse is first pressed
        if (GetLayerOnce == true) {
            /*set a to the distance to the left side of the element, regardless
                of whether left or right was used to determine its original position
            */
            var right = movecontrol.style.right;
            right = (right.substring(0,right.length-2));
            var width = movecontrol.style.width;
            width = (width.substring(0,width.length-2));
            if(movecontrol.style.left == 0){ //check if the element is using left or right for position
                if(document.documentElement.clientWidth != 0){//some older browsers use body.offsetWidth instead of width
                    a = document.documentElement.clientWidth - right - width;
                } else {
                    a = window.innerWidth - right - width;
                }
            } else { //if left was used for position:
                a = movecontrol.style.left;
                a = (a.substring(0,a.length-2)); //as movecontrol.style.left is a string, we need to remove the px on the end
            }
            //set b to the elements vertical position
            b = movecontrol.style.top;
            difx = tempX - a; //get distance between tempX(mouse x) and control's left side
            dify = tempY - (b.substring(0,b.length-2)); //get distance between tempX(mouse x) and control's right side
            GetLayerOnce = false; //prevent this section from running a second time
        }

        if (MoveLayer == true) {
            //move the control, keeping the relative positions of the mouse and control the same
            movecontrol.style.left = (tempX-difx) +'px'; 
            movecontrol.style.top = (tempY-dify) +'px';
        }
        return;
    }
    
    function removeListeners(){
        if (document.removeEventListener) {
            document.removeEventListener('mousemove', getMouseCoord, false);
            document.removeEventListener('mouseup', stopMoveLayer, false);
        } else if (document.detachEvent)  {
            document.detachEvent('onmousemove', getMouseCoord);
            document.detachEvent('onmouseup', stopMoveLayer);//detach
        }
    }
    
    // When the user releases the mouse, prevent moving of the element
    function stopMoveLayer(e) {
        var tempX, tempY, x, y;
        if (IE) { // grab the x-y pos.s if browser is IE
            tempX = event.clientX + document.body.scrollLeft;
        } else {  // grab the x-y pos.s if browser is not IE
            tempX = e.pageX;
        }  
        if(document.documentElement.clientWidth != 0){//some older browsers use different widths
            x = document.documentElement.clientWidth;
        } else {
            x = window.innerWidth;
        }
        
        if(movecontrol != null && x - tempX < 17){
            maximizeControlHalf(element, true);
        } else if(movecontrol != null && tempX < 17) {
            maximizeControlHalf(element, false);
        }
        
        GetLayerOnce = false;
        MoveLayer = false;
        movecontrol = null;
        removeListeners();
    }
}



/*resizes a control panel - called by onmousedown from the expand icon
  takes:
    element - the outer div that will change size
    self - the resize image (as it initiates the function)
    bar - the title bar, as it must scale too
    text - the content div, as it must scale or the content will disappear/fall out of the control
*/
function resizeMapControl(control_id) {
    var movecontrol = document.getElementById(control_id);
    var thiscontrol = document.getElementById(control_id + 'ResizeControl');
    var barcontrol = document.getElementById(control_id + 'Bar');
    var textcontrol = document.getElementById(control_id + 'Text');
    var iframecontrol = document.getElementById(control_id + 'Frame');
    
    if(!movecontrol || !thiscontrol || !barcontrol || !textcontrol){
        return false;
    }
    
    GetLayerResizeOnce = true;
    ResizeLayer = true;

    var IE = document.all?true:false;
    
    if (!IE) { //check if IE
        document.captureEvents(Event.MOUSEMOVE);
    }
    
    document.onmousemove = getMouseCoordR; //call getMouseCoordR when the mouse moves
    document.onmouseup = stopResizeLayer; //call stopResizeLayer when the mouse button is released
    
    var tempX = 0; //the position of the mouse
    var tempY = 0;
    var a, b, c, d; //stores the controls left and top, and the resize image's left and top respectively
    
    function getMouseCoordR(e) {
        if (IE) { // grab the x-y pos.s if browser is IE
            tempX = event.clientX + document.body.scrollLeft;
            tempY = event.clientY + document.body.scrollTop;
        } else {  // grab the x-y pos.s if browser is NS
            tempX = e.pageX;
            tempY = e.pageY;
        }  

        //no negative mouse positions
        if (tempX < 0) {
            tempX = 0;
        }
        
        if (tempY < 0) {
            tempY = 0;
        }  
        
        //set a to the controls left position
        var right = movecontrol.style.right;
        right = (right.substring(0,right.length-2));
        var width = movecontrol.style.width;
        width = (width.substring(0,width.length-2));
        
        if (GetLayerResizeOnce == true) {
            if(movecontrol.style.left == 0){
                if(document.documentElement.clientWidth != 0){
                    a = document.documentElement.clientWidth - right - width;
                } else {
                    a = window.innerWidth - right - width;
                }
            } else {
                a = movecontrol.style.left;
                a = (a.substring(0,a.length-2));
            }
            //reset the left position to ensure a right side anchor doesn't interfere with resizing
            movecontrol.style.left = a + 'px';
            //set b to the controls vertical posistion
            b = movecontrol.style.top;
            b = (b.substring(0,b.length-2));
            
            // set c to the resize image's left position
            var right2 = thiscontrol.style.right;
            right2 = (right2.substring(0,right2.length-2));
            var width2 = thiscontrol.style.width;
            width2 = (width2.substring(0,width2.length-2));
            
            if(thiscontrol.style.left == 0){
                if(document.documentElement.clientWidth != 0){
                    c = document.documentElement.clientWidth - right2 - width2;
                } else {
                    c = window.innerWidth - right2 - width2;
                }
            } else {
                c = thiscontrol.style.left;
                c = (c.substring(0,c.length-2));
            }
            //set d to the resize image's vertical position
            d = thiscontrol.style.top;
            d = (d.substring(0,d.length-2));
        
            //get the distance between the mouse position and the left/top of the expand image
            difx2 = tempX - c;
            dify2 = tempY - d;
            GetLayerResizeOnce = false;//prevent resetting the difs
        }

        if (ResizeLayer == true) {
            //resize the control and associated elements
            if(tempX-a >= 200){ //prevent resizing to too small a size
                thiscontrol.style.left =(tempX-difx2) +'px'; //adjust resize image's position
                barcontrol.style.width =(tempX-6+20-difx2) +'px'; //resize title bar, control, and content div
                movecontrol.style.width =(tempX + 20 - difx2) +'px';
                textcontrol.style.width =(tempX-difx2 + 20 -8) +'px';
                if(iframecontrol != null){ //resize iframe if there is one
                    iframecontrol.style.width = (tempX-difx2 + 20 - 12) +'px';
                }
            } else {
                thiscontrol.style.left = 180 +'px'; //if mouse goes below min size, set to min size
                barcontrol.style.width = 196 +'px';
                movecontrol.style.width = 200 +'px';
                textcontrol.style.width = 192 +'px';
                if(iframecontrol){
                    iframecontrol.style.width = 188 +'px';
                }
            }
            if(tempY - b >= 150) {//prevent resizing to too small a size
                movecontrol.style.height = (tempY-dify2+20) +'px'; //resize control, and content div (title bar doesn't change height)
                textcontrol.style.height = (tempY-dify2+20 - 52) +'px';
                thiscontrol.style.top = (tempY-dify2) +'px';// move the resize image
                if(iframecontrol){ //resize the iframe if there is one
                    iframecontrol.style.height = (tempY-dify2+20 - 56) +'px';
                }
            } else {
                movecontrol.style.height = 150 +'px'; //if mouse goes below min size, set to min size
                textcontrol.style.height = 98 +'px';
                thiscontrol.style.top = 130 +'px';
                if(iframecontrol){
                    iframecontrol.style.height = 94 +'px';
                }
            }
        }
        return;
    }
}

//called when the user release the mouse button so resizing doesn't continue
function stopResizeLayer() {
    GetLayerResizeOnce = false;
    ResizeLayer = false;
}

/*Swaps the control between two states:
    normal: the contents of the control are shown normally
    contracted: the contents are hidden, and only the title bar is shown
 takes:
    div_id - the div that contains the contents that will be hidden; not the moving div itself
    bgcolor - can be '' - the color of the control's background in hex
*/
function hideDiv(control_id, bgcolor) {
    if(bgcolor == ''){
        bgcolor = '#FFFFFF';
    }
    var div, button, control, expand;
    control = document.getElementById(control_id);
    div = document.getElementById(control_id+'Text');
    button = document.getElementById(control_id+'DisplayButton');
    expand = document.getElementById(control_id + 'ResizeControl');
    if(!control || !div){
        return false;
    }
    if (div.style.display != "none") {
        div.style.display = "none"; //hide contents
        control.style.height = '24px'; //make the outer div smaller to avoid blocking things beneth it
        if(button){
            button.src = ButtonPath + ExpandButton; //change the expand/contract icon
        }
        div.style.backgroundColor = ""; //clear the outer div's background
        //control.style.borderStyle = "none"; //hide the outer div's border
        if(expand){
            expand.style.visibility = "hidden"; //hide the resize image
        }
    } else {
        div.style.display = "inline"; //show contents
        control.style.height = ((div.style.height.substring(0,div.style.height.length-2)) - (-52)) + 'px';
            //reset the outer div's size based on the inner div's size
        if(button){
            button.src = ButtonPath + ContractButton; //change the expand/contract icon
        }
        div.style.backgroundColor = bgcolor; //revert the outer div's background
        //control.style.borderStyle = "solid"; //show the outer div's border
        if(expand){
            expand.style.visibility = "visible"; //show the resize image
        }
    }
}

/*reduces the control to just its title bar - the contents are hidden
 takes:
    div_id - the div that contains the contents that will be hidden; not the moving div itself
*/
function contractControl(control_id) {
    var div, button, control, expand;
    control = document.getElementById(control_id);
    div = document.getElementById(control_id+'Text');
    button = document.getElementById(control_id+'DisplayButton');
    expand = document.getElementById(control_id + 'ResizeControl');
    
    if(!control || !div){
        return false;
    }
    
    div.style.display = "none"; //hide contents
    control.style.height = '24px'; //make the outer div smaller to avoid blocking things beneth it
    if(button){
        button.src = ButtonPath + ExpandButton; //change the expand/contract icon
    }
    div.style.backgroundColor = ""; //clear the outer div's background
    if(expand){
        expand.style.visibility = "hidden"; //hide the resize image
    }
    return true;
}

/*Shows the contents of a control if they have been hidden by hideDiv or contractControl
 takes:
    div_id - the div that contains the contents that will be hidden; not the moving div itself
    bgcolor - can be '' - the color of the control's background in hex
*/
function expandControl(control_id, bgcolor) {
    if(bgcolor==''){
        bgcolor = '#FFFFFF';
    }
    var div, button, control, expand;
    control = document.getElementById(control_id);
    div = document.getElementById(control_id+'Text');
    button = document.getElementById(control_id+'DisplayButton');
    expand = document.getElementById(control_id + 'ResizeControl');
    
    if(!control || !div){
        return false;
    }

    div.style.display = "inline"; //show contents
    control.style.height = ((div.style.height.substring(0,div.style.height.length-2)) - (-52)) + 'px';
        //reset the outer div's size based on the inner div's size
    if(button){
        button.src = ButtonPath + ContractButton; //change the expand/contract icon
    }
    div.style.backgroundColor = bgcolor; //revert the outer div's background
    if(expand){
        expand.style.visibility = "visible"; //show the resize image
    }
    return true;
}



var minimizerows = [];
var olddata = []; //used to store the original size/pos of controls that are minimized/maximized
var maxed = '';

//a utility function to determine an object is in an array
//checks for multidimensional arrays first
//returns the 1D index of the result or -1 on failure
function find(value, array) {
    for(var a = 0 ; a < array.length ; a++ ){
        if(array[a] instanceof Array){
            if(find(value, array[a]) != -1) {
                return a;
            }
        } else {
            if(array[a] == value){return a;}
        }
    }
    return -1;
}

//a utility function to determine if a control has data stored, and where
function finddata(name) {
    return find(name,olddata);
}

//another internal utility function to save space in minimize and maximize
function restorecontrol(control_id) {
    var temp = finddata(control_id);
    if(temp==-1){return false;}
    var control = document.getElementById(control_id);
    var bar = document.getElementById(control_id + 'Bar');
    var div = document.getElementById(control_id + 'Text');
    var iframe = document.getElementById(control_id + 'Frame');
    var minbut = document.getElementById(control_id + 'MinimizeButton');
    control.style.left = olddata[temp][1];
    control.style.top = olddata[temp][2];
    control.style.width = olddata[temp][3];
    control.style.height = olddata[temp][4];
    if(minbut.alt == "Restore Button"){
        control.style.zIndex = olddata[temp][5];
    }
    a = olddata[temp][3];
    a = parseInt(a.substring(0,a.length - 2));
    b = olddata[temp][4];
    b = parseInt(b.substring(0,b.length - 2));
    bar.style.width = (a - 6) + 'px';
    div.style.width = (a - 10) + 'px';
    div.style.height = (b - 52) + 'px';
    if(iframe){
        iframe.style.width = (a - 12) + 'px';
        iframe.style.height = (b - 56) + 'px';
    }
}

//another internal utility function to save space in minimize and maximize
function savecontrol(control_id) {
    var control = document.getElementById(control_id);
    var temp = finddata(control_id);
    var a;
    if(temp  == -1){
        a = olddata.length;
    } else {
        a = temp
    }
    olddata[a] = [control_id, control.style.left, control.style.top, control.style.width, control.style.height, control.style.zIndex];
}

//internal function to find the number of defined entries in an array
function getnonempty(array) {
    var count = 0;
    for(var a = 0 ; a < array.length ; a++) {
        if(array[a] != undefined){
            count++;
        }
    }
    return count;
}

//interal function to find the position of the first undefined entry in an array
//returns the array's length if none are found
function getfirstempty(array){
    for(var i = 0 ; i < array.length ; i++) {
        if(array[i] == undefined) {
            return i;
        }
    }
    return array.length;
}

//an internal function to be called by the window.onresize function
//resizes the maxed control to the new window size
//takes the event, but only cares about the maxed variable
function adjustmaxed() {
    var control = document.getElementById(maxed);
    var bar = document.getElementById(maxed + 'Bar');
    var div = document.getElementById(maxed+'Text');
    var iframe = document.getElementById(maxed+'Frame');
    
    var a, b;
    if(document.documentElement.clientWidth != 0){//some older browsers use body.offsetWidth instead of width
        a = document.documentElement.clientWidth;
    } else {
        a = window.innerWidth;
    }
    if(document.documentElement.clientHeight != 0){//some older browsers use body.offsetHeight instead of width
        b = document.documentElement.clientHeight;
    } else {
        b = window.innerHeight;
    }
    
    control.style.width = a + 'px';
    bar.style.width = (a - 6) + 'px';
    div.style.width = (a - 10) + 'px';
    control.style.height = b + 'px';
    div.style.height = (b - 32) + 'px';
    if(iframe){
        iframe.style.width = (a - 12) + 'px';
        iframe.style.height = (b - 36) + 'px';
    }
}

//an internal function to be bound to the window.onresize event
//takes the event, but only cares about the maxed variable
function adjustcontrols(event){
    if(maxed!=''){adjustmaxed();}
    
    var x, y;
    if(document.documentElement.clientWidth != 0){
        x = document.documentElement.clientWidth;
    } else {
        x = window.innerWidth;
    }
    if(document.documentElement.clientHeight != 0){
        y = document.documentElement.clientHeight;
    } else {
        y = window.innerHeight;
    }
    
    // element = document.getElementById(resizeelement);
    // if(element){
        // if (document.body && document.body.offsetWidth) {
            // winW = document.body.offsetWidth;
            // winH = document.body.offsetHeight;
        // }
        // if (document.compatMode=='CSS1Compat' &&
            // document.documentElement &&
            // document.documentElement.offsetWidth ) {
            // winW = document.documentElement.offsetWidth;
            // winH = document.documentElement.offsetHeight;
        // }
        // if (window.innerWidth && window.innerHeight) {
            // winW = window.innerWidth;
            // winH = window.innerHeight;
        // }
        
        // element.style.left = remargins + 'px';
        // element.style.top = remargins + 'px';
        // element.style.width = (winW - remargins * 2) + 'px';
        // element.style.height = (winH - remargins * 2) + 'px';
    // }
    
    for(var a = 0 ; a < minimizerows.length ; a++) {
        for(var b = 0 ; b < minimizerows[a].length ; b++) {
            var bar = document.getElementById(minimizerows[a][b] + 'Bar');
            var control = document.getElementById(minimizerows[a][b]);

            if(parseInt(control.style.left.substring(0,-2)) + 200 > x){
                var row = -1;
                var pos = -1;
                var i = 0;
                while( i < minimizerows.length && row == -1 ){
                    if((getnonempty(minimizerows[i]) + 1) * 200 + MinimizeLeftMargin <= x){
                        row = i;
                        pos = getfirstempty(minimizerows[i]);
                    }
                    i++
                }
                if(row == -1){row=minimizerows.length; pos=0; minimizerows[minimizerows.length]=[];}
                
                
                minimizerows[row][pos] = minimizerows[a][b];
                bar.style.width = '194px';
                bar.className = "floatingbarmini";
                control.style.width = '200px';
                control.className = "floatingcontrolmini";
                control.style.left = (MinimizeLeftMargin + 200 * pos) + 'px';
                if(MinimizeToTop){
                    control.style.top = (26 * row) + 'px';
                } else {
                    control.style.top = (y - 26 - 26 * row) + 'px';
                }
            }
        }
    }
}


/*minimizeControl and maximizeControl swap between three states:
    Normal: control floats as normal
    Maximized: control fills the window, loses resize
    Minimized: just a title bar at the bottom of the window
    
    In the max and min states, the associated button becomes a restore button
        the other button remains its usual
        
    minimizeControl is to be called by the min button, maximizeControl by the max button
    
    Both take the control and return false on an error
*/
function minimizeControl(control_id) {
    var control = document.getElementById(control_id);
    var minbut = document.getElementById(control_id + 'MinimizeButton');
    var maxbut = document.getElementById(control_id + 'MaximizeButton');
    var expand = document.getElementById(control_id + 'ResizeControl');
    var bar = document.getElementById(control_id + 'Bar');
    var div = document.getElementById(control_id + 'Text');
    if(!minbut || !maxbut || !control || !div){
        return false;
    }
    if (div.style.display == "none" && minbut.alt=="Restore Button") {
        //restore
        if(!expandControl(control_id, '')){return false;}
        
        control.onmousedown = function(){bringToTop(control_id);};
        
        restorecontrol(control_id);
        control.style.position = "absolute";
        minbut.src = ButtonPath + MinimizeButton;
        minbut.alt="Minimize Button";
        
        
        var temp = find(control_id,minimizerows);
        var temp2 = find(control_id,minimizerows[temp]);
        if(temp!=-1){
            delete minimizerows[temp][temp2]
        }
        
        bar.onmousedown = function(){moveMapControl(control_id);}
        bar.className = "floatingbar movecursor";
        control.className = "floatingcontrol";
        
    } else {
        //minimize
        if(maxbut.alt!="Restore Button"){
            savecontrol(control_id);
        } else {
            maxbut.src = ButtonPath + MaximizeButton;
            maxbut.alt="Minimize Button";
            restorecontrol(control_id);
            maxed = '';
        }
        if(!contractControl(control_id)){return false;}
        
        control.onmousedown = null;
        
        control.style.position = "fixed";
        control.style.zIndex = 999999;
        minbut.src = ButtonPath + RestoreButton;
        minbut.alt="Restore Button";
        
        var x, y;
        if(document.documentElement.clientWidth != 0){//some older browsers use different widths
            x = document.documentElement.clientWidth;
        } else {
            x = window.innerWidth;
        }
        if(document.documentElement.clientHeight != 0){//some older browsers use different variables for height
            y = document.documentElement.clientHeight;
        } else {
            y = window.innerHeight;
        }
        
        
        var row = -1;
        var pos = -1;
        for(var a = 0 ; a < minimizerows.length ; a++ ){
            if((getnonempty(minimizerows[a]) + 1) * 200 + MinimizeLeftMargin <= x && row == -1){
                row = a;
                pos = getfirstempty(minimizerows[a]);
            }
        }
        if(row == -1){row=minimizerows.length; pos=0; minimizerows[minimizerows.length]=[];}
        
        
        minimizerows[row][pos] = control_id;
        bar.style.width = '194px';
        control.style.width = '200px';
        control.style.left = (MinimizeLeftMargin + 200 * pos) + 'px';
        if(MinimizeToTop){
            control.style.top = (26 * row) + 'px';
        } else {
            control.style.top = (y - 26 - 26 * row) + 'px';
        }
        
        bar.onmousedown = null;
        bar.className = "floatingbarmini";
        control.className = "floatingcontrolmini";
        
    }
    return true;
}

function maximizeControl(control_id) {
    var control = document.getElementById(control_id);
    var minbut = document.getElementById(control_id + 'MinimizeButton');
    var maxbut = document.getElementById(control_id + 'MaximizeButton');
    var expand = document.getElementById(control_id + 'ResizeControl');
    var bar = document.getElementById(control_id + 'Bar');
    var div = document.getElementById(control_id+'Text');
    var iframe = document.getElementById(control_id+'Frame');
    if(!minbut || !maxbut || !control || !div){
        return false;
    }
    if (div.style.display != "none" && maxbut.alt=="Restore Button") {
        //restore
        if(expand){
            expand.style.visibility = "visible"; //show the resize image
        }
        
        control.onmousedown = function(){bringToTop(control_id);};
        
        maxbut.src = ButtonPath + MaximizeButton;
        maxbut.alt="Maximize Button";
        control.style.position = "absolute";
        restorecontrol(control_id);
        
        bar.onmousedown = function(){moveMapControl(control_id);}
        bar.className = "floatingbar movecursor";
        control.className = "floatingcontrol";
        
        maxed = '';
        
    } else {
        //maximize
        if(minbut.alt!="Restore Button"){
            savecontrol(control_id);
        } else {
            minbut.src = ButtonPath + MinimizeButton;
            minbut.alt="Minimize Button";
            if(!expandControl(control_id, '')){return false;}
            var temp = find(control_id,minimizerows);
            if(temp!=-1){
                delete minimizerows[temp][find(control_id,minimizerows[temp])]
            }
            control.onmousedown = function(){bringToTop(control_id);};
        }
        if(expand){
            expand.style.visibility = "hidden"; //hide the resize image
        }
        maxbut.src = ButtonPath + RestoreButton;
        maxbut.alt="Restore Button";
        control.style.position = "fixed";
        control.style.left = '0px';
        control.style.top = '0px';
        control.style.zIndex = maxIndex;
        
        var a, b;
        if(document.documentElement.clientWidth != 0){//some older browsers use different widths
            a = document.documentElement.clientWidth;
        } else {
            a = window.innerWidth;
        }
        if(document.documentElement.clientHeight != 0){//some older browsers use different variables for height
            b = document.documentElement.clientHeight;
        } else {
            b = window.innerHeight;
        }
        
        control.style.width = a + 'px';
        bar.style.width = (a - 6) + 'px';
        div.style.width = (a - 10) + 'px';
        control.style.height = b + 'px';
        div.style.height = (b - 32) + 'px';
        if(iframe){
            iframe.style.width = (a - 12) + 'px';
            iframe.style.height = (b - 36) + 'px';
        }
        
        bar.onmousedown = null;
        bar.className = "floatingbar";
        control.className = "floatingcontrol";
        
        maxed = control_id;
    }
    return true;
}

function maximizeControlHalf(control_id, maxright) {
    var control = document.getElementById(control_id);
    var minbut = document.getElementById(control_id + 'MinimizeButton');
    var maxbut = document.getElementById(control_id + 'MaximizeButton');
    var expand = document.getElementById(control_id + 'ResizeControl');
    var bar = document.getElementById(control_id + 'Bar');
    var div = document.getElementById(control_id+'Text');
    var iframe = document.getElementById(control_id+'Frame');
    if(!minbut || !maxbut || !control || !div){
        return false;
    }
    if (div.style.display != "none" && maxbut.alt=="Restore Button") {
        //restore
        if(expand){
            expand.style.visibility = "visible"; //show the resize image
        }
        
        control.onmousedown = function(){bringToTop(control_id);};
        
        maxbut.src = ButtonPath + MaximizeButton;
        maxbut.alt="Maximize Button";
        control.style.position = "absolute";
        restorecontrol(control_id);
        
        bar.onmousedown = function(){moveMapControl(control_id);}
        bar.className = "floatingbar movecursor";
        control.className = "floatingcontrol";
        
        maxed = '';
        
    } else {
        //maximize
        if(minbut.alt=="Restore Button"){
            minbut.src = ButtonPath + MinimizeButton;
            minbut.alt="Minimize Button";
            if(!expandControl(control_id, '')){return false;}
            var temp = find(control_id,minimizerows);
            if(temp!=-1){
                delete minimizerows[temp][find(control_id,minimizerows[temp])]
            }
            control.onmousedown = function(){bringToTop(control_id);};
        }
        if(expand){
            expand.style.visibility = "hidden"; //hide the resize image
        }
        maxbut.src = ButtonPath + RestoreButton;
        maxbut.alt="Restore Button";
        control.style.position = "fixed";
        control.style.top = '0px';
        
        var a, b;
        if(document.documentElement.clientWidth != 0){//some older browsers use different widths
            a = document.documentElement.clientWidth;
        } else {
            a = window.innerWidth;
        }
        if(document.documentElement.clientHeight != 0){//some older browsers use different height variables
            b = document.documentElement.clientHeight;
        } else {
            b = window.innerHeight;
        }
        
        if(maxright){
            control.style.left = (a - a / 2) + 'px';
        } else {
            control.style.left = '0px';
        }
        
        a = a / 2;
        
        control.style.width = a + 'px';
        bar.style.width = (a - 6) + 'px';
        div.style.width = (a - 10) + 'px';
        control.style.height = b + 'px';
        div.style.height = (b - 32) + 'px';
        if(iframe){
            iframe.style.width = (a - 12) + 'px';
            iframe.style.height = (b - 36) + 'px';
        }
        
        bar.onmousedown = null;
        bar.className = "floatingbar";
        control.className = "floatingcontrol";
        
        maxed = control_id;
    }
    return true;
}

//Displays a div (or other element) that was hidden by killDiv or similar methods
//takes the element to show
function openControl(control_id) {
    var div = document.getElementById(control_id);
    var button = document.getElementById(control_id+'DisplayButton');
    var minbut = document.getElementById(control_id + 'MinimizeButton');
    if(div.style.visibility == "hidden"){
        div.style.visibility = "visible";
    }
    if(div.style.display == "none"){
        div.style.display = "inline";
    }
    if(button && button.src == ButtonPath + ContractButton){
        expandControl(control_id);
    }
    if(minbut && minbut.alt=="Restore Button"){
        minimizeControl(control_id);
    }
}

//'permanently' hides a floating control (or other element)
//takes the element to be hidden
function killDiv(element_id) {
    var div = document.getElementById(element_id);
    div.style.visibility = "hidden";
    div.style.display = "none";
}

//clears the internal html of an iframe
//takes the id of the iframe to be emptied
function emptyIframe(control_id) {
    var iframe = document.getElementById(control_id+"Frame");
    iframe.src = '/blank.html';
}

function bringToTop(element_id){
    var control = document.getElementById(element_id);
    if(control.style.zIndex != currenttop && control.style.zIndex != maxIndex){
        currenttop++;
        control.style.zIndex = currenttop;
    }
}