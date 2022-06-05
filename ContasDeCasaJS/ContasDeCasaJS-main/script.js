var numluz = document.getElementById('numluz')
var numagua = document.getElementById('numagua')
var numnet = document.getElementById('numnet')
var numiptu = document.getElementById('numiptu')

function somar(){
    var luz = Number(numluz.value)
    var agua = Number(numagua.value)
    var net = Number(numnet.value)
    var iptu = Number(numiptu.value)
    var res = document.getElementById('res')

    var div1 = ((luz/3)+(agua/4)+(net/3)+(iptu/4))
    var div2 = ((agua/4)+(iptu/4))
    var tot = (luz+agua+net+iptu)

    if (numluz.value.length == 0 || numagua.value.length == 0 || numnet.value.length == 0 || numiptu.value.length == 0){
        alert('[ERRO] Falta dados!')
    }else{
        if (tot > 550+div2){
            res.innerHTML = `
            <p>Luzirene: R$${div1.toFixed(2)}</p>
            <p>Gabriel: R$${div1.toFixed(2)}</p>
            <p>Paloma: R$${div1.toFixed(2)}</p>
            <p>Juliana: R$${div2.toFixed(2)}</p>
            <p>Total: R$${tot.toFixed(2)}</p><br>
            <p>Total maior que o aluguel, segue a divisão:</p>
            <p>Luzirene: R$${((tot-(550+div2))/3).toFixed(2)}</p>
            <p>Gabriel: R$${((tot-(550+div2))/3).toFixed(2)}</p>
            <p>Paloma: R$${((tot-(550+div2))/3).toFixed(2)}</p>
            `
        }else{
            res.innerHTML = `
            <p>Luzirene: R$${div1.toFixed(2)}</p>
            <p>Gabriel: R$${div1.toFixed(2)}</p>
            <p>Paloma: R$${div1.toFixed(2)}</p>
            <p>Juliana: R$${div2.toFixed(2)}</p>
            <p>Total: R$${tot.toFixed(2)}</p>
            `
            res.innerHTML = '<p>Sem divisão esse mês!</p>'
        }
    }
}