const React = require('react');
const ReactDom = require('react-dom');

const WordRelay = require('./WordRelay');
const WordRelayHooks = require('./WordRelayHooks');
import NumberBaseball from "./NumberBaseball";
import NumberBaseballHooks from "./NumberBaseballHooks";
import RenderTest from "./RenderTest";
import ResponseCheck from "./ResponseCheck";
import ResponseCheckHooks from "./ResponseCheckHooks";
import RSP from "./RSP";
import RSPHooks from "./RSPHooks";
import Lotto from "./Lotto";
import LottoHooks from "./LottoHooks";

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
ReactDom.render(<LottoHooks/>, document.querySelector('#root'));
