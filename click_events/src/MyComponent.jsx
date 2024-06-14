import React, { useState } from "react";

function MyComponent() {

    const [name, setName] = useState("Lola");
    const [age, setAge] = useState(0);
    const [isMember, setIsMember] = useState(false);

    const updateName = () => {
        setName("John");
    }

    const incrementAge = () => {
        setAge(age + 1);
    }

    const toggleMemberStatus = () => {
        setIsMember(!isMember);
    }
    return (<div>
        <p>Name: {name}</p>
        <button onClick={updateName}>Set Name</button>

        <p>Age: {age}</p>
        <button onClick={incrementAge}>Set Age</button>

        <p>Is a Member: {isMember ? "Yes" : "No"} </p>
        <button onClick={toggleMemberStatus}>toggle status</button>
    </div>);
}
export default MyComponent