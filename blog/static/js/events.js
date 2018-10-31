document.getElementById("mouseover").onmouseover = function() {mouseover()};
document.getElementById("mouseover").onmouseout = function() {mouseout()};

function mouseOver() {
    document.getElementById("mouseover").style.color = "yellow";
}

function mouseOut() {
    document.getElementById("mouseover").style.color="black";
}