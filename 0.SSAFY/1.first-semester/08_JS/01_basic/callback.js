// 인자로 배열을 받는다. 해당 배열의 모든 요소를 더한 숫자를 return
const numbersEachPlus = numbers => {
    let acc = 0;
    for (const number of numbers) {
        acc += number;
    }
    return acc;
};

// 인자로 배열을 받는다. 해당 배열의 모든 요소를 뺀 숫자를 return
const numbersEachSub = numbers => {
    let acc = 0;
    for (const number of numbers) {
        acc -= number;
    }
    return acc;
};

// 인자로 배열을 받는다. 해당 배열의 모든 요소를 곱한 숫자를 return
const numbersEachMul = numbers => {
    let acc = 1;
    for (const number of numbers) {
        acc *= number;
    }
    return acc;
};


// 숫자로 이루어진 배열의 요소들을 각각 [???] 한다. [???]는 알아서 해라.
const numberEach = (numbers, callback) => {
    let acc; // JS 에서는 변수 선언만 할 수 있다.
    for (const num of numbers) {
         acc = callback(num, acc);
    }
    return acc;
};

const muler = (number, sum=1) => {
    return sum * number
};

const adder = (number, sum=0) => {
    return sum + number;
};

result1 = numberEach([1,2,3,4,5], adder);
result2 = numberEach([1,2,3,4,5], muler);
result3 = numberEach([1,2,3,4,5], (number, sum=0) => sum + number);

console.log(result1, result2, result3);

// 1. 과목 평가 예시
function myFunc () {
    return n => n + 1;
    // return function (n) {
    //     return n + 1;
    // } // 이거와 같은 말임.
}

const num_101 = myFunc()(100);

// 2. 과목 평가 예시
function func1 (cb1, cb2) {
    console.log(1);
    cb1(cb2(cb1))
}

function func2 (callback) {
    console.log(2);
}

function func3 (callback) {
    console.log(3);
}

func1(func2, func3);
