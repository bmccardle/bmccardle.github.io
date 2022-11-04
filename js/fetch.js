 async function getRankings() {
    let url = 'https://api.collegefootballdata.com/rankings?year=2022&week=10';
    try {
        let res = await fetch(url, {
      "method": "GET",
      mode: 'cors',
      "headers": {
            "Authorization": "Bearer 6JZyHQXvTYAqYotH6T9fm5cho1pJjCWA9typXgprvolqFVkMpdbcmCTss8Czixco",
            'Access-Control-Allow-Origin':'*'
      }
     
      
});

//console.log(res.json())

 return await res.json();
 
 


        
    } catch (error) {
        console.log(error);
    }
}

async function renderRankings() {
  let rankings = await getRankings();
  let html = '';
  
  //console.log(rankings.polls)
  rankings.forEach(rank => {
  
    
    rank.polls.forEach((poll, i) =>{
      
      console.log(i)
      if(i == 0){
        let dropDown = `<option selected >${poll.poll}</option>`
        html += dropDown
      }
      else{
        
        let dropDown = `<option>${poll.poll}</option>`
        html += dropDown
        
      }
      
    })
      
      })
      
  let container = document.querySelector('.selectPoll');
  //let container = document.getElementByID('.selectPoll')
  container.innerHTML = html;
      
      }
      
      function getSelectedPoll() {
        var mylist = document.getElementById("selectPoll");
        let poll  = mylist.options[mylist.selectedIndex].text;
        getPoll(poll);
      }
      
      async function getPoll(poll) {
        
        
        console.log(poll)
        
        
      }
/*    
 async function renderRankings() {
    let rankings = await getRankings();
    let html = '';
    
   //console.log(rankings.polls)
    rankings.forEach(rank => {
    
    console.log(rank.polls)
     let header = `<div class="season">
    <h3>${rank.season}</h3></div>`
    
    html += header;
    
    rank.polls.forEach(poll =>{
    
    
    if (poll.poll == "Coaches Poll"){
    
    
    
    
    let pollHeader = `<div class="poll name">
    <h2>${poll.poll}</h2></div>`
    
    html += pollHeader;
    
    poll.ranks.forEach(ranki =>{
    
   
   
        let htmlSegment = `<div class="coach rank">
                            
                            
         <p>${ranki.rank} ${ranki.school}</p></div>`;

        html += htmlSegment;
let container = document.querySelector('.cp');
    container.innerHTML = html;
        
    })
    }
    
     if (poll.poll == "AP Top 25"){
    
    let htmlap = '' 

    
    
    let pollHeader = `<div class="poll name">
    <h2>${poll.poll}</h2></div>`
    
    htmlap += pollHeader;
    
    poll.ranks.forEach(ranki =>{
    
   
   
        let htmlSegmentap = `<div class="ap rank">
                            
                            
         <p>${ranki.rank} ${ranki.school}</p></div>`;

        htmlap += htmlSegmentap;
let container = document.querySelector('.form-group2');
    container.innerHTML = htmlap;
        
    })
    }
    
    
    })
    });

   // let container = document.querySelector('.form-group1');
    //container.innerHTML = html;
    
    
}
    */

 async function getLiveScores() {
    let url = 'https://cors.io/?https://api.collegefootballdata.com/scoreboard';
    try {
        let res = await fetch(url, {
      "method": "GET",
      mode: 'cors',
      "headers": {
            "Authorization": "Bearer 6JZyHQXvTYAqYotH6T9fm5cho1pJjCWA9typXgprvolqFVkMpdbcmCTss8Czixco",
            'Access-Control-Allow-Origin':'*'
      }
     
      
});

//console.log(res.json())

 return await res.json();
 
 


        
    } catch (error) {
        console.log(error);
    }
}

async function renderLive(){
  
  console.log("render live")

let scores = await getLiveScores();
    let html = '';
    
  /*var scheduled = scores.filter(function(schedule){
    
    return schedule.status == "complete"
    
  })
    
   console.log(scheduled)*/
   let date = new Date()
   
  
   html += date
   
   let h3 = `<div class="lives">
    <h3>Live</h3></div>`
    
    html += h3
    
    scores.forEach(score => {
    
    
    
    if (score.tv === null){
      
      let header = `
    <p>${score.homeTeam.name}</p>
    <p>${score.awayTeam.name}</p>
    <p>${score.status}</p>
    <hr>`
      
      html += header;
      
    }
      
      else{
        let header = `
    <p>${score.homeTeam.name}</p>
    <p>${score.awayTeam.name}</p>
    <p>${score.tv}</p>
    <p>${score.status}</p>
    <hr>`
        
        html += header;
        
      }
    });
    
    let container = document.querySelector('.w3-twothird.w3-container');
    container.innerHTML = html;



}
