console.log(typeof 1);
console.log(typeof (typeof 1));

console.log(function () {});
console.log(typeof (()=>{}));

console.log(typeof NaN);

// 더하기가 아래와 같은 결과를 만든다
console.log(200 + 'a');
console.log('200' + 'a');

// 곱하기가 아래와 같은 결과를 만든다
console.log(typeof ('100' * 1));
console.log('100' * 1);

