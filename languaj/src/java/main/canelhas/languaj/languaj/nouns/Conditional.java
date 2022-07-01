package canelhas.languaj.languaj.nouns;

import java.util.Optional;

public interface Conditional< K > extends Functional< Boolean, Optional< K > > {

    default Optional< K > when( Boolean b ) {
        return apply( b );
    }

    default Optional< K > whenEquals( Object a, Object b ) {
        return when( a.equals( b ) );
    }

    default Optional< K > whenNotEquals( Object a, Object b ) {
        return when( !a.equals( b ) );
    }

}
