package canelhas.languaj.languaj.nouns;

import java.util.function.Function;

public class Pipe< K > {

    private final K value;

    public Pipe( K obj ) {
        this.value = obj;
    }

    public static < T > Pipe< T > of( T obj ) {
        return new Pipe<>( obj );
    }

    public Pipe< K > through( Function< K, ? > action ) {
        action.apply( this.value );
        return this;
    }
}
