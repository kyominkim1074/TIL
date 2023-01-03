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

var myFalse = new Boolean(false);   // 초기값 거짓
var g = Boolean(myFalse);           // 초기값 참
var myString = new String('Hello'); // 문자열 객체
var s = Boolean(myString);          // 초기값 참