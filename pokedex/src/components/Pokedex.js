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
            {pokemonData.map((pokemon) => (
                <div className={styles.background}>
                    <div className={styles.number}>
                        {pokemon.pokedex_number}
                    </div>
                    <div className={styles.name}>{pokemon.pokemon}</div>
                    <div className={styles.image}>Sprite</div>
                    <div className={styles.type}>
                        {pokemon.type.map((type, index) => (
                            // ADD STYLES
                            <div
                                key={index}
                                className={`${styles.TO_BE_DETERMINED} ${styles[type]}`}
                            >
                                {type}
                            </div>
                        ))}
                    </div>
                    <div className={styles.weakness}>
                        {pokemon.weakness.map((weakness, index) => (
                            // ADD STYLES
                            <div
                                key={index}
                                className={`${styles.TO_BE_DETERMINED} ${styles[weakness]}`}
                            >
                                {weakness}
                            </div>
                        ))}
                    </div>
                </div>
            ))}
        </div>
    );
}

export default Pokedex;
