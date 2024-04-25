//////////////
// Javascript for Post Page 
//////////////

$(function( ){
    // Excute when js_menu-icon js clicked
    $('.js-option-icon').click(function() {
        /// $(This) - Self element , namely .div js-menu-icon
        /// .next() - Next to js .div js-menu-icon, namely div.menu
        /// .toogle() - Switch show and hide 
        $(this).next().toggle();
    })
})