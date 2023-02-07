document.getElementById("main").innerHTML=document.getElementById("hello").innerHTML;

function checking(){
  if (document.getElementById('correct').checked) {
    score +=2;
    check.push("correct");
    scores.push(2);   
  }
  else if(document.getElementById('incorrect1').checked){
    score-=1;
    check.push("Incorrect");  
    scores.push(-1); 
  }
  else if(document.getElementById('incorrect2').checked){
    score-=1;
    check.push("Incorrect");
    scores.push(-1);
  }
  else{
    check.push('Not attempt');
    scores.push(0);
  }
}
var change;
function quizrules(){
  change=document.getElementById("quizimage").value;
  document.getElementById("main").innerHTML=document.getElementById("rules").innerHTML;
}

function hello(){
  document.getElementById("main").innerHTML=document.getElementById("game").innerHTML;
}
var startGame;
var player;
var myVar ;
function play(){
  if(document.getElementById("fname").value!=""){
    player=document.getElementById("fname").value;
    if (change=="false") {
      document.getElementById("main").innerHTML=document.getElementById("questiones").innerHTML;
    }
    startGame=new Date().getTime();
    myVar = setTimeout(displayScore,60000);
    timer();
  }
  else{
    document.getElementById("main").innerHTML=document.getElementById("game").innerHTML;
    alert("Fill the name please");
  }
}
function  musicQ(){
  document.getElementById("main").innerHTML=document.getElementById("questiones").innerHTML;
}
var scores=[];
score=0;
var check=[];

function q1(){ 
  checking();
  document.getElementById("q1").innerHTML=document.getElementById("q2").innerHTML;
}

function q2(){
  checking();
  document.getElementById("q1").innerHTML=document.getElementById("q3").innerHTML;
 }

function q3(){
  checking();
  document.getElementById("q1").innerHTML=document.getElementById("q4").innerHTML;
}

function q4(){
  checking();
  document.getElementById("q1").innerHTML=document.getElementById("q5").innerHTML;
}

function q5(){
  checking();
  document.getElementById("q1").innerHTML=document.getElementById("q6").innerHTML;
}

function q6(){
  checking();
  document.getElementById("q1").innerHTML=document.getElementById("q7").innerHTML;
}

function q7(){
  checking();
  document.getElementById("q1").innerHTML=document.getElementById("q8").innerHTML;
}

function q8(){
  checking();
  document.getElementById("q1").innerHTML=document.getElementById("q9").innerHTML;
}

function q9(){
  checking();
  document.getElementById("q1").innerHTML=document.getElementById("q10").innerHTML;
}
function q10(){
  checking();
  displayScore();
}

var timeDuration;
var minutes;
var number;

function timeDifference(){
  endGame=new Date().getTime();    
  timeDuration=((endGame-startGame)-000020);
  minutes=timeDuration/60000;
  number = minutes.toFixed(2); 
}

var status;
function displayScore(){
  timeDifference();
  clearTimeout(myVar);
  if (score>12){
    status ="Pass";
    document.body.style.backgroundColor="#2A573C";
  }
  else{
    status ="Fail";
    document.body.style.backgroundColor="#900C3F";
    
  }
  for(var i=0;i<10;i++){
    if(scores[i]==-1){
      document.getElementById("card"+(i+1)).style.backgroundColor="#B81212";
      document.getElementById("Q"+(i+1)).innerHTML="Result :"+check[i];
      document.getElementById("marks"+(i+1)).innerHTML="Marks :"+scores[i];
    }
    else if(scores[i]==2){
      document.getElementById("card"+(i+1)).style.backgroundColor="#326D4A";
      document.getElementById("Q"+(i+1)).innerHTML="Result :"+check[i];
      document.getElementById("marks"+(i+1)).innerHTML="Marks :"+scores[i];
    }
    else{
      document.getElementById("card"+(i+1)).style.backgroundColor="orange";
      document.getElementById("Q"+(i+1)).innerHTML="Result :"+check[i];
      document.getElementById("marks"+(i+1)).innerHTML="Marks :"+scores[i];
    }
  }
  document.getElementById("main").innerHTML=document.getElementById("scorecard").innerHTML;
  document.getElementById("playername").innerHTML="Player :"+player;
  document.getElementById("scoregot").innerHTML="Score :"+score;
  document.getElementById("result").innerHTML="Status :"+status;
  document.getElementById("timetaken").innerHTML="Time :"+number+"minutes";
  document.getElementById("check1").innerHTML=check[0];
  document.getElementById("scores1").innerHTML=scores[0];
               
}
               
function startTimer(duration, display) {
  var timer = duration, minutes, seconds;
  setInterval(function () {
    minutes = parseInt(timer / 60, 10);
    seconds = parseInt(timer % 60, 10);

    minutes = minutes < 10 ? "0" + minutes : minutes;
    seconds = seconds < 10 ? "0" + seconds : seconds;

    display.textContent = minutes + ":" + seconds;

    if (--timer < 0) {
      timer = duration;
    }
  }, 1000);
}

function timer(){
  var oneMinutes = 60 * 1,
  display = document.querySelector('#time');
  startTimer(oneMinutes, display);
};