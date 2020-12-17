$('.figure').on('click', function(){
	const image = $(this).find('img')
	const modal = $(".modal .modal-dialog")
	const inputData = $(this).find('input').data()
	const imageWidth = inputData['image-width']
	const imageHeight = inputData['image-height'] 
	$('.dynamic_title').text(inputData['title']);

	const carouselInner = $('.carousel-inner').empty();
	const carouselIndicators = $('.carousel-indicators').empty();
	$(this).find(".modal_img").each(function(i,e){
		const active = (i==0)? 'active':'';
		carouselInner.prepend(`
			<div class="carousel-item ${active}">
				<img class="d-block w-100 dynamic_image" src="${e.src}" alt="First slide">
				<div class="carousel-caption d-none d-md-block">
					<h5 style="color:${$(e).data('color')}">${$(e).data('name')}</h5>
					<p style="color:${$(e).data('color')}">${$(e).data('description')}</p>
				</div>
			</div>

			`)
		carouselIndicators.prepend(`
		<li data-target="#carouselExampleIndicators" data-slide-to="${i}" class="${active}"></li>
			`);

		if(modal.hasClass('modal-wider') == false){ 
			if(e.width>500){
				modal.addClass("modal-wider")
			}else{
				modal.removeClass("modal-wider")
			}
		}
	})
})
$("#zoom").on('click', function(){
	$('body').toggleClass('body-zoomed')
	// var viewport = document.querySelector('meta[name="viewport"]');
	let span = $('span', this)
	console.log(span.text()=="dupa")
	if (span.text()=="in"){ 
		span.html("out")
		// clientWidthZoomed = document.body.clientWidth * .5
		// console.log(clientWidthZoomed )
		// viewport.content = `width=${clientWidthZoomed}`;
		}
	else{
		span.html("in")
		// viewport.content = "width=device-width";
		}
	}
)

