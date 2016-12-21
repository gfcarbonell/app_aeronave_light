var $ 		 	  			  = require("jquery");
var _        				  = require("underscore");
var Backbone 	  			  = require("backbone");
Backbone.$ = $;
var EmpleadoView		  	 = require("./empleado");
var Empleado 				 = require("../../models/empleado");
var Empleados 				 = require("../../collections/empleados");


class EmpleadosView extends Backbone.View 
{
	initialize()
	{
		this.listenTo(this.collection, "sync", this.render);
		this.get_tipos_empleados();
		this.empleados_nuevo = new Empleados();
		
	}

	get_tipos_empleados()
	{
		var id_tipos_empleados = [];
		var nombre_tipos_empleados = [];
		var self = this;
		this.collection.each(function(model){
			id_tipos_empleados.push(model.attributes.solucion.tipo_empleado.id);
			nombre_tipos_empleados.push(model.attributes.solucion.tipo_empleado.nombre);
		});

		var nombre_tipos_empleados_unicos = [];
		var nombre_tipos_empleados_unicos = nombre_tipos_empleados.filter(function(elem, pos) {
		   return nombre_tipos_empleados.indexOf(elem) == pos;
		});
		var id_tipos_empleados_unicos = [];
		var id_tipos_empleados_unicos = id_tipos_empleados.filter(function(elem, pos) {
		   return id_tipos_empleados.indexOf(elem) == pos;
		});

		$("#titulo_soluciones").html("");
		$("#titulo_soluciones").append("Solucion(es) | ");
		for (var i = nombre_tipos_empleados_unicos.length - 2; i >= 0; i--) {
			$("#titulo_soluciones").append("<i class='id_tipo_empleado' id="+ id_tipos_empleados_unicos[i]+">"+nombre_tipos_empleados_unicos[i] +"</i>, "); 
		};
		$("#titulo_soluciones").append("<i class='id_tipo_empleado' id="+ id_tipos_empleados_unicos[nombre_tipos_empleados_unicos.length - 1]+">"+(nombre_tipos_empleados_unicos[nombre_tipos_empleados_unicos.length - 1]) + "</i> |");



		console.log("Tipos empleado:" + id_tipos_empleados_unicos);
		this.get_array_empleados(id_tipos_empleados_unicos)
		.then(function(response){
			console.log(response);
			var empleados = new Empleados(response);
			self.empleados_nuevo = empleados;
			self.render();
		});
	}

	get_array_empleados(tipo_empleado)
	{
		var self = this;
		return new Promise(function(resolve, reject)
		{
			var empleado_array = [];
			var x = 0;
			console.log("tipos empleados:" + tipo_empleado.length);
			for (var i = 0; i < tipo_empleado.length; i++)
			{
				self.get_empleado_list(tipo_empleado[i])
				.then(function(response)
				{
					console.log("---------------------------");
					empleado_array = $.merge( empleado_array, response);

					if(x + 1 == tipo_empleado.length)
					{
						resolve(empleado_array);		
					}
					else{
						x++;
					}
				});
			}
		});
	}
	
	get_empleado_list(tipo_empleado)
	{
		var self = this;

		return new Promise(function(resolve, reject)
		{
			var empleado_array = [];
			self.get_empleado(tipo_empleado)			
			.then(function(response)
			{
				var empleado_json = $.parseJSON(response);
				for (var i = 0; i < empleado_json.length; i++) 
				{
					var empleado = new Empleado(empleado_json[i]);
					console.log("Empleado " + i + " | " + empleado.get("nombre"));
					empleado_array.push(empleado);
					if(empleado_json.length == i+1)
					{
						console.log("Tamaño Array:" + empleado_array.length);
						resolve(empleado_array);
					}
				};
			})
			
			;
		});
	}

	ajax_read(tipo_empleado){
		return new Promise(function(resolve, reject){
			$.ajax({
					url : "/mantenimiento/diagnostico/nuevo/?format=api&tipo_empleado="+ tipo_empleado,

					type: "GET",

					dataType: "text",

					data: {"tipo_empleado":tipo_empleado},

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

	get_empleado(tipo_empleado){
		var self = this;
		return new Promise(function(resolve, reject)
		{
			self.ajax_read(tipo_empleado)
			.then(function(response){
				resolve(response);
			});
		});
	}

	render()
	{
		//Crear Cache 
		var cache = document.createDocumentFragment();
		//Iterar objetos y pasando a la vista

		this.empleados_nuevo.each(function(model){
			var empleado = new EmpleadoView({model: model});
			cache.appendChild(empleado.render().el);
		});
		this.$el.append(cache);
	}
}

module.exports = EmpleadosView;