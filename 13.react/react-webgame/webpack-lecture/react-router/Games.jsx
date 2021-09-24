import React from "react";
import {BrowserRouter, HashRouter, Route, Link} from "react-router-dom";
import GameMatcher from "./GameMatcher";

const Games = () => {
    return (
        <BrowserRouter>
            <div>
                공통인 부분
                &nbsp;
                <Link to="/game/number-baseball">숫자야구</Link>
                &nbsp;
                <Link to="/game/rock-scissors-paper">가위바위보</Link>
                &nbsp;
                <Link to="/game/word-relay">끝말잇기</Link>
                &nbsp;
                <Link to="/game/index">게임 매처</Link>
            </div>
            <div>
                <Route path={"/game/:name"} component={GameMatcher}/>
            </div>
        </BrowserRouter>
    );
};

export default Games;
