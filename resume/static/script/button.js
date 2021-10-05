function toggleClassHover(el){
$(el.target.parentElement.firstElementChild).toggleClass('svg-button-hover');
}
$(".svg-button a").mouseover(toggleClassHover ).mouseout(toggleClassHover)
