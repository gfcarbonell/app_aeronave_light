var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;


class BotonDiagnosticar extends Backbone.View
{
	tagName() { return "input[type=button]"; }

	events()
	{
		return {
				"click #boton_diagnosticar"					  : "diagnosticar",
			   };
	}

	diagnosticar(e)
	{
		
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
