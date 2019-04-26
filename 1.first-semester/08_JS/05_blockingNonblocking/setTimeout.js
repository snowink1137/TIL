// // 1. 비교 대상
// const nothing = () => {};
//
// console.log('start');
// setTimeout(nothing, 3000);
// console.log(('end'));

// // 2. 비교 대상
// const logEnd = () => {
//     console.log(('end'));
// };
//
// console.log('start');
// setTimeout(logEnd, 3000);


// 3. 비교 대상
const sleep_3s = () => {
    setTimeout(() => {
        console.log('Wake up!')
    }, 3000);
};

console.log('start sleeping');
sleep_3s();
console.log(('end'));