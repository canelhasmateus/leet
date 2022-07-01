package canelhas.languaj.languaj.adverbs;


import canelhas.languaj.languaj.nouns.BiFunctional;
import canelhas.languaj.languaj.nouns.Functional;

import java.util.function.BiFunction;
import java.util.function.Function;

public class NullAdverbs {
    public static < K, V > Functional< K, V > safely( Function< K, V > action ) {
        return ( K k ) -> {
            if ( k == null ) {
                return null;
            }
            return action.apply( k );
        };
    }

    public static < K, U, V > BiFunctional< K, U, V > safely( BiFunction< K, U, V > action ) {
        return ( K k, U u ) -> {
            if ( k == null || u == null ) {
                return null;
            }

            return action.apply( k, u );
        };
    }
}
