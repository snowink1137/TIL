const React = require('react');
const ReactDom = require('react-dom');

const WordRelay = require('./끝말잇기/WordRelay');
const WordRelayHooks = require('./끝말잇기/WordRelayHooks');
import NumberBaseball from "./숫자야구/NumberBaseball";
import NumberBaseballHooks from "./숫자야구/NumberBaseballHooks";
import RenderTest from "./반응속도체크/RenderTest";
import ResponseCheck from "./반응속도체크/ResponseCheck";
import ResponseCheckHooks from "./반응속도체크/ResponseCheckHooks";
import RSP from "./가위바위보/RSP";
import RSPHooks from "./가위바위보/RSPHooks";
import Lotto from "./로또/Lotto";
import LottoHooks from "./로또/LottoHooks";
import TicTacToe from "./틱택토/TicTacToe";
import MineSearch from "./지뢰찾기/MineSearch";
import Games from "./react-router/Games";


// ReactDom.render(<WordRelay/>, document.querySelector('#root'));
// ReactDom.render(<WordRelayHooks/>, document.querySelector('#root'));
// ReactDom.render(<NumberBaseball/>, document.querySelector('#root'));
// ReactDom.render(<NumberBaseballHooks/>, document.querySelector('#root'));
// ReactDom.render(<RenderTest/>, document.querySelector('#root'));
// ReactDom.render(<ResponseCheck/>, document.querySelector('#root'));
// ReactDom.render(<ResponseCheckHooks/>, document.querySelector('#root'));
// ReactDom.render(<RSP/>, document.querySelector('#root'));
// ReactDom.render(<RSPHooks/>, document.querySelector('#root'));
// ReactDom.render(<Lotto/>, document.querySelector('#root'));
// ReactDom.render(<LottoHooks/>, document.querySelector('#root'));
// ReactDom.render(<TicTacToe/>, document.querySelector('#root'));
// ReactDom.render(<MineSearch/>, document.querySelector('#root'));
ReactDom.render(<Games/>, document.querySelector('#root'));
