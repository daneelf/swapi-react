import React, { Component } from "react";
import "./App.css";

class App extends Component {
  constructor(props) {
    super(props);
    this.fetchFilms = this.fetchFilms.bind(this);
    this.filterSpecies = this.filterSpecies.bind(this);
    this.filterCharacters = this.filterCharacters.bind(this);
    this.handleCharacter = this.handleCharacter.bind(this);
    this.toggleClass = this.toggleClass.bind(this)

    this.state = {
      films: [],
      species: [],
      characters: [],
      character: [],
      isFilmsLoading: false,
      isSpeciesLoading: false,
      isCharactersLoading: false,
      characterIsLoading: false,
      active: false,
      error: ""
    };

    this.fetchFilms();
  }

  fetchFilms() {
    let films = [];
    fetch("http://127.0.0.1:8000/api/films/")
      .then(results => {
        if (results.ok) {
          return results.json();
        }
        throw new Error("Failed to fetch");
      })
      .then(data => {
        data.results.forEach(item => {
          films.push(item);
        });
        this.setState({ films: films });
      })
      .catch(error => {
        this.setState({ error: error.message });
      });
  }
  
  toggleClass() {
      const currentState = this.state.active;
      this.setState({ active: !currentState });
  };
  
  filterSpecies(e) {
    let species_id = parseInt(e.target.id.split("/")[5]);
    let formattedNumber = ("0" + species_id).slice(-2);
    let filteredSpecies = [];
    this.setState({ isSpeciesLoading: true });
    fetch("http://127.0.0.1:8000/api/films/" + formattedNumber)
      .then(results => {
        if (results.ok) {
          return results.json();
        }
        throw new Error("Failed to fetch");
      })
      .then(data => {
        filteredSpecies = data;
        this.setState({
          species: filteredSpecies,
          isSpeciesLoading: false,
        });
      })
      .catch(error => {
        this.setState({ error: error.message });
      });
  }

  filterCharacters(e) {
    let species_id = parseInt(e.target.id.split("/")[5]);
    let formattedNumber = ("0" + species_id).slice(-2);
    let filteredCharacters = [];
    this.setState({ isCharactersLoading: true });
    fetch("http://127.0.0.1:8000/api/species/" + formattedNumber)
      .then(results => {
        if (results.ok) {
          return results.json();
        }
        throw new Error("Failed to fetch");
      })
      .then(data => {
        filteredCharacters = data;
        this.setState({
          characters: filteredCharacters,
          isCharactersLoading: false
        });
      })
      .catch(error => {
        this.setState({ error: error.message });
      });
  }

  handleCharacter(e) {
    this.setState({ characterIsLoading: true });
    let species_id = parseInt(e.target.id.split("/")[5]);
    let formattedNumber = ("0" + species_id).slice(-2);
    let character = [];
    this.setState({ isCharacterLoading: true });
    fetch("http://127.0.0.1:8000/api/characters/" + formattedNumber)
      .then(results => {
        if (results.ok) {
          return results.json();
        }
        throw new Error("Failed to fetch");
      })
      .then(data => {
        character = data;
        this.setState({
          character: character,
          isCharacterLoading: false
        });
      })
      .catch(error => {
        this.setState({ error: error.message });
      });
  };

  render() {
    return (
      <div className="container">
        <div className="col align-self-center">
          <center>            
            <h1>In a galaxy far far away...</h1>
          </center>
        </div>
        <br></br>
        <div className="row">
          <div className="col-4 pb-5">
            <div className="list-group">
              {this.state.isFilmsLoading ? (
                <div className="alert alert-info" role="alert">
                  <h4>In a galaxy far far away...</h4>
                </div>
              ) : (
                this.state.films.map((film, i) => {
                  return (
                    <a
                      href="#"
                      onClick={this.filterSpecies}
                      onChange={this.toggleClass}
                      className="list-group-item"
                      id={film.url}
                      key={i}
                    >
                      {/* <Film 
                      // onChange={this.toggleClass} 
                      // onClick={this.filterSpecies}
                      // className="list-group-item"

                      filmTitle={film.title}/> */}
                      {film.title}
                    </a>
                  );
                })
              )}
            </div>
          </div>
          <div className="col-4 pb-5">
            <div className="list-group">
              {this.state.isSpeciesLoading ? (
                <div className="alert alert-info" role="alert">
                  <h4>Patience young Padawan...</h4>
                </div>
              ) : (
                this.state.species.map((species, i) => (
                  <a
                    href="#"
                    onClick={this.filterCharacters}
                    id={species.url}
                    className="list-group-item"
                    key={i}>
                    {species.name}
                  </a>
                ))
              )}
            </div>
          </div>
          <div className="col-4 pb-5">
            {this.state.isCharactersLoading ? (
              <div className="alert alert-info" role="alert">
                <h4>These might be droids you're looking for....</h4>
              </div>
            ) : (
              this.state.characters.map((character, i) => (
                <a
                  href="#"
                  onClick={this.handleCharacter}
                  id={character.url}
                  className="list-group-item"
                  key={i}
                >
                  {character.name}
                </a>
              ))
            )}
          </div>
          <div className="col-4 pb-5">
            {this.state.isCharacterLoading ? (
              <div className="alert alert-info" role="alert">
                <h4>The force is strong with this one...</h4>
              </div>
            ) : (
              <div>
                <h3>{this.state.character.name}</h3>
                <h4>{this.state.character.birth_year}</h4>
                <h4>{this.state.character.gender}</h4>
              </div>
            )}
          </div>
        </div>
      </div>
    );
  }
}

export default App;
