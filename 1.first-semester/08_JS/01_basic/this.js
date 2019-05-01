function hi() {

}

const bye = () => {

};

const me = {
    name: '지쓰',
    phone: '01011112222',
    email: 'jiss@naver.com',
    intro: function () {
        return `Hi my name is ${this.name}.`
    }
};
console.log(me.intro());
const you = {
    name: '상현',
    phone: '01011112222',
    email: 'jiss@naver.com',
    intro: () => {
        return `Hi my name is ${this.name}.`
    },
    wait: function () {
        setTimeout(() => {
          console.log(this.email)
        }, 1000)
    }
};

console.log(you.wait());