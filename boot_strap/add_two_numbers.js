function dosomething(){
    let a = document.getElementById('inputA').value;
    let b = document.getElementById('inputB').value;
    document.getElementById("valueA").innerHTML = a;
    document.getElementById("valueB").innerHTML = b;
    document.getElementById("valueC").innerHTML = number(a) + number(b);
}