var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;


class PanelMenuPiloto extends Backbone.View
{

	initialize()
	{
		this.template = _.template($("#panel_menu_template").html());
		this.render();
	}

	events()
	{
		return {
				"click #menu_personales" 		  : "show_personales",
				"click #menu_domicilio" 		  : "show_domicilio",
        		"click #menu_piloto" 		      : "show_piloto",
			   };
	}

	show_personales(e)
	{
		e.preventDefault();
		$("#panel_personales").show();
		$("#menu_personales").addClass("color-black").parent().addClass("background-white");

		$("#panel_piloto").hide();
		$("#menu_piloto").removeClass("color-black").parent().removeClass("background-white");

   		$("#panel_domicilio").hide();
    	$("#menu_domicilio").removeClass("color-black").parent().removeClass("background-white");
	}

	show_domicilio(e)
	{
		e.preventDefault();
		$("#panel_domicilio").show();
		$("#menu_domicilio").addClass("color-black").parent().addClass("background-white");;

		$("#panel_personales").hide();
		$("#menu_personales").removeClass("color-black").parent().removeClass("background-white");

  	   $("#panel_piloto").hide();
       $("#menu_piloto").removeClass("color-black").parent().removeClass("background-white");
	}

  show_piloto(e)
	{
		e.preventDefault();
		$("#panel_piloto").show();
		$("#panel_piloto").addClass("color-black").parent().addClass("background-white");;

		$("#panel_personales").hide();
		$("#menu_personales").removeClass("color-black").parent().removeClass("background-white");

        $("#panel_domicilio").hide();
        $("#menu_domicilio").removeClass("color-black").parent().removeClass("background-white");
	}

    render()
	{
        this.$el.html(this.template());
		return this;
    }

}

module.exports = PanelMenuPiloto;
