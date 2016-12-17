var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;
var Catalogo 				 = require("../../models/catalogo");
var Catalogos 				 = require("../../collections/catalogos");

var csrftoken = getCookie('csrftoken');

var router = new Backbone.Router();

function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

// usando jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = $.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function csrfSafeMethod(method) {
    // estos métodos no requieren CSRF
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

class BotonSubmit extends Backbone.View
{
    initialize() 
    {
    	this.template = _.template($("#boton_submit_template").html());
    	this.listenTo(this.model, "change", this.render, this);
 	}

 	events()
	{
		return {
				"click #boton_submit"					  : "post_view",
			   };
	}

	post_view(e)
	{
		e.preventDefault();
		var self = this;
		var id_aeronave = $("#aeronaves").val();
		var id_averias = [];
		var fecha_diagnostico = $("#date_diagnostico").val();
		$('.averias:checked').each(function() {
		    id_averias.push($(this).attr('id'));
		});
		var id_empleado = $("input:radio[name='especialistas']:checked").val();
		if(id_aeronave!=0)
		{
			if(id_averias.length>0){
				if(id_empleado!=undefined)
				{
					if(fecha_diagnostico!=undefined)
					{
						var x = 0;
						for (var i = id_averias.length - 1; i >= 0; i--) {
							this.get_catalogo(id_aeronave, id_averias[i])
							.then(function(response)
							{
								var csrftoken = csrftoken;
								//var csrftoken = $('meta[name="csrfmiddlewaretoken"]').val();
								//var csrftoken = getCookie('csrftoken');
								
								var seleccionar = true;
								var objeto = {
									"csrfmiddlewaretoken":getCookie('csrftoken'),
									"catalogo_aeronave_parte_averia":$.parseJSON(response)[0].id,
									"empleado":id_empleado,
									"fecha_diagnostico":fecha_diagnostico,
									"seleccionar":seleccionar
								}
								console.log("-----------");
								
								x++;
								console.log("x:" + x);
								console.log(JSON.stringify(objeto));
								self.ajax_post(JSON.stringify(objeto))
								.then(function(response){
									
								});
							})
							.then(function(response)
							{
								if(id_averias.length == x){
									console.log("entre");
									window.location.href = "/mantenimiento/diagnosticos/";
								}
							});
						};
					}
					else{
						alert("Debe seleccionar la fecha de diagnostico");
					}
				}
				else
				{
					alert("Debe seleccionar un tipo de especilista");
				}
			}
			else{
				alert("Debe seleccionar al menos una averia");
			}
		}
		else{
			alert("Debe seleccionar un tipo de aeronave");
		}
	}

	get_catalogo(aeronave, averia){
		var self = this;
		return new Promise(function(resolve, reject)
		{
			self.ajax_read(aeronave, averia)
			.then(function(response){
				resolve(response);
			});
		});
	}

	ajax_read(aeronave, averia){
		return new Promise(function(resolve, reject){
			$.ajax({
					url : "/mantenimiento/diagnostico/nuevo/?format=api&aeronave="+aeronave+"&averia="+averia,

					type: "GET",

					dataType: "text",

					data: {"aeronave":aeronave, "averia":averia},

					async: true,

					success: function(data){
						resolve(data);
					},

					error: function (data, textStatus, jqXHR) {
		                var errors = $.parseJSON(data.responseText);
		                console.log(xhr.status + ": " + xhr.responseText);
		                alert(data.responseText);
				    }

			});
		});
	}

	ajax_post(json){
		return new Promise(function(resolve, reject){

			//Agregamos en la configuración de la funcion $.ajax de Jquery lo siguiente:
			$.ajaxSetup({
			                beforeSend: function(xhr, settings) {
			                    if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
			                        // Send the token to same-origin, relative URLs only.
			                        // Send the token only if the method warrants CSRF protection
			                        // Using the CSRFToken value acquired earlier
			                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
			                    }
			                }
			});

			$.ajax({
					url : "/mantenimiento/diagnostico/create/",

					type: "POST",

					dataType: "json",
					contentType: 'application/json; charset=utf-8',
					data: json,

					async: true,

					success: function(data){
						resolve(data);
					},

					error: function (data, textStatus, jqXHR) {
		                var errors = $.parseJSON(data.responseText);
		                console.log(xhr.status + ": " + xhr.responseText);
		                alert(data.responseText);
				    }

			});
		});
	}
	render()
	{
		this.$el.html(this.template());
		return this;
	}
}

module.exports = BotonSubmit;