import Student from "./Student.jsx"

function App() {

  return (
    <>
      <Student name="joe" age={30} isStudent={true} />
      <Student name="betty" />
      <Student name="lola" age={36} isStudent={false} />
      <Student age={36} isStudent={false} />
    </>
  );
}

export default App
