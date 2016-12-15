/**
 * Este script de javascript permite trabajar transparentemente solicitudes que requieren 
 * protección del token CSRF por medio de AJAX JQUERY.
 * Esto te permitirá hacer solcitudes a web Services de Django por medio de AJAX Jquery.
 * Para utilizarlo basta con integrar el archivo DjangoAjax.js en tu directorio de JS  y hacer referencia a él en tus templates 
 * que requieren del uso de AJAX por POST o algún otro que requiera el token CSRF.
 * Este script está basado en la documentación oficial de Django https://docs.djangoproject.com
 */

$(function(){
    //Obtenemos la información de csfrtoken que se almacena por cookies en el cliente

});