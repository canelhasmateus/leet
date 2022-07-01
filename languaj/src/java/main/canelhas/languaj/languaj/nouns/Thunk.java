package canelhas.languaj.languaj.nouns;

import java.util.function.Function;
import java.util.function.Supplier;

@FunctionalInterface
public interface Thunk< K > extends Functional< Void, K >, Supplier< K > {

    @Override default K get( ) {
        return apply( null );
    }


    @Override default < V > Thunk< V > andThen( Function< ? super K, ? extends V > after ) {

        return ( Void v ) -> after.apply( this.get() );
    }


}
