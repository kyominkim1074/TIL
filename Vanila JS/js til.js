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
// 42