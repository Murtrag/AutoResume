$('.figure').on('click', function(){
	const image = $(this).find('img')
	const modal = $(".modal .modal-dialog")
	const inputData = $(this).find('input').data()
	// const imageWidth = inputData['image-width']
	// const imageHeight = inputData['image-height'] 
	$('.dynamic_title').text(inputData['title']);
	let imageToZoom = image[0].src

	const carouselInner = $('.carousel-inner').empty();
	const carouselIndicators = $('.carousel-indicators').empty();

	$(this).find(".modal_img").each(function(i,e){
		const active = (i==0)? 'active':'';
		carouselInner.prepend(`
			<div class="carousel-item ${active}">
				<img class="d-block w-100 dynamic_image" src="${e.src}" alt="First slide">
				<div class="carousel-caption d-md-block">
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

	$('#ImageCarousels').bind('slide.bs.carousel', function (e) {
	setTimeout(()=>{
	imageToZoom = $('#ImageCarousels .active img')[0].src
	console.log(imageToZoom);
	}, 900)
});
	$("#zoom").on('click', function () {
		$('#zoom').html()
		window.location.href = imageToZoom;
	}
)

})

