const num = 42;
try {
  num = 99;
} catch (err) {
  console.log(err);
  // 오류 : TypeError: Assignment to constant variable.
}

console.log(num)
// excepted output : 42

let x = 1;
if (x === 1) {
  let x = 2;
  console.log(x);
  // excepted output : 2
}
console.log(x);
// excepted output : 1

var a = 1;
if (a === 1) {
  var a = 2;
  console.log(a);
  // excepted output : 2
}
console.log(a);
// excepted output : 2

var x_ = new Boolean(false);
if (x_) {
  // 이 코드는 실행됨
}

var x__ = false;
if (x__) {
  // 이 코드는 실행되지 않음
}