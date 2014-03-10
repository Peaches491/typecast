var wpcomment = document.getElementById('newContent');

wpcomment.onkeyup = function() {
	document.getElementById('newContent').innerHTML = this.value;

	var converter = new Markdown.Converter();
	Markdown.Extra.init(converter, {highlighter: "highlight"});
	document.getElementById('preview').innerHTML = converter.makeHtml(this.value);
}