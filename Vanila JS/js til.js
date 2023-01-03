// Const
// const는 블록범위의 상수를 선언한다. 상수의 값은 재할당할 수 없으며, 다시 선언할 수도 없다.
const num = 42;
try {
  num = 99;
} catch (err) {
  console.log(err);
  // 오류 : TypeError: Assignment to constant variable.
}

console.log(num)
// excepted output : 42

// ----------------------------------

// let
// let 명령문은 블록 스코프의 범위를 가지는 지역 변수를 선언하며, 선언과 동시에 임의의 값으로 초기화할 수 있다.

let x = 1;
if (x === 1) {
  let x = 2;
  console.log(x);
  // excepted output : 2
}
console.log(x);
// excepted output : 1