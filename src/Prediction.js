function Prediction({algorithm,rooms,year,val, res}) {
    //console.log(res)
    console.log(algorithm)
    console.log(rooms)
    //Client Side:
    // if (algorithm == 'rf')
    //     image = <img src="http://127.0.0.1:5000/img/fl1" style={{ height:'500px'}} />
    // else
    //     image = <img src="http://127.0.0.1:5000/img/fl2"  style={{ height:'500px'}}  />
     
    return(
        <div>
            <hr />
            <p>Algorithm: {algorithm}</p> 
            <p>Rooms :{rooms} </p>
            
            <p>Prediction: {res.prediction}</p> 
           
        </div>
        
    )
}
export default Prediction;