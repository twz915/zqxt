;(function ($, window, undefined) {
  'use strict';

  var $doc = $(document),
      Modernizr = window.Modernizr;

  
  $.fn.foundationAlerts           ? $doc.foundationAlerts() : null;
  $.fn.foundationAccordion        ? $doc.foundationAccordion() : null;
  $.fn.foundationTooltips         ? $doc.foundationTooltips() : null;
  $('input, textarea').placeholder();
  
  
  $.fn.foundationButtons          ? $doc.foundationButtons() : null;
  
  
  
  $.fn.foundationCustomForms      ? $doc.foundationCustomForms() : null;
  $.fn.foundationMediaQueryViewer ? $doc.foundationMediaQueryViewer() : null;
  
  

  // UNCOMMENT THE LINE YOU WANT BELOW IF YOU WANT IE8 SUPPORT AND ARE USING .block-grids
  // $('.block-grid.two-up>li:nth-child(2n+1)').css({clear: 'both'});
  // $('.block-grid.three-up>li:nth-child(3n+1)').css({clear: 'both'});
  // $('.block-grid.four-up>li:nth-child(4n+1)').css({clear: 'both'});
  // $('.block-grid.five-up>li:nth-child(5n+1)').css({clear: 'both'});

  // Hide address bar on mobile devices
  if (Modernizr.touch) {
    $(window).load(function () {
      setTimeout(function () {
        window.scrollTo(0, 1);
      }, 0);
    });
  }
  
})(jQuery, this);

function colorToHex(color) {    
    var rgb = blue | (green << 8) | (red << 16);
    return '#' + rgb.toString(16);
};

function resizeMe()
{                                       
    var th = $('#titleRow').height();
    var ch = $('#colorsRow').height();   
    var rh = $('#resultRow').height();
    var wh = $(window).height();
    var total = th + ch + rh;
                    
    var dif;
    if( total < wh)
        dif = (wh - total) / 5;
    else
        dif = 15;
                          
    if( dif < 0)
        dif = 0;
    $('#titleRow, #colorsRow, #resultRow').css('marginTop', dif + 'px'); 
    
}

function componentToHex(c) {
    var hex = c.toString(16);
    return hex.length == 1 ? "0" + hex : hex;
}

function rgbToHex(r, g, b) {
    return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}

$(function(){
    $('.colorBox').keydown(function(event){
        // Allow: backspace, delete, tab, escape, and enter
        if ( event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9 || event.keyCode == 27 || event.keyCode == 13 || 
             // Allow: Ctrl+A
            (event.keyCode == 65 && event.ctrlKey === true) || 
             // Allow: home, end, left, right
            (event.keyCode >= 35 && event.keyCode <= 39)) {
                 // let it happen, don't do anything
                 return;
        }
        else 
        {
            // Ensure that it is a number and stop the keypress
            if (event.shiftKey || (event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105 )) {
                event.preventDefault(); 
            }   
            
            
            
        } 
    });
    
    $('.colorBox').keyup(function(){
        var r = parseInt($('#colorR').val());
        var g = parseInt($('#colorG').val());
        var b = parseInt($('#colorB').val());
        r = (r ? (r < 0 ? 0 : (r > 255 ? 255 : r)) : 0);
        g = (g ? (g < 0 ? 0 : (g > 255 ? 255 : g)) : 0);
        b = (b ? (b < 0 ? 0 : (b > 255 ? 255 : b)) : 0);                                                           
                                               
        var msg = rgbToHex(r,g,b);     
        $('.resultBox').animate({backgroundColor : msg});        
        $('.resultHex').text(msg );
    });
    $('.colorBox').blur(function(){
        if( $(this).val().length == 0) 
        {
            $(this).val('0');    
        }
        $(this).keyup(); 
    });
    $('.colorBox').focus(function(){    
        $(this).select();
    });   
    $('.colorBox').mouseup(function(e){ // fix for chrome and safari
        e.preventDefault();
    });
    resizeMe();
});

$(window).resize(resizeMe);
