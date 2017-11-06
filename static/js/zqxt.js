var menu = $('#topnavDIV'), pos = menu.offset();
$(window).scroll(function(){
    if($(this).scrollTop() > pos.top){
        menu.addClass('topnavContainerScroll');        
        $("#topDIV").addClass('topScroll');
        $(".w3DropdownMenu").addClass('w3DropdownMenuScroll').css('margin-top','38px');        
        $("#menyen").addClass('menyenScroll');
        $("#topLogo").css("display","none");
     } else if($(this).scrollTop() <= pos.top){
        menu.removeClass('topnavContainerScroll');
        $("#topDIV").removeClass('topScroll');
        $(".w3DropdownMenu").removeClass('w3DropdownMenuScroll').css('margin-top','88px');
        $("#menyen").removeClass('menyenScroll');
        $("#topLogo").css("display","");
     } });
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
    $("#w3dropdowntutorials").fadeToggle(200, function () {$("#dropdownTutorialsBtn").css("background-color","");$("#dropdownTutorialsBtn").css("color","");});
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
    $("#w3dropdownreferences").fadeToggle(200, function(){$("#dropdownReferencesBtn").css("background-color","");$("#dropdownReferencesBtn").css("color","");});
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
    $("#w3dropdownexamples").fadeToggle(200, function(){$("#dropdownExamplesBtn").css("background-color","");$("#dropdownExamplesBtn").css("color","");});
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
    $("#w3dropdownsearch").fadeToggle(200, function(){$("#gsc-i-id1").focus();$("#dropdownSearchBtn").css("background-color","");});
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
    $("#w3dropdowntranslate").fadeToggle(200, function(){$("#dropdownTranslateBtn").css("background-color","");});
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
xmlhttp.send("url=" + err_url + "&email=" + err_email + "&desc=" + err_desc);

document.getElementById("err_desc").value="";
hideError();
document.getElementById("err_sent").style.display="block";
}


function printPage()
{
content=document.getElementsByClassName("main")[0].getElementsByTagName("div")[0].getElementsByTagName("div")[0].innerHTML;
head=document.getElementsByTagName("head")[0].innerHTML;
var myWindow=window.open('','','');
myWindow.document.write("<html><head>"+head+"<style>body{padding:15px;}</style></head><body><button onclick='window.print()'>Print Page</button>"+content+"<center><p>文章来源：<a href='http://www.ziqiangxuetang.com'>自强学堂 在线教程</a></p></center></body></html>");
}


//hight html code
(function () {
function lookAhead(x, ipos, n) {
var i, c, text;
text = "";
for (i = ipos; i < ipos + n; i++) {
  if (i < x.length) {
    c = x.charAt(i);
    text += c;
  }
}
return text.toUpperCase();
}
var x, y, z, i, j, c, ch, text, status, ele;
if (!document.getElementsByClassName) {return;}
y = document.getElementsByClassName("htmlHigh");
for (j = 0; j < y.length; j++) {
z = y[j];
ele = "";
text = "";
script = false;
status = "TAGW";
x = z.innerHTML;

for (i = 0; i < x.length; i++) {
c = x.charAt(i);
ch = c.charCodeAt(0);  
if (status == "ANG") {
  if (c == "}") {
    if (lookAhead(x, i, 2) == "}}") {
      text += "}}" + "</span>";
      i++;
      status = "TAGW";
      continue;
    }
  }
} 
if (status == "TAGW") {
  if (c == "&") {
    if (lookAhead(x, i, 7) == "&LT;!--") {
      text += "<span class='highCOM'>" + c;
      status = "COM";
      continue;
    }
    if (lookAhead(x, i, 4) == "&LT;") {
      if (script == true) {
        if (lookAhead(x, i, 11) != "&LT;/SCRIPT") {
          text += c;
          continue;
        }
        if (lookAhead(x, i, 11) == "&LT;/SCRIPT") {
          script = false;
        }
      }
      text += "<span class='highLT'>" + c;
      status = "LT";
      continue;
    }         
  }
  if (c == "{") {
    if (lookAhead(x, i, 2) == "{{") {
      text += "<span class='highATT'>" + c;
      status = "ANG";
      continue;
    }
  }    
}          
if (status == "ELEW") {
  if (ch != 32 && ch != 10 && ch != 13 && ch != 9) {
    text += "<span class='highELE'>" + c;
    ele = c;
    status = "ELE";
    if (lookAhead(x, i, 9) == "SCRIPT&GT") {script = true;}
    continue;
  }
} 
if (status == "ELE") {
  if (ch == 32 || ch == 10 || ch == 13 || ch == 9) {
    text += "</span>";
    status = "ATTW"; 
  }
  if (c == "&") {
    if (lookAhead(x, i, 4) == "&GT;") {
      text += "</span><span class='highGT'>" + c;
      status = "GT";
      continue;
    }
  }
  ele += c;
}        
if (status == "ATTW") {
  if (c == "&")
    if (lookAhead(x, i, 4) == "&GT;") {
      text += "<span class='highGT'>" + c;
      status = "GT";
      continue;
    }
  if (ch != 32 && ch != 10 && ch != 13 && ch != 9) {
    text += "<span class='highATT'>" + c;
    status = "ATT";
    continue;
  }
} 
if (status == "ATT") {
  if (c == "=") {
    text += c + "</span><span class='highVAL'>";
    status = "VALW";
    continue;
  }
  if (c == "&") {
    if (lookAhead(x, i, 4) == "&GT;") {
      text += "</span><span class='highGT'>" + c;
      status = "GT";
      continue;
    }
  }       
}
if (status == "COM") {
  if (c == "-") {
    if (lookAhead(x, i, 6) == "--&GT;") {
      text += c;
      status = "COMW";
      continue;
    }
  }
}       
if (status == "COMW") {
  if (c == "&") {
    if (lookAhead(x, i, 4) == "&GT;") {
      text += c;
      status = "GT";
      continue;
    }
  }
}       
if (status == "VALS") {
  if (c == "'") {
    text += c + "</span>";
    status = "ATTW";
    continue;
  }
}
if (status == "VALD") {
  if (c == '"') {
    text += c + "</span>";
    status = "ATTW";
    continue;
  }
}
if (status == "VALW") {
  if (c == "'") {
    status = "VALS";
    text += c;
    continue;
  }
  if (c == '"') {
    status = "VALD";
    text += c;
    continue;
  }    
}  
if (status == "LT") {
  if (c == ";") {
    text += c + "</span>";
    status = "ELEW";
    continue;
  }
} 
if (status == "GT") {
  if (c == ";") {
    text += c + "</span>";
    status = "TAGW";
    continue;
  }
} 
text += c;
}
z.innerHTML = text;


}})();

(function () {
function lookAhead(x, ipos, n) {
var i, c, text;
text = "";
for (i = ipos; i < ipos + n; i++) {
  if (i < x.length) {
    c = x.charAt(i);
    text += c;
  }
}
return text.toUpperCase();
}
var x, y, z, i, j, c, ch, text, status, temp, span;
if (!document.getElementsByClassName) {return;}
y = document.getElementsByClassName("cssHigh");
for (j = 0; j < y.length; j++) {
z = y[j];
text = "";
temp = "";
span = false;
status = "SELW";
x = z.innerHTML;

for (i = 0; i < x.length; i++) {
c = x.charAt(i);
ch = c.charCodeAt(0);  
if (c == "<") {
  text += c;
  temp = status;
  status = "TAG";
  continue;
}
if (c == "/") {
  if (lookAhead(x, i, 2) == "/*") {
    text += "<span class='highCOM'>";
    span = true;
    temp = status;
    status = "COM";
  }     
  text += c;
  continue;   
} 
if (status == "COM" ) {
  if (c == "*") {
      if (lookAhead(x, i, 2) == "*/") {
        if (span) {
          text += c;
          i++;
          text += x.charAt(i);
          text += "</span>";
          span = false;
          status = temp;
        }
      } else {
        text += c;
      }    
  continue;   
  }    
} 
if (status == "MED") {
  if (c == "{") {
    text += "</span>" + c;
    span = false;
    status = "SELW";
    continue;
  }
}           
if (status == "SELW") {
  if (c == "@") {
    if (lookAhead(x,i,5) == "@FONT") {
      text += "<span class='highELE'>" + c;
      span = true;
      status = "SEL";
      continue;
    } else {
      text += "<span class='highELE'>" + c;
      span = true;
      status = "MED";
      continue;
    }
  }
  if (c == "}") {
    text += c;
    continue;
  }
  if (ch != 32 && ch != 10 && ch != 13 && ch != 9) {
    text += "<span class='highELE'>" + c;
    span = true;
    status = "SEL";
    continue;
  }
}           
if (status == "TAG") {
  text += c;
  if (c == ">") {
    status = temp;
  }        
  continue;
}
if (c == "&") {
  text += c;
  if (lookAhead(x, i, 6) == "&NBSP;") {
    temp = status;
    status = "NBSP";
  }
  continue; 
}
if (status == "NBSP") {
  text += c;
  if (c == ";") {
    status = temp;
  }        
  continue;
}
if (status == "SEL") {
  if (c == "{") {
    if (span) {
      text += "</span>";
      span = false;
    }
    text += c;
    status = "PROW"; 
    continue;
  }
}        
if (status == "PROW") {
  if (c == "}") {
    if (span) {
      text += "</span>";
      span = false;
    }
    text += c;
    status = "SELW"; 
    continue;
  } 
  if (ch != 32 && ch != 10 && ch != 13 && ch != 9) {
    text += "<span class='highATT'>" + c;
    span = true;
    status = "VALW"; 
    continue;
  }
}        
if (status == "VALW") {
  if (c == ":") {
    text += c; 
    if (span) {
      text += "</span>";
      span = false;
    }
    text += "<span class='highVAL'>";
    span = true;
    status = "VAL"; 
    continue;
    }
}        
if (status == "VAL") {
  if (c == "}") {
    if (span) {
      text += "</span>";
      span = false;
    }
    text += c;
    status = "SELW"; 
    continue;
  }
  if (c == ";") {
    text += c;
    if (span) {
      text += "</span>";
      span = false;
    }
    status = "PROW"; 
    continue;
  }
}        
text += c;
}

z.innerHTML = text;

}})();

(function () {
function lookAhead(x, ipos, n) {
var i, c, text;
text = "";
for (i = ipos; i < ipos + n; i++) {
  if (i < x.length) {
    c = x.charAt(i);
    text += c;
  }
}
return text.toUpperCase();
}
var x, y, z, i, j, c, ch, text, status;
if (!document.getElementsByClassName) {return;}
y = document.getElementsByClassName("jsonHigh");
for (j = 0; j < y.length; j++) {
z = y[j];
text = "";
status = "";
x = z.innerHTML;

for (i = 0; i < x.length; i++) {
c = x.charAt(i);
ch = c.charCodeAt(0);  
 
if (status == "") {
  if (c == '"') {
    status = "OBJNAME";
    text += "<span class='highELE'>" + c;
    continue;
  }        
  if (c == "{") {
    status = "OBJECT";
    text += c;
    continue;
  }
  text += c;
  continue;
}
if (status == "OBJECT") {
  if (c == '"') {
    status = "OBJNAME";
    text += "<span class='highELE'>" + c;
    continue;
  }        
  text += c;
  continue;
}
if (status == "OBJNAME") {
  if (c == '"') {
    status = "WAITCOLON";
    text += c + "</span>"
    continue;
  }        
  text += c;
  continue;
}
if (status == "WAITCOLON") {
  if (c == ":") {
    status = "COLON";
    text += c;
    continue;
  }
  text += c;
  continue;
}        
if (status == "COLON") {
  if (c == '"') {
    status = "VALUE";
    text += "<span class='highVAL'>" + c;
    continue;
  }
  if (ch > 47 && ch < 58) {
    status = "NUMBER";
    text += "<span class='highVAL'>" + c;
    continue;
  }
  if (c == "{") {
    status = "OBJECT";
    text += c;
    continue;
  }
  if (c == "[") {
    status = "ARRAY";
    text += c;
    continue;
  }
  text += c;
  continue;
}
if (status == "ARRAY") {
  if (c == ']') {
    status = ""; 
    text += c;
    continue;
  }
  if (c == '{') {
    status = "OBJECT"; 
    text += c;
    continue;
  }
  text += c;
  continue;
}        
if (status == "VALUE") {
  if (c == '"') {
    status = "OBJECT"; 
    text += c + "</span>";
    continue;
  }
  text += c;
  continue;
}
if (status == "NUMBER") {
  if (ch < 48 || ch > 57) {
    status = ""; 
    text += "</span>" + c;
    continue;
  }
  text += c;
  continue;
} 
text += c;
}
z.innerHTML = text;
}})();

(function () {
function lookAhead(x, ipos, n) {
var i, c, ch, text;
text = "";
for (i = ipos; i < ipos + n; i++) {
  if (i < x.length) {
    c = x.charAt(i);
    ch = c.charCodeAt(0);  
    if (ch == 32 || ch == 10 || ch == 13 || ch == 9 ) {
      text += " ";        
    } else {
      text += c;
    }
  }
}
return text;
}
function lookWord(x, ipos) {
var i, c, ch, text;
text = "";
for (i = ipos; i < x.length; i++) {
  c = x.charAt(i);
  ch = c.charCodeAt(0);  
  if (ch == 10 || ch == 13 || ch == 9 || ch == 32 || ch == 38 || ch == 40 || ch == 41 || ch == 42 || ch == 43 ||
  ch == 44 || ch == 58 || ch == 47 || ch == 58 || ch == 59 || ch == 60 || ch == 61 || ch == 91 || ch == 93) {
    return text;        
  } else {
    text += c;
  }
}
return text;
}
var x, y, z, i, j, k, c, ch, text, status, ele, comp, pos;
jsArr = ["var","boolean","break","case","catch","continue","debugger","default","do","else","finally","for",
"function","if","in","new","return","switch","throw","try","typeof","while","with"];
if (!document.getElementsByClassName) {return;}
y = document.getElementsByClassName("jsHigh");
for (j = 0; j < y.length; j++) {
z = y[j];
ele = "";
text = "";
status = "";
x = z.innerHTML;

for (i = 0; i < x.length; i++) {
  c = x.charAt(i);
  ch = c.charCodeAt(0);
  if (ch == 32 || ch == 10 || ch == 13 || ch == 9 ) {
    text += c;
    continue;
  }
  if (lookAhead(x, i, 2) == "//") {
    text += "<span class='highCOM'>";  
    pos = x.substr(i).indexOf("<br>");
    if (pos == -1) {
      text += x.substr(i); 
      i = x.length;
    } else {
      text += x.substr(i,pos + 4);
      i += pos + 3;
    }  
    text += "</span>"
    continue;
  }
  if (lookAhead(x, i, 2) == "/*") {
    text += "<span class='highCOM'>";  
    pos = x.substr(i).indexOf("*/");
    if (pos == -1) {
      text += x.substr(i); 
      i = x.length;
    } else {
      text += x.substr(i,pos + 2);
      i += pos + 1;
    }  
    text += "</span>"
    continue;
  }
  if (c == "&") {
    pos = x.substr(i).indexOf(";");
    if (pos == -1) {
      text += x.substr(i); 
      i = x.length;
    } else {
      text += x.substr(i,pos + 1);
      i += pos;
    }  
    continue;
  }
  if (c == "'" || c == '"') {
    text += "<span class='highVAL'>";  
    pos = x.substr(i+1).indexOf(c);
    if (pos == -1) {
      text += x.substr(i); 
      i = x.length;
    } else {
      text += x.substr(i, pos + 2);
      i += pos + 1;
    }  
    text += "</span>"
    continue;
  }
  if (lookAhead(x, i, 4) == "<br>") {
    i += 3;
    text += "<br>";
    continue
  }
  ele = lookWord(x, i);
  if (ele) {
    if (ele =="true" || ele == "false" || ele == "null" || isNaN(ele) == false) {  
      text += "<span class='highVAL'>" + x.substr(i,ele.length) + "</span>";
      i += ele.length - 1;
      status = "";
      continue;
    }
    for (k = 0; k < jsArr.length; k++) {
      if (ele == jsArr[k]) {
        text += "<span class='highELE'>" + x.substr(i,ele.length) + "</span>";
        i += ele.length - 1;
        status = "SPW";
        break;
      }  
    }
    if (status == "SPW") {
      status = "";
      continue;   
    } else {
      text += x.substr(i, ele.length);
      i += ele.length - 1;
      continue;
    }
  }
  text += c;
}
z.innerHTML = text;
}})();
