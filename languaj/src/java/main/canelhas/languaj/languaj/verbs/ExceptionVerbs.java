package canelhas.languaj.languaj.verbs;

import canelhas.languaj.languaj.nouns.Conditional;

import java.util.Optional;
import java.util.function.Supplier;

public class ExceptionVerbs {

    public static < X extends RuntimeException > Conditional< Void > raise( Supplier< X > supplier ) throws X {
        return ( Boolean condition ) -> {
            if ( Boolean.TRUE.equals( condition ) ) {
                throw supplier.get();
            }
            else {
                return Optional.empty();
            }
        };
    }

    public static < K > Optional< K > hope( Supplier< K > sup ) {

        try {
            return Optional.ofNullable( sup.get() );
        }
        catch ( Exception e ) {
            return Optional.empty();
        }
    }


}
