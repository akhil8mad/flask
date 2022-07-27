import NoblePrize from './NoblePrize';
// import './App.css';
import { useState } from 'react';
import axios from "axios"
import Prediction from './Prediction'
function App() {

  const [algorithm, setAlgorithm] = useState("lr");
  const [rooms, setRooms] = useState();
  const [prediction,setPrediction]=useState("");
  const[water,setWater]=useState("")
  const[summary,setSummary]=useState("")
  const [year, setYear] = useState();
  const [plt, setPlot] = useState();
  const [val, setVal] = useState();
  //this.setRooms = {value: '1'};
  const handleClick = event => {
    //event.preventDefault();
    
    axios.get('http://127.0.0.1:5000/prediction/' + algorithm +'/' +rooms + '/' +year + '/' +val + '/' +plt)
    .then(res => {
      setPrediction(res.data.prediction);
      setWater(res.data.image_water);
      setSummary(res.data.image_summ);


      //this.prediction=res.data;
      console.log(res.data);
    });
    

  };


  return (
    <div style={{
    padding:"100px",
    backgroundColor:"skyblue"
    }} id="container">
      <h1> Machine Learning Prediction</h1>
      <h2> {algorithm} </h2>
      <select value={algorithm} onChange={(e) => { setAlgorithm(e.target.value)}}>
        <option value="lr">Linear Regression</option>
        <option value="rf">Random Forest</option>
      </select>
     
      <hr />
      <header className="App-header">
        <h1> Select Features </h1>
      </header>

      <p> rooms</p>
      <select value={rooms} onChange={(e) => { setRooms(e.target.value)}}>
         <option value="1"> 1</option>
         <option value="2"> 2</option>
         <option value="3"> 3</option>
         <option value ="4"> 4</option>
         <option value="5">5</option>
      </select>
     <div>
      <p>Build Year:</p>
      <input 
      type="text" 
      value={year} 
      onChange={event => setYear(event.target.value)}
      />
      </div>
    <div>
     <p>Area:</p>
     <input 
      type="text" 
      pattern="[0-9]*"
      value={val} 
      onChange={(e) =>
        setVal((v) => (e.target.validity.valid ? e.target.value : v))}
      />
      </div>

      <div>
      <p>plot type:</p>
      <input 
      type="text" 
      value={plt} 
      onChange={event => setPlot(event.target.value)}
      />
      </div>
<br/>

<button onClick = {handleClick}>Predict</button>

<p>Prediction Value:</p>
<p>{prediction}</p>
<div>
<img src={`http://127.0.0.1:5000/${water}`}></img>
</div>
<div>
<img src={`http://127.0.0.1:5000/${summary}`}></img>
</div>




   </div>
  );
}

export default App;
