package canelhas.languaj.languaj.adverbs;

import canelhas.languaj.languaj.nouns.BiFunctional;
import canelhas.languaj.languaj.nouns.Functional;

import java.util.Optional;
import java.util.function.BiFunction;
import java.util.function.Function;

public class OptionalAdverbs {
    public static < K, V > Functional< K, Optional< V > > hopefully( Function< K, V > action ) {
        return ( K k ) -> {
            try {
                return Optional.ofNullable( action.apply( k ) );
            }
            catch ( Exception e ) {
                return Optional.empty();
            }
        };
    }

    public static < K, U, V > BiFunctional< K, U, Optional< V > > hopefully( BiFunction< K, U, V > action ) {
        return ( K k, U u ) -> {
            try {
                return Optional.ofNullable( action.apply( k, u ) );
            }
            catch ( Exception e ) {
                return Optional.empty();
            }
        };
    }
}
