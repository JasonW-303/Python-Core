var counter = document.getElementById('counter');
var upButton = document.getElementById('up');
var resetButton = document.getElementById('reset')
var count = parseInt(counter.textContent);


function incrementCounter() {
    count += 2;
    counter.textContent = count;
}
