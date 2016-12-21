var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");
Backbone.$ = $
var Catalogo = require("../models/catalogo");


class Catalogos extends Backbone.Collection
{
	initialize()
	{
		this.model = Catalogo; 
	}
}

module.exports = Catalogos;