import useAxios from 'axios-hooks';

import MapWithPlaceholder from './Map';
import './App.css';

function App() {
  const [{ data, loading, error }] = useAxios(
    'http://127.0.0.1:5001/point/'
  )

  if (loading) return <p>Loading...</p>
  if (error) return <p>Error! Unable to retrieve data from backend</p>

  console.log(data);
  var pointData = data;
  console.log(pointData);

  return (
    <>
      <h1>Drone Byakugan</h1>
      <MapWithPlaceholder pointData={pointData}  />
    </>
  );
}

export default App;