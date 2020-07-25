import java.util.ArrayList;
import java.util.HashMap;

public class PokeBag {
    private final HashMap<String, ArrayList<Pokemon>> pokemons = new HashMap<>();

    public ArrayList<Pokemon> getPokemons(String name) {
        return pokemons.get(name);
    }

    public void add(Pokemon pokemon) {
        if (pokemons.containsKey(pokemon.name)) {
            pokemons.get(pokemon.name).add(pokemon);
        } else {
            ArrayList<Pokemon> temp = new ArrayList<>();
            temp.add(pokemon);
            pokemons.put(pokemon.name, temp);
        }

    }

    public Pokemon getStrongest(String name) {
        Pokemon result = new Pokemon("temp", 0);
        if (!pokemons.containsKey(name)) {
            return null;
        }

        for (Pokemon pokemon : pokemons.get(name)) {
            if (pokemon.cp > result.cp) {
                result = pokemon;
            }
        }
        return result;
    }

    public Pokemon getStrongest() {
        ArrayList<Pokemon> strongestList = new ArrayList<>();
        for (String name : pokemons.keySet()) {
            strongestList.add(getStrongest(name));
        }

        Pokemon result = strongestList.get(0);
        for (Pokemon pokemon : strongestList) {
            if (pokemon.cp > result.cp) {
                result = pokemon;
            }
        }
        return result;
    }
}