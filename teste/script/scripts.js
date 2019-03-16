var oldValue = atributo.value;
var validateHasBeenCalled = false

function inserirLinha(){
			var table = document.getElementById("tabela");
			var linha = table.insertRow(-1);
			for (var i = 0; i < 6; i++) {
				var col = linha.insertCell(i);
				col.innerHTML = "teste";
			}
		}

function limparTexto(atributo){
	if(atributo.value == atributo.name){
		atributo.value = "";
	}
}

function resetarTexto(atributo){
	if(atributo.value == ""){
		atributo.value = atributo.name;
	}
}

function validarNumero(atributo){
	if(isNaN(atributo.value) == false){
		alert("Somente números, por favor.");
		var str = atributo.value;
		str = str.slice(0,-1);
		atributo.value = str;
		validateHasBeenCalled = true;
	}

}