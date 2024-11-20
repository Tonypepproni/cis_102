var navItems = document.getElementsByClassName("nav-li")
var collapsed = false

function collapse(){
    if (collapsed == false) {
        collapsed = true
        for(var i=0; i<navItems.length; i++){
            navItems[i].style.display = "none"
        }
    }
    else{
        collapsed = false
        for(var i=0; i<navItems.length; i++){
            navItems[i].style.display = "flex"
        }
    }
}