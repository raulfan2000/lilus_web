$(window).scroll(function(){
	if ($(this).scrollTop() > 60 && screen.width > 900){
		$('#menu').addClass("menuVisible");
		$('#nav').addClass("navegadorDivScroll");
		$('#nav').addClass("fixed-top");
		$('#fondo').addClass("marginScroll");
	}
	else {
		$('#menu').removeClass("menuVisible");
		$('#nav').removeClass("navegadorDivScroll");
		$('#nav').removeClass("fixed-top");
		$('#fondo').removeClass("marginScroll");
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
});
