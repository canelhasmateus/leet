package canelhas.languaj.languaj.nouns;

import java.util.function.Function;

public interface Functional< K, V > extends Function< K, V > {

    @Override default < U > Functional< K, U > andThen( Function< ? super V, ? extends U > after ) {
        return ( K k ) -> after.apply( this.apply( k ) );
    }

    @Override default < U > Functional< U, V > compose( Function< ? super U, ? extends K > before ) {
        return before.andThen( this )::apply;
    }

    @SuppressWarnings( "unchecked" )
    default < F extends Function< K, V >, U > U qualify( Function< F, U > qualifier ) {
        return qualifier.apply( ( F ) this );
    }


}
