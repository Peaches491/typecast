var wpcomment = document.getElementById('newContent');

wpcomment.onkeyup = function(){
    document.getElementById('newContent').innerHTML = this.value;
    

    
//    var content = document.createTextNode(this.value);
    
//    var marked = require('marked');
//    marked.setOptions({
//    	  renderer: new marked.Renderer(),
//    	  gfm: true,
//    	  tables: true,
//    	  breaks: false,
//    	  pedantic: false,
//    	  sanitize: true,
//    	  smartLists: true,
//    	  smartypants: false
//    	});
    
//    marked.setOptions({
//    	  highlight: function (code, lang, callback) {
//    	    require('pygmentize-bundled')({ lang: lang, format: 'html' }, code, function (err, result) {
//    	      callback(err, result.toString());
//    	    });
//    	  }
//    	});
    
    document.getElementById('preview').innerHTML = this.value;
//    marked('I am using __markdown__.');
    
}