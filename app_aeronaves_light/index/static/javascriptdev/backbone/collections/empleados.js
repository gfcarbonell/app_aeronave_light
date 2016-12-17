var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");
Backbone.$ = $
var Empleado = require("../models/empleado");


class Empleados extends Backbone.Collection
{
	initialize()
	{
		this.model = Empleado; 
	}
}

module.exports = Empleados;