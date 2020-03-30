// XHR.js ES6+ BROWSER

const DOMAIN = 'https://jsonplaceholder.typicode.com';
const RESOURCE = '/posts';
const QUERY_STRING = '';

const URL = DOMAIN + RESOURCE + QUERY_STRING;
// req 대리인 XHR 객체 생성
const XHR = new XMLHttpRequest();

// XHR 요청 발사 준비 (method, url)
XHR.open('POST', URL);
XHR.setRequestHeader(
    'Content-Type',
    'application/json;charset=UTF-8'
);

// XHR 요청 발사!
XHR.send(
    JSON.stringify({ "title": "NewPost", "body": "This is New post", "userId": 1 })
);

XHR.addEventListener('load', e => {
    const rawData = e.target.response;
    const parseData = JSON.parse(rawData);
    console.log(parseData);
});