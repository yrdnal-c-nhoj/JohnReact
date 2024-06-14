function Button() {

    let count = 0;

    const handleClick = (name) => {
        if (count < 3) {
            count++;
            console.log(`${name} you clicked ${count} me`);
        }
        else {
            console.log(`${name} stop clicking me`);
        }
    };
    return (<button onClick={handleClick}>⍟click</button>);
}
export default Button
