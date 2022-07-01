package canelhas.languaj.languaj.nouns;

import java.util.function.BiFunction;
import java.util.function.Function;


// Shamelessly copied / adapted from https://gist.github.com/mathieuancelin/bb30a104c17037e34f0b
// Credits to @mathieuancelin

public class Lens< K, V > {

    private final Function< K, V >      getter;
    private final BiFunction< K, V, K > setter;

    //region constructor
    private Lens( Function< K, V > getter, BiFunction< K, V, K > setter ) {
        this.getter = getter;
        this.setter = setter;
    }

    public static < A, B > Lens< A, B > of( Function< A, B > getter, BiFunction< A, B, A > setter ) {
        return new Lens<>( getter, setter );
    }
    //endregion

    public V get( K target ) {
        return getter.apply( target );
    }

    public Functional< V, K > set( K target ) {
        return ( V v ) -> over( __ -> v ).apply( target );
    }

    public Functional< K, K > over( Function< V, V > mapper ) {
        return ( obj ) -> {
            V transformed = getter.andThen( mapper ).apply( obj );
            return set( obj ).apply( transformed );
        };
    }

    public < U > Lens< K, U > through( Lens< V, U > other ) {
        return new Lens<>(
                ( K a ) -> other.getter.apply( getter.apply( a ) ),
                ( K a, U u ) -> {
                    V b    = getter.apply( a );
                    V newB = other.over( __ -> u ).apply( b );
                    return setter.apply( a, newB );
                }
        );
    }
}