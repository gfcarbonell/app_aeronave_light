var $ 		 	  			  = require("jquery");
var _        				  = require("underscore");
var Backbone 	  			  = require("backbone");
Backbone.$ = $;
var AveriaSolucion		  		  = require("./averia_solucion");


class AveriasSoluciones extends Backbone.View 
{
	initialize()
	{
		this.listenTo(this.collection, "sync", this.render);
		this.render();
	}

	render()
	{
		//Crear Cache 
		var cache = document.createDocumentFragment();
		//Iterar objetos y pasando a la vista
		this.collection.each(function(model){
			var averia_solucion = new AveriaSolucion({model: model});
			cache.appendChild(averia_solucion.render().el);
		});

		this.$el.append(cache);
	}
}

module.exports = AveriasSoluciones;