const canvasHeight = 500;
const canvasWidth = 1000;

var ballX = canvasWidth / 2;
var ballY = canvasHeight / 2;

var ballSize = 30;

let strokeColor = 'black';
let ballColor = 'white';
//współrzędne paletki gracza pierwszego
var paddlePX = 50;
var paddlePY = 180;
//współrzędne paletki gracza drugiego
var paddlePTX = 930;
var paddlePTY = 180;
//wysokosc paletki
paddleHeight = 140;
//szerokosc paletki
paddleWidth = 20;
//szybkosc piłki
ballSpeedX = 4;
ballSpeedY = -4;
//wielkość linii środkowych
const lineWidth = 6;
const lineHeight = 20;

function setup(){
  frameRate(60);
  createCanvas(canvasWidth, canvasHeight);
};

function draw(){
  background('gray');
  lines();
  ball();
  paddleOne();
  paddleTwo();
};
function ball(){
  ellipse(ballX, ballY, ballSize, ballSize);
  fill(ballColor);
  stroke(strokeColor);

  ballX += ballSpeedX;
  ballY += ballSpeedY;

  if(ballY - 15 < 0){
    ballSpeedY = -ballSpeedY;
  }
  if(ballY + 15 > canvasHeight){
    ballSpeedY = -ballSpeedY;
  }
  if(ballX - 10 < 0){
    ballSpeedX = -ballSpeedX;
  }
  if(ballX + 10 > canvasWidth){
    ballSpeedX = -ballSpeedX;
  }
};

function paddleOne(){
  rect(paddlePX, paddlePY, paddleWidth, paddleHeight, 20);
};
function paddleTwo(){
  rect(paddlePTX, paddlePTY, paddleWidth, paddleHeight, 20);
};
function lines(){
  for (
    let linePosition = 20;
    linePosition < canvasHeight;
    linePosition += 2 * lineHeight
  ) {
    rect(canvasWidth / 2 - lineWidth / 2, linePosition, lineWidth, lineHeight);
  }
};
