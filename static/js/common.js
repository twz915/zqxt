function show_header(n)
{
	document.getElementById('headerdiv1').style.display='none';
	document.getElementById('headerdiv2').style.display='none';
	document.getElementById('headerdiv3').style.display='none';
	document.getElementById('arrowraquo1').style.background='';
	document.getElementById('arrowraquo2').style.background='';
	document.getElementById('arrowraquo3').style.background='';
	document.getElementById('arrowraquo1').style.color='#333333';
	document.getElementById('arrowraquo2').style.color='#333333';
	document.getElementById('arrowraquo3').style.color='#333333';
	document.getElementById('arrowhr1').style.background='#d4d4d4';
	document.getElementById('arrowhr2').style.background='#d4d4d4';
	document.getElementById('arrowhr3').style.background='#d4d4d4';
	document.getElementById('arrowraquo' + n).style.background='#ff4800';
	document.getElementById('arrowraquo'+ n).style.color='#ffffff';
	document.getElementById('arrowhr' + n).style.background='#ff4800';
	document.getElementById('headerdiv' + n).style.display='block';
}
