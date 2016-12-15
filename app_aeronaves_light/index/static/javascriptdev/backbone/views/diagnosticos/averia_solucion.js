var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;
var Solucion = require("../../models/solucion");
var Soluciones = require("../../collections/soluciones");
var SolucionesView = require("./soluciones");
var SolucionView = require("./solucion");




class AveriaSolucion extends Backbone.View
{
	tagName() { return "li"; }
	className(){return "card-panel container";}

	events()
	{

	}

	checked_averia(e)
	{
		var self = this;
		var averias = [];
		$('.averias:checked').each(function() {
		    averias.push($(this).attr('id'));
		});

		this.get_soluciones(averias)
		.then(function(response){
			console.log(response);
			var soluciones_view;
			
			if (soluciones_view instanceof SolucionesView)
			{
				soluciones_view.undelegateEvents();
			}
			else
			{
				$("#container_soluciones").html("");
				soluciones_view = new SolucionesView({el:$("#container_soluciones"), collection:response});
			}
			
		});
		
	}

	ajax_read(averia){
		return new Promise(function(resolve, reject){
			$.ajax({
					url : "/mantenimiento/diagnostico/nuevo/?format=api&averia="+ averia,

					type: "GET",

					dataType: "text",

					data: {"averia":averia},

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

	get_solucion(averia){
		var self = this;
		return new Promise(function(resolve, reject)
		{
			self.ajax_read(averia)
			.then(function(response){
				var solucion_json = $.parseJSON(response);
				var solucion = new Solucion(solucion_json[0]);
				resolve(solucion);
			});
		});
	}

	get_soluciones(averias){
		var self = this;
		return new Promise(function(resolve, reject)
		{
			var soluciones = [];
			var soluciones_collection;
			var x = 0;
			for (var i = 0; i < averias.length; i++) {
				self.get_solucion(averias[i])
				.then(function(data){
					
					if (soluciones_collection instanceof Soluciones)
					{
							//console.log("creado:" + data);
							soluciones_collection.add(data);
							if (x+1==averias.length)
							{
								resolve(soluciones_collection);
							}
							else{
								x++;
							}
					}
					else{
						//console.log("Nuevo:" + data);
						soluciones_collection = new Soluciones();
						soluciones_collection.add(data);	
						console.log(data);
					}	
					
				});
			};
	
		});
	}

    initialize() 
    {
    	this.template = _.template($("#averia_solucion_template").html());
    	this.listenTo(this.model, "change", this.render, this);
 	}
 	
	render()
	{
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
}

module.exports = AveriaSolucion;
