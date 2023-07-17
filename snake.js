var gameBoard = document.getElementById('game-board');

for (var i = 0; i < 20; i++) {
  for (var j = 0; j < 20; j++) {
    var cell = document.createElement('div');
    cell.id = 'cell-' + i + '-' + j;
    cell.className = 'cell';
    gameBoard.appendChild(cell);
  }
}

// The snake is represented as an array of coordinates
var snake = [[10, 10]];

// The food is represented as a coordinate
var food = [5, 5];

function updateGameBoard() {
  // Clear the game board
  for (var i = 0; i < 20; i++) {
    for (var j = 0; j < 20; j++) {
      document.getElementById('cell-' + i + '-' + j).style.backgroundColor = 'white';
    }
  }

  // Draw the snake
  for (var part of snake) {
    document.getElementById('cell-' + part[0] + '-' + part[1]).style.backgroundColor = 'green';
  }

  // Draw the food
  document.getElementById('cell-' + food[0] + '-' + food[1]).style.backgroundColor = 'red';
}

updateGameBoard();

// Snake Movement
function moveSnake(direction) {
  // Get the head of the snake
  var head = snake[0];

  // Calculate the new head position
  var newHead;
  if (direction === 'up') {
    newHead = [head[0] - 1, head[1]];
  } else if (direction === 'down') {
    newHead = [head[0] + 1, head[1]];
  } else if (direction === 'left') {
    newHead = [head[0], head[1] - 1];
  } else if (direction === 'right') {
    newHead = [head[0], head[1] + 1];
  }

  // Add the new head to the snake
  snake.unshift(newHead);

  // Remove the tail of the snake
  snake.pop();
}

// Eating Food
function eatFood() {
  // Get the head of the snake
  var head = snake[0];

  // If the head is on the food
  if (head[0] === food[0] && head[1] === food[1]) {
    // Add the food to the snake
    snake.unshift(food);

    // Generate new food
    while (true) {
      var newFood = [Math.floor(Math.random() * 20), Math.floor(Math.random() * 20)];
      if (!snake.some(part => part[0] === newFood[0] && part[1] === newFood[1])) {
        food = newFood;
        break;
      }
    }
  }
}

// Game Over Condition
function isGameOver() {
  // Get the head of the snake
  var head = snake[0];

  // If the head is out of bounds
  if (head[0] < 0 || head[0] >= 20 || head[1] < 0 || head[1] >= 20) {
    return true;
  }

  // If the head is on the body
  for (var i = 1; i < snake.length; i++) {
    if (snake[i][0] === head[0] && snake[i][1] === head[1]) {
      return true;
    }
  }

  // Otherwise, the game is not over
  return false;
}

// AI Opponent
function makeAIMove() {
  // Get the head of the snake
  var head = snake[0];

  // If the food is to the right of the snake, move right
  if (food[1] > head[1]) {
    moveSnake('right');
  }
  // If the food is to the left of the snake, move left
  else if (food[1] < head[1]) {
    moveSnake('left');
  }
  // If the food is above the snake, move up
  else if (food[0] < head[0]) {
    moveSnake('up');
  }
  // If the food is below the snake, move down
  else if (food[0] > head[0]) {
    moveSnake('down');
  }
}

// Start the game
moveSnake('right');