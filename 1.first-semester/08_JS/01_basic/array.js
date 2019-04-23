const numbers = [1, 2, 3, 4];

numbers[0]; // 1
numbers[-1]; // undefined
numbers.length; // 4

/* 원본이 달라지는 methods */
numbers.reverse();
numbers;
numbers.reverse();

number.push('a');
numbers;

numbers.pop();
numbers;

numbers.unshift('a'); // 5 new length
numbers;

numbers.shift();
numbers;

/* Copy, 다른 결과 return */
numbers.includes(1);
numbers.includes(0);

numbers.push('a'); // test
numbers.push('a');
numbers.indexOf('a');
numbers.indexOf('b'); // 없음 => -1

numbers.join('-'); // '1-2-3-4-a-a'
numbers.join(''); // '1234aa'
numbers.join(); // '1,2,3,4,a,a'
