var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");
Backbone.$ = $
var Solucion = require("../models/solucion");


class Soluciones extends Backbone.Collection
{
	initialize()
	{
		this.model = Solucion; 
	}
}

module.exports = Soluciones;