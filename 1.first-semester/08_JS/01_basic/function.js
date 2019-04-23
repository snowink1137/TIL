// 1. 함수 키워드 정의
function add (num1, num2) {
        return num1 + num2;
}

// 2. 변수에 함수 로직 할당. 함수는 const!
const sub = function (num1, num2) {
    return num1 - num2;
};


// 3. arrow 표현식
/*
추가 리팩토링
step 1: 인자가 단 하나라면 ()가 생략 가능하다.
step 2: 함수 블록안에 코드가 return 문 한 줄이라면, {} & return 키워드 생략 가능하다.
 */
mul = (num1, num2) => {
    return num1 * num2;
};

let square = function (num) {
    return num ** 2;
};

square = num => num ** 2;
console.log(square(3))

let noArgs = () => {
    return 'nothing';
};

noArgs = () => 'nothing';
manArgs = (a, b, c, d, e) => 'wow';

/* Default Args */
function sayHello (name) {
    return `hi ${name}!`;
}

const sayHi = (name='ssafy') => `hi ${name}!`;

sayHi();

console.log((num => num ** 2)(4));


