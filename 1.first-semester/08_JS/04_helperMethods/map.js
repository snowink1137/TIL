// map과 forEach의 차이점:
// 1. map은 return이 있다.

const numbers = [1, 2, 3];

function double(n) {
    return n * 2;
}

const doubleNumbers = numbers.map(double);
const tripleNumbers = numbers.map(number => {
    return number * 3;
});

console.log(doubleNumbers, tripleNumbers);

/*
    아래의 pluck 함수를 완성하세요.
    pluck 함수는 배열(array)과 요소 이름(key)의 문자열을 받ㅇ
 */

function pluck(array, property) {
    // Fill me
    const result = array.map(e => {
        if (e[property]) return e[property];
    });
    return result
}

const paints = [
    {color: 'red'},
    {color: 'blue'},
    {color: 'white'},
    {smell: 'ughh'},
];

console.log(pluck(paints, 'color'));
console.log(pluck(paints, 'smell'));

