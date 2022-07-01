package canelhas.languaj.languaj.adverbs;


import canelhas.languaj.languaj.nouns.Conditional;
import canelhas.languaj.languaj.nouns.Functional;

import java.util.Optional;
import java.util.function.BiFunction;

public class FunctionalAdverbs {
    //region optionals
    public static < T > Conditional< T > conditionally( T element ) {
        return ( Boolean b ) -> {
            if ( Boolean.TRUE.equals( b ) ) {
                return Optional.ofNullable( element );
            }
            else {
                return Optional.empty();
            }
        };
    }

    public static < K, U, V > Functional< U, V > partially( BiFunction< K, U, V > action, K element ) {
        return ( U u ) -> action.apply( element, u );
    }

    public static < K, U, V > Functional< K, V > partially( U element, BiFunction< K, U, V > action ) {
        return ( K k ) -> action.apply( k, element );
    }
}
