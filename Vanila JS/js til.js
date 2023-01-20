// const num = 42;
// try {
//   num = 99;
// } catch (err) {
//   console.log(err);
//   // 오류 : TypeError: Assignment to constant variable.
// }

// console.log(num)
// // excepted output : 42

// let x = 1;
// if (x === 1) {
//   let x = 2;
//   console.log(x);
//   // excepted output : 2
// }
// console.log(x);
// // excepted output : 1

// var a = 1;
// if (a === 1) {
//   var a = 2;
//   console.log(a);
//   // excepted output : 2
// }
// console.log(a);
// // excepted output : 2

// var x_ = new Boolean(false);
// if (x_) {
//   // 이 코드는 실행됨
// }

// var x__ = false;
// if (x__) {
//   // 이 코드는 실행되지 않음
// }

// var myFalse = new Boolean(false);   // 초기값 거짓
// var g = Boolean(myFalse);           // 초기값 참
// var myString = new String('Hello'); // 문자열 객체
// var s = Boolean(myString);          // 초기값 참

// let fruits = ['사과', '바나나']
// console.log(fruits.length)
// fruits.forEach(function (item, index, array) {
//   console.log(item, index)
// })

// const player = {
//   name: "kim",
//   points: 10,
//   fat: false,
// };

// console.log(player);

// player.fat = true;

// console.log(player);
// console.log(player.name);

// function sayHello(nameOfPerson, age) {
//   console.log(nameOfPerson, age);
// }

// sayHello("bak", 12);
// sayHello("kim", 15);

// function plus(a, b) {
//   console.log(a + b);
// }

// function divide(c, d) {
//   console.log(c / d);
// }

// plus(10, 120);
// divide(30, 8)

// const calculator = {
//   plus: function (a, b) {
//     return a + b;
//   },
//   minus: function (a, b) {
//     return a - b;
//   },
//   times: function (a, b) {
//     return a * b;
//   },
//   divide: function (a, b) {
//     return a / b;
//   },
//   power: function (a, b) {
//     return a ** b;
//   },
// }

// const plusResult = calculator.plus(2, 3);
// console.log(plusResult)
// const minusResult = calculator.minus(plusResult, 10);
// console.log(minusResult)
// const timesResult = calculator.times(minusResult, -10);
// const divideResult = calculator.divide(timesResult, 2);
// const powerResult = calculator.power(divideResult, divideResult);

const age = parseInt(prompt("age?"));

// || = or, && = and
if (isNaN(age) || age < 0) {
  console.log("Please write a real positive number.");
} else if (age < 18) {
  console.log("You are not adult.");
} else if (age > 50 && age <= 50) {
  console.log("You are adult.");
} else if (age > 50 && age <= 80) {
  console.log("You should take care of your health.");
} else if (age > 80) {
  console.log("You can do whatever you want.");
} else if (age === 100) {
  console.log("You are wise.");
}