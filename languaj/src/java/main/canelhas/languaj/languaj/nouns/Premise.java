package canelhas.languaj.languaj.nouns;

import java.util.function.Predicate;

@FunctionalInterface
public interface Premise< K > extends Functional< K, Boolean >, Predicate< K > {

    @Override default boolean test( K k ) {
        return apply( k );
    }
}
