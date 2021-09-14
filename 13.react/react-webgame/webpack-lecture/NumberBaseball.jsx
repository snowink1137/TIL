import React, {Component} from "react";
import Try from "./Try";

function getNumbers() {  // 숫자 네 개를 겹치지 않고 랜덤하게 뽑는 경우

}

class NumberBaseball extends Component {
    state = {
        result: '',
        value: '',
        answer: getNumbers(),
        tries: [],
    };

    onSubmitForm = () => {

    };

    fruits = [
        {fruit: '사과', taste: '맛있다'},
        {fruit: '밤', taste: '맛있다'},
        {fruit: '감', taste: '맛있다'},
        {fruit: '귤', taste: '맛있다'},
        {fruit: '사과', taste: '맛없다'},
    ];

    render() {
        return (
            <>
                <h1>{this.state.result}</h1>
                <form onSubmit={this.onSubmitForm}>
                    <input maxLength={4} value={this.state.value} onChange={this.onChangeInput}/>
                </form>
                <div>시도: {this.state.tries.length}</div>
                <ul>
                    {this.fruits.map((v, i) => {
                        return (
                            <Try value={v} index={i}/>
                        );
                    })}
                </ul>
            </>
        )
    }
}

export default NumberBaseball;  // import NumberBaseball;