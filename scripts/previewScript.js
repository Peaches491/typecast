var wpcomment = document.getElementById('newContent');

wpcomment.onkeyup = function(){
    document.getElementById('newContent').innerHTML = this.value;
    var content = document.createTextNode(this.value);
    document.getElementById('preview').innerHTML = this.value;
}