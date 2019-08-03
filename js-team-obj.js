const team = {
  _players: [
    {
      firstName: 'Mesut', lastName: 'Ozil', age: 30
  },
    {
      firstName: 'Alexandre', lastName: 'Lacazette', age: 29
    },
    {
      firstName: 'Nicolas', lastName: 'Pepe', age: 24
    }
  ],
  _games: [
    { opponent: 'Spurs', teamPoints: 4, opponentPoints: 2
    },
    { opponent: 'Liverpool', teamPoints: 1, opponentPoints: 1}, {
      opponent: 'Brighton', teamPoints: 6, opponentPoints: 0
    }
  ],
  get games(){
    return this._games;
  },
  get players(){
    return this._players;
  },
  addPlayer(firstName, lastName, age){
    let player = {
      firstName: firstName,
      lastName: lastName,
      age: age
    };
    
this.players.push(player); },
  
  addGame(opponent, teamPoints, opponentPoints){
    let game = {
      opponent: opponent,
      teamPoints: teamPoints,
      opponentPoints: opponentPoints
    };
  this.games.push(game);
  }
  
};

team.addPlayer('Rob', 'Holding', 23);
team.addGame('Man City', 3, 2);

console.log(team.players)
console.log(team.games)
