const React = require('react');
const ReactDom = require('react-dom');

const WordRelay = require('./WordRelay');
const WordRelayHooks = require('./WordRelayHooks');
import NumberBaseball from "./NumberBaseball";

// ReactDom.render(<WordRelay/>, document.querySelector('#root'));
// ReactDom.render(<WordRelayHooks/>, document.querySelector('#root'));
ReactDom.render(<NumberBaseball/>, document.querySelector('#root'));
