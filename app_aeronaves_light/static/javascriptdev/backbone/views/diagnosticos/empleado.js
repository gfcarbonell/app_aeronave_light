var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;


class Empleado extends Backbone.View
{
	tagName() { return "li"; }
	
    initialize() 
    {
    	this.template = _.template($("#empleado_template").html());
    	this.listenTo(this.model, "change", this.render, this);
 	}
 	
	render()
	{
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
}

module.exports = Empleado;
