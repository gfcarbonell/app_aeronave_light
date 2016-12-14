var $ 		 	  			  = require("jquery");
var _        				  = require("underscore");
var Backbone 	  			  = require("backbone");
Backbone.$ = $;
var Solucion		  		  = require("./solucion");


class Soluciones extends Backbone.View 
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
			var solucion = new Solucion({model: model});
			cache.appendChild(solucion.render().el);
		});
		this.$el.append(cache);
	}
}

module.exports = Soluciones;