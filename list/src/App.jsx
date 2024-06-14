import List from "./List.jsx"

function App() {

  const boats = [{ id: 1, name: "tugboat", length: 62 },
  { id: 2, name: "sailboat", length: 42 },
  { id: 3, name: "motorboat", length: 23 },
  { id: 4, name: "canoe", length: 182 },
  { id: 5, name: "kayak", length: 12 }];

  const vehicles = [{ id: 6, name: "moped", length: 5 },
  { id: 7, name: "bus", length: 42 },
  { id: 8, name: "car", length: 14 },
  { id: 9, name: "van", length: 18 },
  { id: 10, name: "truck", length: 24 }];

  return (<>
    {boats.length > 0 && < List items={boats} category="Boats" />}
    {vehicles.length > 0 && < List items={vehicles} category="Vehicles" />}

  </>);
}

export default App
