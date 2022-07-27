import noblePrize from './prize.json'

function NoblePrize({year}) {
    const validYears = ["2021", "2020", "2019", "2018"]
    let noblerows = new Set()
    noblePrize.prizes.forEach((itm)=>{
      let winners = []
      itm.laureates?.forEach((w)=>{
        if (w.surname)
          winners.push(w.firstname + " " + w.surname)
        else
          winners.push(w.firstname)
  
      })
      if (year && itm.year === year && validYears.includes(year))
        noblerows.add({"prizeyear": itm.year, "category": itm.category, "winners": winners})
      else if (!validYears.includes(year))
        noblerows.add({"prizeyear": itm.year, "category": itm.category, "winners": winners})
  
    })
    //console.log(noblerows)
    return(
        <div className="card" style={{width: '48rem'}}>
        {
            Array.from(noblerows).map(x => 
              <div className="card-body">
              <h5 className="card-title">{x.prizeyear}</h5>
              <h6 className="card-subtitle mb-2 text-muted">{x.category}</h6>
              <p className="card-text"> 🏆 {x.winners.join(", ")}</p>
            </div>
            )
          }
      </div>
    );
}
export default NoblePrize;
