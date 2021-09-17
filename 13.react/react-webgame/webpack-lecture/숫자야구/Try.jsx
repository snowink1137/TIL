import React, {PureComponent} from "react";

class Try extends PureComponent {
    render() {
        console.log('퓨어 렌더링')
        return (
            <li>
                <div>{this.props.tryInfo.try}</div>
                <div>{this.props.tryInfo.result}</div>
            </li>
        )
    }
}

export default Try;
