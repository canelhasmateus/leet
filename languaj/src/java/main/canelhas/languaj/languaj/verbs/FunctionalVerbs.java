package canelhas.languaj.languaj.verbs;

import canelhas.languaj.languaj.nouns.Functional;
import canelhas.languaj.languaj.nouns.Thunk;

import java.util.function.Function;

public class FunctionalVerbs {
    public static < K, V > Thunk< V > delay( Function< K, V > action, K element ) {
        return ( Void v ) -> action.apply( element );
    }

    public static < V > Thunk< V > delay( V element ) {
        return ( Void v ) -> element;
    }

    public static < K, V > Functional< K, V > disambiguate( Function< K, V > action, Class< K > input ) {
        return action::apply;
    }
}
