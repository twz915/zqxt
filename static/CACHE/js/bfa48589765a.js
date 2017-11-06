if(window.addEventListener){window.addEventListener("resize",browserResize);}else if(window.attachEvent){window.attachEvent("onresize",browserResize);}
var xbeforeResize=window.innerWidth;var ybeforeResize=window.innerWidth;var zbeforeResize=window.innerWidth;function skyscraperResize(){if(window.innerWidth<975+17){document.getElementById("right-ad-1").style.minHeight="0";}}
function browserResize(){var afterResize=window.innerWidth;if((xbeforeResize<(1200+14)&&afterResize>=(1200+14))||(xbeforeResize>=(1200+14)&&afterResize<(1200+14))||(xbeforeResize<(700+14)&&afterResize>=(700+14))||(xbeforeResize>=(700+14)&&afterResize<(700+14))||(xbeforeResize<(480+17)&&afterResize>=(480+17))||(xbeforeResize>=(480+17)&&afterResize<(480+17))){xbeforeResize=afterResize;}
if((ybeforeResize<(1675+14)&&afterResize>=(1675+14))||(ybeforeResize>=(1675+14)&&afterResize<(1675+14))||(ybeforeResize<(1100+14)&&afterResize>=(1100+14))||(ybeforeResize>=(1100+14)&&afterResize<(1100+14))||(ybeforeResize<(975+17)&&afterResize>=(975+17))||(ybeforeResize>=(975+17)&&afterResize<(975+17))){ybeforeResize=afterResize;skyscraperResize()}
if((zbeforeResize<(1200+14)&&afterResize>=(1200+14))||(zbeforeResize>=(1200+14)&&afterResize<(1200+14))){zbeforeResize=afterResize;}}
skyscraperResize();function open_menu(){var x,m;m=(document.getElementById("leftmenu")||document.getElementById("sidemenu"));if(m.style.display=="block"){close_menu();}else{w_close_all_nav();m.style.display="block";if(document.getElementsByClassName){x=document.getElementsByClassName("chapter")
for(i=0;i<x.length;i++){x[i].style.visibility="hidden";}
x=document.getElementsByClassName("nav")
for(i=0;i<x.length;i++){x[i].style.visibility="hidden";}
x=document.getElementsByClassName("sharethis")
for(i=0;i<x.length;i++){x[i].style.visibility="hidden";}}
fix_sidemenu();}}
function close_menu(){var m;m=(document.getElementById("leftmenu")||document.getElementById("sidemenu"));m.style.display="none";if(document.getElementsByClassName){x=document.getElementsByClassName("chapter")
for(i=0;i<x.length;i++){x[i].style.visibility="visible";}
x=document.getElementsByClassName("nav")
for(i=0;i<x.length;i++){x[i].style.visibility="visible";}
x=document.getElementsByClassName("sharethis")
for(i=0;i<x.length;i++){x[i].style.visibility="visible";}}}
if(window.addEventListener){window.addEventListener("scroll",function(){fix_sidemenu();});window.addEventListener("resize",function(){fix_sidemenu();});window.addEventListener("touchmove",function(){fix_sidemenu();});window.addEventListener("load",function(){fix_sidemenu();});}else if(window.attachEvent){window.attachEvent("onscroll",function(){fix_sidemenu();});window.attachEvent("onresize",function(){fix_sidemenu();});window.attachEvent("ontouchmove",function(){fix_sidemenu();});window.attachEvent("onload",function(){fix_sidemenu();});}
function fix_sidemenu(){if(document.getElementById("leftmenu")){var w,top;w=window.innerWidth||document.documentElement.clientWidth||document.body.clientWidth;top=scrolltop()
if(w<993&&w>600){if(top==0){document.getElementById("leftmenu").style.paddingTop="147px";}
if(top>0&&top<100){document.getElementById("leftmenu").style.paddingTop=(140-top)+"px";}
if(top>100){document.getElementById("leftmenu").style.paddingTop=document.getElementById("topnav").offsetHeight+"px";document.getElementById("belowtopnav").style.paddingTop="44px";document.getElementById("topnav").style.position="fixed";document.getElementById("topnav").style.top="0";}else{document.getElementById("belowtopnav").style.paddingTop="0";document.getElementById("topnav").style.position="relative";}
document.getElementById("leftmenuinner").style.paddingTop="0";}else{if(top==0){if(w<600){document.getElementById("leftmenu").style.paddingTop="109px";}else{document.getElementById("leftmenu").style.paddingTop="0";}}
if(top>63){document.getElementById("leftmenu").style.paddingTop="0";if(w>992){document.getElementById("leftmenuinner").style.paddingTop="44px";}
document.getElementById("belowtopnav").style.paddingTop="44px";document.getElementById("topnav").style.position="fixed";document.getElementById("topnav").style.top="0";}else{if(w>992){document.getElementById("leftmenuinner").style.paddingTop=(112-top)+"px";}
document.getElementById("belowtopnav").style.paddingTop="0";document.getElementById("topnav").style.position="relative";}}}else{var w,top;w=window.innerWidth||document.documentElement.clientWidth||document.body.clientWidth;top=scrolltop()
if(w<993&&w>600){if(top==0){document.getElementById("sidemenu").style.paddingTop="147px";}
if(top>0&&top<100){document.getElementById("sidemenu").style.paddingTop=(140-top)+"px";}
if(top>100){document.getElementById("sidemenu").style.paddingTop=document.getElementById("topnav").offsetHeight+"px";document.getElementById("belowtopnav").style.paddingTop="44px";document.getElementById("topnav").style.position="fixed";document.getElementById("topnav").style.top="0";}else{document.getElementById("belowtopnav").style.paddingTop="0";document.getElementById("topnav").style.position="relative";}}else{if(top==0){if(w<600){document.getElementById("sidemenu").style.paddingTop="109px";}else{document.getElementById("sidemenu").style.paddingTop="0";}}
if(top>63){document.getElementById("sidemenu").style.paddingTop="0";document.getElementById("belowtopnav").style.paddingTop="44px";document.getElementById("topnav").style.position="fixed";document.getElementById("topnav").style.top="0";}else{document.getElementById("belowtopnav").style.paddingTop="0";document.getElementById("topnav").style.position="relative";}}}}
function scrolltop(){var top=0;if(typeof(window.pageYOffset)=="number"){top=window.pageYOffset;}else if(document.body&&document.body.scrollTop){top=document.body.scrollTop;}else if(document.documentElement&&document.documentElement.scrollTop){top=document.documentElement.scrollTop;}
return top;}
function w_open_nav(x){var contentNode;if(document.getElementById("nav_"+x).style.display=="block"){w_close_nav(x);}else{w_close_all_nav();if(document.getElementById("nav_"+x).innerHTML==""){contentNode=document.body.removeChild(document.getElementById("nav_"+x+"_content"));document.getElementById("nav_"+x).appendChild(contentNode);document.getElementById("nav_"+x+"_content").style.display="block";}
document.getElementById("nav_"+x).style.display="block";if(document.getElementById("topnavbtn_"+x)){document.getElementById("topnavbtn_"+x).getElementsByTagName("i")[0].style.display="none";document.getElementById("topnavbtn_"+x).getElementsByTagName("i")[1].style.display="inline";}
if(x=="search"){if(document.getElementById("gsc-i-id1")){document.getElementById("gsc-i-id1").focus();}}}}
function w_close_nav(x){document.getElementById("nav_"+x).style.display="none";if(document.getElementById("topnavbtn_"+x)){document.getElementById("topnavbtn_"+x).getElementsByTagName("i")[0].style.display="inline";document.getElementById("topnavbtn_"+x).getElementsByTagName("i")[1].style.display="none";}}
function w_close_all_nav(){w_close_nav("tutorials");w_close_nav("references");w_close_nav("examples");w_close_nav("search");close_menu();}
(function(){var x,i,a,b,m;m=(document.getElementById("leftmenu")||document.getElementById("sidemenu"));x=m.getElementsByTagName("A");i;for(i=0;i<x.length;i++){if(document.location.href.indexOf(x[i].href)>=0){x[i].className="active";}}
x=document.getElementById("topnav").getElementsByTagName("A");for(i=0;i<x.length;i++){a=document.location.pathname;b=x[i].pathname;if(a.substr(0,a.indexOf("/",1))==b.substr(0,b.indexOf("/",1))){x[i].className="active";}}
if(window.addEventListener){document.getElementById("main").addEventListener("click",w_close_all_nav,true);m.addEventListener("click",w_close_all_nav,true);document.getElementById("right").addEventListener("click",w_close_all_nav,true);}else if(window.attachEvent){document.getElementById("main").attachEvent("onclick",w_close_all_nav);m.attachEvent("onclick",w_close_all_nav);document.getElementById("right").attachEvent("onclick",w_close_all_nav);}})();function searchfield_focus(obj)
{obj.style.color=""
obj.style.fontStyle=""
if(obj.value=="搜索 自强学堂")
{obj.value=""}}
var addr=document.location.href;function displayError()
{document.getElementById("err_url").value=addr;document.getElementById("err_form").style.display="block";document.getElementById("err_email").focus();hideSent();}
function hideError()
{document.getElementById("err_form").style.display="none";}
function hideSent()
{document.getElementById("err_sent").style.display="none";}
function sendErr()
{var xmlhttp;var err_url=document.getElementById("err_url").value;var err_email=document.getElementById("err_email").value;var err_desc=document.getElementById("err_desc").value;var csrfmiddlewaretoken=document.getElementsByName("csrfmiddlewaretoken")[0].value;if(window.XMLHttpRequest)
{xmlhttp=new XMLHttpRequest();}
else
{xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");}
xmlhttp.open("POST","/error_tutorial.py",true);xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");xmlhttp.setRequestHeader("X-CSRFToken",csrfmiddlewaretoken);xmlhttp.send("err_url="+err_url+"&err_email="+err_email+"&err_desc="+escape(err_desc));document.getElementById("err_desc").value="";hideError();document.getElementById("err_sent").style.display="block";}
function printPage(){content=document.getElementById("main_content").innerHTML;head=document.getElementsByTagName("head")[0].innerHTML;var myWindow=window.open('','','');myWindow.document.write("<html><head>"+head+"<style>body{padding:15px;}</style></head><body><button onclick='window.print()'>Print Page</button>"+content+"<center><p>文章来源：<a href='http://www.ziqiangxuetang.com'>自强学堂 在线教程</a></p></center></body></html>");}