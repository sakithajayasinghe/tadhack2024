$(document).ready(function() {
    /* Click on X button clears the numbers typed */
    $("div.remover").click(function() {
      $('#number').val("");
    });
    /* Dial pad input*/
         $(".dialer1").click(function() {
           $('#number').val($('#number').val() + '1');
         });
         $(".dialer2").click(function() {
           $('#number').val($('#number').val() + '2');
         });
         $(".dialer3").click(function() {
           $('#number').val($('#number').val() + '3');
         });
         $(".dialer4").click(function() {
           $('#number').val($('#number').val() + '4');
         });
         $(".dialer5").click(function() {
           $('#number').val($('#number').val() + '5');
         });
         $(".dialer6").click(function() {
           $('#number').val($('#number').val() + '6');
         });
         $(".dialer7").click(function() {
           $('#number').val($('#number').val() + '7');
         });
         $(".dialer8").click(function() {
           $('#number').val($('#number').val() + '8');
         });
         $(".dialer9").click(function() {
           $('#number').val($('#number').val() + '9');
         });
         $(".dialer0").click(function() {
           $('#number').val($('#number').val() + '0');
         });
         $(".dialerAst").click(function() {
           $('#number').val($('#number').val() + '*');
         });
         $(".dialerHash").click(function() {
           $('#number').val($('#number').val() + '#');
         });
    $(".home-button").click(function() {
        $(".homescreen").toggle(); /* toggle deprecated */
    });
    $(".call-button").click(function() {
        $(".callscreen").addClass("callscreen-transition").css("-webkit-transform", "scale(1.3, 1.3)");
        $(".callscreen").toggle(); /* toggle deprecated */
        $(".callscreen-container").toggle();
        $(".dialer-app-container").toggle(); 
        $(".status-bar, .fa-signal").css("color", "white"); 
    });
    $(".end-call-button").click(function() {
      $(".callscreen-container").toggle();
      $(".dialer-app-container").toggle(); 
      $(".callscreen").toggle();
      $(".status-bar, .fa-signal").css("color", "black"); 
    });
  });