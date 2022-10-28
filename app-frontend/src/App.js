import logo from './logo.svg';
import './App.css';
import MapWithPlaceholder from './Map';
import pointData from './pointData.json';

function App() {

  return (
    <>
      <h1>Drone Byakugan</h1>
      <MapWithPlaceholder pointData={pointData}  />
    </>
    // <div className="App">
    //   <header className="App-header">
    //   </header>
    // </div>
  );
}

export default App;