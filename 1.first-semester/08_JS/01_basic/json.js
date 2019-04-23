const myObject = {
    coffee: 'Americano',
    iceCream: 'Cookie and Cream',
};

const jsonData = JSON.stringify(myObject);
console.log(typeof jsonData);

const parseData = JSON.parse(jsonData);
console.log(typeof parseData);

