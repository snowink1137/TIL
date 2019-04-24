/* 1. <input> 태그 안의 값을 잡는다. */
const inputArea = document.querySelector('#js-userinput');
const button = document.querySelector('#js-go');
const resultArea = document.querySelector('#result-area');

inputArea.addEventListener('keydown', e => {
    if (e.key === 'Enter') {
        searchAndPush(inputArea.value);
    }
});
button.addEventListener('click', e => {
    searchAndPush(inputArea.value);
});


/* 2. Giphy API 를 통해 data 를 받아서 가공한다. */
/* 3. GIF 파일들을 index.html(DOM)에 밀어 넣어서 보여준다. */
const searchAndPush = keyword => {
    const KEY = 'npTD8hoaM96K0yuzH9pzyMRc0Ag7TrtC';
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${KEY}`;

// AJAX 요청을 보낸다. =>
    /* 기존의 요청
        1. 링크를 누른다.
        2. href 으로 요청이 간다.
        3. 브라우저가 새로고침 되며, 응답을 render 한다.

       AJAX 요청
        1. 어떤 event 가 발생한다.
        2. 요청을 전송하고, 응답이 도착할 때까지 기다린다. 화면 전환은 없다!
        3. 응답이 오면, 지금 문서에서 응답 내용을 추가로 render 한다.
     */
    const AJAXCall = new XMLHttpRequest(); // AJAX 요청을 보내줄 친구
    AJAXCall.open('GET', URL); // 요청을 발사할 준비
    AJAXCall.send();
    AJAXCall.addEventListener('load', e => {
        // console.log(e);
        const rawData = e.target.response;
        const parseData = JSON.parse(rawData);
        pushToDOM(parseData);
    });

    const pushToDOM = dataset => {
        resultArea.innerHTML = null; // 기존의 img 다 날리고 다시 시작한다.
        const dataArray = dataset.data;
        let imageURL, element;
        for (const imgData of dataArray) {
            imageURL = imgData.images.fixed_height.url;
            element = document.createElement('img'); // <img >
            element.classList.add('container-image'); // <img class="container-image" >
            element.src = imageURL;
            resultArea.appendChild(element);
        }
    };
};
