import React, {memo} from "react";

// const TryHooks = (props) => {
//     return (
//         <li>
//             <div>{props.tryInfo.try}</div>
//             <div>{props.tryInfo.result}</div>
//         </li>
//     )
// }

const TryHooks = memo(({tryInfo}) => {
    return (
        <li>
            <div>{tryInfo.try}</div>
            <div>{tryInfo.result}</div>
        </li>
    )
})

export default TryHooks;
