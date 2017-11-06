var menu = $('#topnavDIV'), pos = menu.offset();
$(window).scroll(function(){
    if($(this).scrollTop() > pos.top && menu.hasClass('topnavContainer')){
        menu.removeClass('topnavContainer').addClass('topnavContainer2');
        $("#topDIV").removeClass('top').addClass('top2');
        $(".w3DropdownMenu").removeClass('w3DropdownMenuNotScroll').addClass('w3DropdownMenuScroll').css('margin-top','38px');
     } else if($(this).scrollTop() <= pos.top && menu.hasClass('topnavContainer2')){
        menu.removeClass('topnavContainer2').addClass('topnavContainer');
        $("#topDIV").removeClass('top2').addClass('top');
        $(".w3DropdownMenu").removeClass('w3DropdownMenuScroll').addClass('w3DropdownMenuNotScroll').css('margin-top','90px');
     }
});
$(document).ready(function(){
  $("#dropdownTutorialsBtn").click(function(){
    closeTheOthers("tutorials");
    if ($("#w3dropdowntutorials").css("display") == "none") {
      $("#dropdownTutorialsBtn").css("background-color","#f5f5f5");
      $("#dropdownTutorialsBtn").css("color","#555555");
    } else {
      $("#dropdownTutorialsBtn").css("background-color","");
      $("#dropdownTutorialsBtn").css("color","");
    }
    $("#w3dropdowntutorials").fadeToggle(200, function () {
    });
    return false;      
  });
  $("#dropdownReferencesBtn").click(function(){
    closeTheOthers("references");
    if ($("#w3dropdownreferences").css("display") == "none") {
      $("#dropdownReferencesBtn").css("background-color","#f5f5f5");
      $("#dropdownReferencesBtn").css("color","#555555");
    } else {
      $("#dropdownReferencesBtn").css("background-color","");
      $("#dropdownReferencesBtn").css("color","");
    }
    $("#w3dropdownreferences").fadeToggle(200);
    return false;      
  });
  $("#dropdownExamplesBtn").click(function(){
    closeTheOthers("examples");
    if ($("#w3dropdownexamples").css("display") == "none") {
      $("#dropdownExamplesBtn").css("background-color","#f5f5f5");
      $("#dropdownExamplesBtn").css("color","#555555");
    } else {
      $("#dropdownExamplesBtn").css("background-color","");
      $("#dropdownExamplesBtn").css("color","");
    }
    $("#w3dropdownexamples").fadeToggle(200);
    return false;      
  });
  $("#dropdownSearchBtn").click(function(){
    closeTheOthers("search");
    if ($("#w3dropdownsearch").css("display") == "none") {
      $("#dropdownSearchBtn").css("background-color","#f5f5f5");
      $("#dropdownSearchBtn").css("color","#555555");
    } else {
      $("#dropdownSearchBtn").css("background-color","");
      $("#dropdownSearchBtn").css("color","");
    }
    $("#w3dropdownsearch").fadeToggle(200, function(){$("#gsc-i-id1").focus();});
    return false;      
  });
  $("#dropdownTranslateBtn").click(function(){
    closeTheOthers("translate");
    if ($("#w3dropdowntranslate").css("display") == "none") {
      $("#dropdownTranslateBtn").css("background-color","#f5f5f5");
      $("#dropdownTranslateBtn").css("color","#555555");
    } else {
      $("#dropdownTranslateBtn").css("background-color","");
      $("#dropdownTranslateBtn").css("color","");
    }
    $("#w3dropdowntranslate").fadeToggle(200);
    return false;      
  });
  $(".main").click(function(){
    closeTheOthers();
  });
  $(".top").click(function(){
    closeTheOthers();
  });
});
function closeTheOthers(x) {
    if (x != "tutorials") { 
        $("#dropdownTutorialsBtn").css("background-color","");
        $("#dropdownTutorialsBtn").css("color","");
        $("#w3dropdowntutorials").fadeOut(100);
    }
    if (x != "references") { 
        $("#dropdownReferencesBtn").css("background-color","");
        $("#dropdownReferencesBtn").css("color","");
        $("#w3dropdownreferences").fadeOut(100);
    }
    if (x != "examples") { 
        $("#dropdownExamplesBtn").css("background-color","");
        $("#dropdownExamplesBtn").css("color","");
        $("#w3dropdownexamples").fadeOut(100);
    }
    if (x != "search") { 
        $("#dropdownSearchBtn").css("background-color","");
        $("#dropdownSearchBtn").css("color","");
        $("#w3dropdownsearch").fadeOut(100);
    }
    if (x != "translate") { 
        $("#dropdownTranslateBtn").css("background-color","");
        $("#dropdownTranslateBtn").css("color","");
        $("#w3dropdowntranslate").fadeOut(100);
    }
}
var menyknapp_hartrykket = 0;
function vismenyen() {
closeTheOthers();
x = document.getElementById("menyen");
if (menyknapp_hartrykket == 0) {
    x.style.position = "fixed";
    x.style.zIndex = "1000";    
    x.style.top = "90px";   
    x.style.bottom = "0";   
    x.style.overflow = "auto";  
    x.style.display = "block";
    x.style.right = "0";
    x.style.backgroundColor = "#ffffff";
    x.style.padding = "20px";
    x.style.borderLeft = "2px solid #f1f1f1";
    x.style.borderBottom = "2px solid #f1f1f1";
    menyknapp_hartrykket = 1;
} else {
    x.style.display = "none";
    menyknapp_hartrykket = 0;
}
}
function hideDropdownMenu() {
    closeTheOthers();
}


var addr=document.location.href;
function displayError()
{
document.getElementById("err_url").value=addr;
document.getElementById("err_form").style.display="block";
document.getElementById("err_desc").focus();
hideSent();
}
function hideError()
{
document.getElementById("err_form").style.display="none";
}
function hideSent()
{
document.getElementById("err_sent").style.display="none";
}
function sendErr()
{
var xmlhttp;
var err_url=document.getElementById("err_url").value;
var err_email=document.getElementById("err_email").value;
var err_desc=document.getElementById("err_desc").value;
var csrfmiddlewaretoken=document.getElementsByName("csrfmiddlewaretoken")[0].value;
if (window.XMLHttpRequest) {
  // code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
} else {
  // code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
}
xmlhttp.open("POST","/error_tutorial.py",true);
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xmlhttp.setRequestHeader("X-CSRFToken", csrfmiddlewaretoken);
xmlhttp.send("url=" + err_url + "&email=" + err_email + "&desc=" + escape(err_desc));

document.getElementById("err_desc").value="";
hideError();
document.getElementById("err_sent").style.display="block";
}

function printPage()
{
content=document.getElementsByClassName("main")[0].getElementsByTagName("DIV")[0].innerHTML;
head=document.getElementsByTagName("head")[0].innerHTML;
var myWindow=window.open('','','');
myWindow.document.write("<html><head>"+head+"<style>body{padding:15px;}</style></head><body><button onclick='window.print()'>Print Page</button>"+content+"<p><a href='http://www.ziqiangxuetang.com'>自强学堂</a> Copyright 2008-2015. All Rights Reserved.</p></body></html>");
}