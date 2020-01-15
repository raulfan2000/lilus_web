$(window).scroll(function(){
	if ($(this).scrollTop() > 77 && screen.width > 900){
		$('#menu').addClass("menuVisible");
		$('#nav').addClass("navegadorDivScroll");
		$('#nav').addClass("fixed-top");
		$('#fondo').addClass("marginScroll");
		$('#activeBusquedaScroll, .fa-globe-europe, .idiomaDiv, .fa-caret-down, .facebookLink, .logoPeque').addClass("active");
	}
	else {
		$('#menu').removeClass("menuVisible");
		$('#nav').removeClass("navegadorDivScroll");
		$('#nav').removeClass("fixed-top");
		$('#fondo').removeClass("marginScroll");
		$('#activeBusquedaScroll, .fa-globe-europe, .idiomaDiv, .fa-caret-down, .facebookLink, .logoPeque').removeClass("active");
	}
});

$('#ponerMenu').click(function () {
	if($('#sidebar').hasClass('active')){
		$('#sidebar, .menuPalo1, .menuPalo2, .menuPalo3').removeClass('active');
		$('html,body').css('overflow', 'scroll');
	}
	else{
		$('#sidebar, .menuPalo1, .menuPalo2, .menuPalo3').addClass('active');
		$('html,body').css('overflow', 'hidden');
	}
});

$(document).ready(function () {
	$('#activarBuscadorMovil, #activarBuscador').on('click', function () {
			$('#buscadorMovil, .overlay').addClass('active');
			$('html,body').css('overflow', 'hidden');
			$('#inputBuscador').focus();
	});
	$('#cerrarBuscadorMovil, .overlay').on('click', function () {
			$('#buscadorMovil, .overlay').removeClass('active');
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


$('#idiomaSelector').change(function(){
	document.forms["submitIdioma"].submit();
});


$('#m2, #m3, #m4').mouseover(function(){
		$('.overlay2').addClass('active');
});
$('#m2, #m3, #m4').mouseout(function(){
		$('.overlay2').removeClass('active');
});


if (localStorage.controlcookie > 0){
	document.getElementById('cookie1').style.display = 'none';
}
function controlcookies() {
	localStorage.controlcookie = (localStorage.controlcookie || 0);
	localStorage.controlcookie++;
	cookie1.style.display='none';
}
