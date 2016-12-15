var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;
var Solucion = require("../../models/solucion");
var Soluciones = require("../../collections/soluciones");
var SolucionesView = require("./soluciones");
var SolucionView = require("./solucion");
var EmpleadosView = require("./empleados");


class BotonDiagnosticar extends Backbone.View
{
	events()
	{
		return {
				"click #boton_diagnosticar"					  : "diagnosticar",
			   };
	}

	diagnosticar(e)
	{
		if (confirm("¿ Desea Diagnosticar?") == true) 
		{
		    var self = this;
			var averias = [];
			var tipos_profesores = [];
			$('.averias:checked').each(function() {
			    averias.push($(this).attr('id'));
			});

			if(averias.length < 1)
			{
				alert("Debe seleccionar al menos un tipo de averia");
			}
			else{
				this.get_soluciones(averias)
				.then(function(response){
					
					var soluciones_view;
					var empleados_view;
					console.log(response);
					if (soluciones_view instanceof SolucionesView)
					{
						soluciones_view.undelegateEvents();
					}
					else
					{
						$("#container_soluciones").html("");
						soluciones_view = new SolucionesView({el:$("#container_soluciones"), collection:response});
					}


					if (empleados_view instanceof EmpleadosView)
					{
						empleados_view.undelegateEvents();
					}
					else
					{
						$("#container_empleados").html("");
						empleados_view = new EmpleadosView({el:$("#container_empleados"), collection:response});
					}
					
				});
			}

		} else {

		    
		}
	}

	get_soluciones(averias){
		var self = this;
		return new Promise(function(resolve, reject)
		{
			var soluciones_collection;
			for (var i = 0; i < averias.length; i++) {
				self.get_solucion(averias[i])
				.then(function(data){
					
					if (soluciones_collection instanceof Soluciones)
					{
							//console.log("creado:" + data);
							soluciones_collection.push(data);
							if (soluciones_collection.length==averias.length)
							{
								resolve(soluciones_collection);
							}	
					}
					else{
						//console.log("Nuevo:" + data);
						soluciones_collection = new Soluciones();
						soluciones_collection.push(data);	
					}	
					
				});
			};
	
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

    initialize() 
    {
    	this.template = _.template($("#boton_diagnosticar_template").html());
    	this.listenTo(this.model, "change", this.render, this);
 	}
 	
	render()
	{
		this.$el.html(this.template());
		return this;
	}
}

module.exports = BotonDiagnosticar;
