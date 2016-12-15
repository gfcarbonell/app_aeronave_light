var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");
Backbone.$ = $;

//Boton de menu de navegacion
var BotonUsuarioDato = require("../views/boton_usuario_dato");
var BotonCloseMenu = require("../views/boton_close_menu");
var BotonOpenMenu  = require("../views/boton_open_menu");


//Empleado | Especialista
var PanelMenuEmpleado  = require("../views/empleados/panel_menu_empleado");
var FotografiaEmpleado         = require("../views/empleados/file_imagen_fotografia");
//Piloto
var PanelMenuPiloto  = require("../views/pilotos/panel_menu_piloto");

var SearchBox                          = require("../views/search_box");
var Fotografia                         = require("../views/file_imagen_fotografia");
var DocumentoIdentificacion            = require("../views/select_documento_identificacion");
var NumeroDocumentoIdentificacion      = require("../views/input_numero_documento_identificacion");

var AveriasSoluciones = require("../views/diagnosticos/averias_soluciones");
var Diagnosticar = require("../views/diagnosticos/diagnosticar");
var BotonDiagnosticar = require("../views/diagnosticos/boton_diagnosticar");
var BotonSubmit = require("../views/diagnosticos/boton_submit");


class Router extends Backbone.Router
{
    initialize () {
        this._bindRoutes();
        var boton_usuario_dato = new BotonUsuarioDato({el:$("#boton_usuario_dato_container")});
        var boton_open_menu = new BotonOpenMenu({el: $("#boton_open_menu_container")})
        var boton_close_menu = new BotonCloseMenu({el: $("#boton_close_menu_container")})
    }

    routes ()
    {
        return {
            "mantenimiento/aeronaves/"                              : "aeronaves",
            "mantenimiento/aeronave/nuevo/"                         : "aeronave_nuevo",
            "mantenimiento/aeronave/:aeronave/modificar/"           : "aeronave_modificar",
            "mantenimiento/pilotos/"                                : "pilotos",
            "mantenimiento/piloto/nuevo/"                           : "piloto_nuevo",
            "mantenimiento/piloto/:piloto/modificar/"               : "piloto_modificar",

            "mantenimiento/especialistas/"                                : "especialistas",
            "mantenimiento/especialista/nuevo/"                           : "especialista_nuevo",
            "mantenimiento/especialista/:especialista/modificar/"         : "especialista_modificar",
            
            "mantenimiento/diagnostico/nuevo/"                                : "diagnostico_nuevo",

            "mantenimiento/ordenes-de-vuelos/"                                : "ordenes_vuelos",
            };
    }

    aeronaves()
    {
        var search_empleado = new SearchBox({el:$("#container_search_registro") });
    }
    aeronave_nuevo()
    {
        var panel_menu_empleado = new PanelMenuEmpleado({el:$("#panel_menu")});
        var fotografia = new Fotografia({el:$("#container_fotografia")});
    }
    aeronave_modificar(aeronave)
    {
        var panel_menu_empleado = new PanelMenuEmpleado({el:$("#panel_menu")});
        var fotografia = new Fotografia({el:$("#container_fotografia")});
    }

    pilotos()
    {
        var search_piloto = new SearchBox({el:$("#container_search_registro") });
    }
    piloto_nuevo()
    {
        var panel_menu_piloto                = new PanelMenuPiloto({el:$("#panel_menu")});
        var Fotografia                       = new Fotografia({el:$("#container_fotografia")});
    }

    piloto_modificar(piloto)
    {
        var panel_menu_piloto = new PanelMenuPiloto({el:$("#panel_menu")});
        var fotografia = new Fotografia({el:$("#container_fotografia")});
    }

    especialistas()
    {
        var search_empleado = new SearchBox({el:$("#container_search_registro") });
    }
    especialista_nuevo()
    {
        var panel_menu_empleado = new PanelMenuEmpleado({el:$("#panel_menu")});
        var fotografia = new FotografiaEmpleado({el:$("#container_fotografia")});
    }
    especialista_modificar(especialista)
    {
        var panel_menu_empleado = new PanelMenuEmpleado({el:$("#panel_menu")});
        var fotografia = new FotografiaEmpleado({el:$("#container_fotografia")});
    }

    diagnostico_nuevo()
    {
        var diagnosticar = new Diagnosticar({el:$("#container_aeronaves")});
        var button        = new BotonDiagnosticar({el:$("#container_boton_diagnosticar")});
        var button_submit = new BotonSubmit({el:$("#container_submit")});
        button_submit.render();
        button.render();
    }
    ordenes_vuelos()
    {
        var search_orden_vuelo = new SearchBox({el:$("#container_search_registro") });
    }
 }

module.exports = Router;
