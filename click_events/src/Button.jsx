function Button() {

    const handleClick = (e) => e.target.textContent = "hey";

    return (<button onClick={(e) => handleClick(e)}>⌚️Click</button>);


}
export default Button