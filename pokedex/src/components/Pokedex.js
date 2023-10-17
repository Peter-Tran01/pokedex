import styles from "../css/Pokedex.module.css";
import { Button, TextField } from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";

function Pokedex() {
    return (
        <div>
            <form
                className={styles.search}
                noValidate
                autoComplete="off"
                // onSubmit={handleSearch}
            >
                <div className={styles.searchBlock} />
                <TextField
                    sx={{
                        flexGrow: 1,
                    }}
                    placeholder="Search"
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
            <div className={styles.background}>
                <div className={styles.number}>Number</div>
                <div className={styles.name}>Name</div>
                <div className={styles.image}>Sprite</div>
                <div className={styles.type}>Type</div>
                <div className={styles.weakness}>Weakness</div>
            </div>
        </div>
    );
}

export default Pokedex;
