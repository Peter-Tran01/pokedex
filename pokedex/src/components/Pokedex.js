import React, { useState, useEffect } from "react";
import styles from "../css/Pokedex.module.css";
import { Button, TextField } from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";

function Pokedex() {
    const [pokemonData, setPokemonData] = useState([]);

    const handleSearch = async (searchQuery) => {
        try {
            console.log(searchQuery);
            const response = await fetch(
                `http://127.0.0.1:8000/search?query=${searchQuery}`
            );
            const data = await response.json();
            setPokemonData(data);
        } catch (error) {
            console.error("Error fetching search results:", error);
        }
    };

    return (
        <div>
            <form className={styles.search} noValidate autoComplete="off">
                <div className={styles.searchBlock} />
                <TextField
                    sx={{
                        flexGrow: 1,
                    }}
                    placeholder="Search"
                    onChange={(e) => handleSearch(e.target.value)}
                ></TextField>
                <Button
                    type="submit"
                    variant="contained"
                    endIcon={<SearchIcon />}
                >
                    Search
                </Button>
                <div className={styles.searchBlock} />
            </form>
            <br />
            <div className={styles.results}>
                <div className={styles.resultIndent} />
                <div className={styles.resultsBlock}>
                    <div className={styles.background}>
                        <div className={styles.number}>
                            <div className={styles.label}>Pokedex Number</div>
                        </div>
                        <div className={styles.name}>
                            <div className={styles.label}>Pokemon Name</div>
                        </div>
                        <div className={styles.image}>
                            {/* <div className={styles.label}>Picture</div> */}
                        </div>
                        <div className={styles.pokemon_type}>
                            <div className={styles.label}>Pokemon Type</div>
                        </div>
                        <div className={styles.weakness}>
                            <div className={styles.label}>Pokemon Weakness</div>
                        </div>
                    </div>
                    {pokemonData.map((pokemon) => (
                        <div className={styles.background}>
                            <div className={styles.number}>
                                {pokemon.pokedex_number}
                            </div>
                            <hr />
                            <div className={styles.name}>{pokemon.pokemon}</div>
                            <hr />
                            <div className={styles.image}>Sprite</div>
                            <hr />
                            <div className={styles.pokemon_type}>
                                {pokemon.type.map((type, index) => (
                                    // ADD STYLES
                                    <div
                                        key={index}
                                        className={`${styles.type} ${styles[type]}`}
                                    >
                                        {type}
                                    </div>
                                ))}
                            </div>
                            <hr />
                            <div className={styles.weakness}>
                                {pokemon.weakness.map((weakness, index) => (
                                    // ADD STYLES
                                    <div
                                        key={index}
                                        className={`${styles.type} ${styles[weakness]}`}
                                    >
                                        {weakness}
                                    </div>
                                ))}
                            </div>
                        </div>
                    ))}
                </div>
                <div className={styles.resultIndent} />
            </div>
        </div>
    );
}

export default Pokedex;
