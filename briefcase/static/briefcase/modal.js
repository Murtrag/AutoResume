$('.figure').on('click', function(){
	const input = $(this).find('input')
	const imageWidth = input.data('image-width')
	const imageHeight = input.data('image-height') 
	const image = $(this).find('img')
	const modal = $(".modal .modal-dialog")

	$('.dynamic_image').attr('src', image.attr('src'));
	$('.dynamic_title').text(input.data('title'));
	$('.dynamic_description').html(input.data('description'));
	// $('.dynamic_url').text(input.data('url'));
	$('.dynamic_image').css({
		"height": imageHeight+"px",
		"width": imageWidth+"px"
	});
	if(parseInt(imageWidth,10)>500){
		modal.css("max-width", imageWidth+578+"px")
	}else{
		modal.css("max-width", "500px")
	}
})
