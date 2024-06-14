import UserGreeting from "./UserGreeting"

function App() {

  return (
    <>
      <UserGreeting isLoggedIn={true} username="John" />
    </>
  );
}

export default App
