$('.figure').on('click', function(){
	const input = $(this).find('input')
	const imageWidth = input.data('image-width')
	const imageHeight = input.data('image-height') 
	const image = $(this).find('img')
	const modal = $(".modal .modal-dialog")

	$('.dynamic_image').attr('src', image.attr('src'));
	$('.dynamic_title').text(input.data('title'));
	$('.dynamic_description').html(input.data('description'));
	if(parseInt(imageWidth,10)>500){
		modal.css("max-width", "62vw")
	}else{
		modal.css("max-width", "500px")
	}
})
