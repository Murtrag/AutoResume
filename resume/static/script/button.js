function toggleClassHover(el){
$(el.target.parentElement.firstElementChild).toggleClass('svg-button-hover-bg');
let thisElParent = $(this).parent()
thisElParent.toggleClass('svg-button-hover-bold')
// thisElParent.first().toggleClass('svg-button-hover-bg')
// thisElParent.filter('path').toggleClass('svg-button-hover-bg')
}
$(".svg-button a").mouseover(toggleClassHover ).mouseout(toggleClassHover)
