var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;
var AveriasSoluciones = require("./averias_soluciones");

var averias_soluciones;
var cat;

var Catalogos = require("../../collections/catalogos");


class Diagnosticar extends Backbone.View
{

	initialize()
	{
		this.template = _.template($("#aeronaves_template").html());
		this.render();
	}
	events()
	{
		return {
				"change #aeronaves"					  : "select_aeronave",
			   };
	}
	select_aeronave(e)
	{
		e.preventDefault();
		var aeronave = $( "#aeronaves" ).val();

		var aeronaves = $.ajax({
					url : "/mantenimiento/diagnostico/nuevo/?format=api&aeronave="+ aeronave,

					type: "GET",

					dataType: "text",

					data: {"aeronaves":aeronave},

					async: true,

					success: function(data){
						var catalogo = JSON.parse(data);
						cat = new Catalogos(catalogo);

						if (averias_soluciones != undefined)
						{
							averias_soluciones.undelegateEvents();
						}
						$("#averias_soluciones").html("");
						averias_soluciones = new AveriasSoluciones({el:$("#averias_soluciones"), collection:cat});
			
					},

					error: function (data, textStatus, jqXHR) {
		                var errors = $.parseJSON(data.responseText);
		                console.log(xhr.status + ": " + xhr.responseText);
		                alert(data.responseText);
				    }

				});
		return false;
	}
  	render()
	{
			this.$el.html(this.template());
		 	return this;
  	}

}

module.exports = Diagnosticar;
