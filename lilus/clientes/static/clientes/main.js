$('.clienteNavPerfil').mouseover(function(){
		$('.overlay2').addClass('active');
});
$('.clienteNavPerfil').mouseout(function(){
		$('.overlay2').removeClass('active');
});


$('#activeLateral, .overlay1').click(function () {
	if($('.lateralNav').hasClass('active')){
		$('.lateralNav, .datosLegales, .overlay1, .menuPalo1, .menuPalo2, .menuPalo3').removeClass('active');
		$('html').css('overflow-y', 'scroll');
	}
	else{
		$('.lateralNav, .datosLegales, .overlay1, .menuPalo1, .menuPalo2, .menuPalo3').addClass('active');
		$('html').css('overflow-y', 'hidden');
	}
});




$(document).ready(function () {
	$('.agregar-favoritos').on('click', function () {
		// leemos los datos clave del producto y los guardamos en un objeto
		var datos = {
			id: $(this).attr('id'),
			url: document.getElementById($(this).attr('id')).value
		};
		// guardamos los favoritos en un JSON
		var favoritos = localStorage.getItem("favoritos") || "[]";
		favoritos = JSON.parse(favoritos);
		// buscamos el producto en la lista de favoritos
		var posLista = favoritos.findIndex(function(e) { return e.id == datos.id; });
		// eliminamos o guardamos
		if (posLista > -1) {
			favoritos.splice(posLista, 1);
		} else {
			favoritos.push(datos);
		}
		// guardamos la lista de favoritos
		localStorage.setItem("favoritos", JSON.stringify(favoritos));
	});

	colorearActivos()
	function colorearActivos(){
		// guardamos los favoritos en un JSON
		var favoritos = localStorage.getItem("favoritos") || "[]";
		favoritos = JSON.parse(favoritos);
		for (var x = 0; x < favoritos.length; x++) {
			$('#' + favoritos[x].id).addClass('activeFav');
			$('#' + favoritos[x].id).removeClass('desactiveFav');
		}
	}
});


$('.favoritosBotonAnadir').click(function () {
	if($(this).hasClass('desactiveFav')){
		$(this).addClass('activeFav');
		$(this).removeClass('desactiveFav');
	}
	else{
		$(this).removeClass('activeFav');
		$(this).addClass('desactiveFav');
	}
});