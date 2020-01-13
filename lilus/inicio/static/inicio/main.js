$(window).scroll(function(){
	if ($(this).scrollTop() > 69 && screen.width > 900){
		$('#menu').addClass("menuVisible");
		$('#nav').addClass("navegadorDivScroll");
		$('#nav').addClass("fixed-top");
		$('#fondo').addClass("marginScroll");
		$('#activeBusquedaScroll').addClass("active");
	}
	else {
		$('#menu').removeClass("menuVisible");
		$('#nav').removeClass("navegadorDivScroll");
		$('#nav').removeClass("fixed-top");
		$('#fondo').removeClass("marginScroll");
		$('#activeBusquedaScroll').removeClass("active");
	}
});

$(document).click(function () {
	if($('#sidebar').hasClass('active')){
		$('#ponerMenu').on('click', function () {
				$('#sidebar').removeClass('active');
				$('.menuPalo1').removeClass('active');
				$('.menuPalo2').removeClass('active');
				$('.menuPalo3').removeClass('active');
				$('html,body').css('overflow', 'scroll');
		});
	}
	else{
		$('#ponerMenu').on('click', function () {
				$('#sidebar').addClass('active');
				$('.menuPalo1').addClass('active');
				$('.menuPalo2').addClass('active');
				$('.menuPalo3').addClass('active');
				$('html,body').css('overflow', 'hidden');
		});
	}
});

$(document).ready(function () {
	$('#activarBuscadorMovil, #activarBuscador').on('click', function () {
			$('#buscadorMovil').addClass('active');
			$('.overlay').addClass('active');
			$('html,body').css('overflow', 'hidden');
			$('#inputBuscador').focus();
	});

	$('#cerrarBuscadorMovil, .overlay').on('click', function () {
			$('#buscadorMovil').removeClass('active');
			$('.overlay').removeClass('active');
			$('html,body').css('overflow', 'scroll');
	});



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

$('.activeFav').click(function () {
	$(this).removeClass('activeFav');
	$(this).addClass('desactiveFav');
});
