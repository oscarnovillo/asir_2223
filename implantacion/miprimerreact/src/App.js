import logo from './logo.svg';
import './App.css';

function App() {

  const name = "pepe";

  const handleSomething = () => {

    //sumar dos numero
    

    return "something";


  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Hello {name}!
           {handleSomething()}
        </p>
       
      </header>
    </div>
  );
}

export default App;
