var game_grid; //8x8 matrix
var n=8; //size of the grid matrix

function zero2D(rows, cols) {
  var array = [], row = [];
  while (cols--) row.push(0);
  while (rows--) array.push(row.slice());
  return array;
}

game_grid=zero2D(n,n);
console.log(game_grid);

var cell ={
	r:0,
	c:0,
	state:-1
}
//dead cell = -1; live cell = 1

console.log(cell);

