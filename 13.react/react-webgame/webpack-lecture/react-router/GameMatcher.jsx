import React, {Component} from "react";
import NumberBaseball from "../숫자야구/NumberBaseball";
import RSP from "../가위바위보/RSP";
import WordRelay from "../끝말잇기/WordRelay";

export default class GameMatcher extends Component {
    render() {
        if (this.props.match.params.name === 'number-baseball') {
            return <NumberBaseball/>;
        } else if (this.props.match.params.name === 'rock-scissors-paper') {
            return <RSP/>;
        } else if (this.props.match.params.name === 'word-relay') {
            return <WordRelay/>;
        }

        return (
            <div>
                일치하는 게임이 없습니다.
            </div>
        );
    }
};
