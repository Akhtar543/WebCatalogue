//store
window.addEventListener('load',store)
current=''
image=''

function store(){
	document.getElementById('divjew').style.display='none'
	document.getElementById('divshi').style.display='none'
	document.getElementById('divpan').style.display='none'
	document.getElementById('btnjew').addEventListener('click',jewelry)
	document.getElementById('btnshi').addEventListener('click',shirts)
	document.getElementById('btnpan').addEventListener('click',pants)
}
function jewelry(){
	current='divjew'
	document.getElementById('divjew').style.display='block'
	document.getElementById('divshi').style.display='none'
	document.getElementById('divpan').style.display='none'
}
function shirts(){
	current='divshi'
	document.getElementById('divshi').style.display='block'
	document.getElementById('divpan').style.display='none'
	document.getElementById('divjew').style.display='none'
}
function pants(){
	current='divpan'
	document.getElementById('divpan').style.display='block'
	document.getElementById('divjew').style.display='none'
	document.getElementById('divshi').style.display='none'
}