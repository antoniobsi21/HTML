var pattern = [10, "", "", "", 0, 0];

function inserirLinha(){
	var table = document.getElementById("tabela");
	var linha = table.insertRow(-1);
	posicionarDados();
	var col = linha.insertCell(0);
	col.innerHTML = pattern[0];
	col.id = "pos" + pattern[0];
	for (var i = 1; i < 6; i++) {
		var col = linha.insertCell(i);
		col.innerHTML = pattern[i];
	}
}


function posicionarDados(){
	var pos = ((document.getElementById('pos' + (pattern[0]*1)).innerHTML)*1)+1;
	console.log(pos);
	pattern[0] = pos;
	console.log(pattern);
	for (var j = 1; j < 5; j++){
		pattern[j] = document.getElementById('a'+j).value;
	}
	pattern[5] = Math.round(((pattern[3] / pattern[4]) * 100000)*100)/100;
}

function limparTexto(atributo){
	if(atributo.value == atributo.name){
		atributo.value = "";
	}
}

function resetarTexto(atributo){
	if(atributo.value == ""){
		atributo.value = atributo.name;
	} else if (atributo.name){

	}
}
/* NÃO FUNCIONA
function validarNumero(atributo){
	if(isNaN(atributo.value) == false){
		alert("Somente números, por favor.");
		var str = atributo.value;
		str = str.slice(0,-1);
		atributo.value = str;
	}

}*/