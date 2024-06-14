import List from "./List.jsx"

function App() {

  const boats = [{ id: 1, name: "tugboat", length: 62 },
  { id: 2, name: "sailboat", length: 42 },
  { id: 3, name: "motorboat", length: 23 },
  { id: 4, name: "canoe", length: 182 },
  { id: 5, name: "kayak", length: 12 }];

  return (<List items={boats} category="Boats" />);
}

export default App
