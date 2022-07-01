package canelhas.languaj.languaj.nouns;

import java.util.function.BiFunction;

import static br.com.lity.api.common.languaj.adverbs.FunctionalAdverbs.partially;


@FunctionalInterface
public interface BiFunctional< K, U, V > extends BiFunction< K, U, V > {

    default Functional< K, V > bindRight( U secondArgument ) {
        return partially( secondArgument, this );
    }

    default Functional< U, V > bindLeft( K firstArgument ) {
        return partially( this, firstArgument );
    }
}
