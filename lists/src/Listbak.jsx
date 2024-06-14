function List() {

    const boats = [{ id: 1, name: "tugboat", length: 62 },
    { id: 2, name: "sailboat", length: 42 },
    { id: 3, name: "motorboat", length: 23 },
    { id: 4, name: "canoe", length: 182 },
    { id: 5, name: "kayak", length: 12 }];

    //  boats.sort((a, b) => a.name.localeCompare(b.name));// alphabetical
    //  boats.sort((a, b) => a.length - b.length); //numerical
    //  boats.sort((a, b) => b.name.localeCompare(a.name)); //reverse alphabetica
    //  boats.sort((a, b) => b.length - a.length); //descending


    const bigger_boats = boats.filter(boats => boats.length > 30);

    const listItems = bigger_boats.map(bigger_boats => <li key={bigger_boats.id}>
        {bigger_boats.name}: & nbsp;
        <b>{bigger_boats.length}</b> </li >);


    return (<ol>{listItems}</ol>);

}

export default List