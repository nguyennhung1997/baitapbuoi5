
function changeColor() {
  document.getElementById("doan1").style.color = "#319e14";
  document.getElementById("doan2").style.color = "#f9c710";
  document.getElementById("doan3").style.color = "#f5380e";
}

function changeBgColor() {
  document.body.style.backgroundColor = "#b3ece5";
}

function copyContent() {
  let doan1 = document.getElementById("doan1").innerHTML;
  document.getElementById("doan2").innerHTML = doan1;
}

function changeFontSize(x) {
  document.getElementById("doan1").style.fontSize = x + 'px';
  document.getElementById("doan2").style.fontSize = x + 'px';
  document.getElementById("doan3").style.fontSize = x + 'px';
}

function changeFontSize2(x, paragraph) {
  document.getElementById(paragraph).style.fontSize = x + 'px';
}

function increaseFontSize(paragraph) {
  let elem = document.getElementById(paragraph);
  let current_fontsize = window.getComputedStyle(elem, null).getPropertyValue('font-size');
  let x = parseInt(current_fontsize) + 1;
  if (x <= 30) {
    changeFontSize2(x, paragraph);
  }
}

function decreaseFontSize(paragraph) {
  let elem = document.getElementById(paragraph);
  let current_fontsize = window.getComputedStyle(elem, null).getPropertyValue('font-size');
  let x = parseInt(current_fontsize) - 1;
  if (x >= 10) {
    changeFontSize2(x, paragraph);
  }
}