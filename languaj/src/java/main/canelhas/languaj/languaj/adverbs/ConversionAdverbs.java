package canelhas.languaj.languaj.adverbs;


import canelhas.languaj.languaj.nouns.Arrow;
import canelhas.languaj.languaj.nouns.Effect;
import canelhas.languaj.languaj.nouns.Premise;
import canelhas.languaj.languaj.nouns.Thunk;

import java.util.function.*;

public class ConversionAdverbs {
    public static < K > Arrow< K > fluently( Consumer< K > con ) {
        return ( K k ) -> {
            con.accept( k );
            return k;
        };
    }

    //region functionally
    public static < K > Premise< K > functionally( Predicate< K > predicate ) {
        return predicate::test;
    }

    public static < K > Effect< K > functionally( Consumer< K > consumer ) {
        return ( K k ) -> {
            consumer.accept( k );
            return null;
        };
    }

    public static < K > Arrow< K > functionally( UnaryOperator< K > operator ) {
        return operator::apply;
    }

    public static < V > Thunk< V > functionally( Supplier< V > supplier ) {
        return ( Void v ) -> supplier.get();
    }

    public static < K > Premise< K > logically( Function< K, Boolean > predicate ) {
        return predicate::apply;
    }

    public static < K > Premise< K > logicallyNot( Function< K, Boolean > predicate ) {
        return Predicate.not( logically( predicate ) )::test;
    }
}
