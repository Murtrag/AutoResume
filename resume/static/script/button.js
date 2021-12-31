function toggleClassHover(el){
$(el.target.parentElement.firstElementChild).toggleClass('svg-button-hover-bg');
let thisElParent = $(this).parent()
thisElParent.toggleClass('svg-button-hover-bold')
}
$(".svg-button a").mouseover(toggleClassHover ).mouseout(toggleClassHover)
