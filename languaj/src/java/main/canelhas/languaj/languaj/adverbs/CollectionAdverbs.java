package canelhas.languaj.languaj.adverbs;


import canelhas.languaj.languaj.nouns.Functional;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Collectors;

import static canelhas.languaj.languaj.adverbs.ConversionAdverbs.logically;


public class CollectionAdverbs {
    public static < K, V > Functional< K, List< V > > associativelly( Function< K, V >... functions ) {
        var result = new ArrayList< V >();

        return ( K k ) -> {
            for ( Function< K, V > function : functions ) {
                result.add( function.apply( k ) );
            }
            return result;
        };
    }

    //region collections
    public static < K, V > Functional< Collection< K >, List< V > > collectively( Function< K, V > action ) {
        return ( Collection< K > iterable ) -> {

            final var result = new ArrayList< V >( iterable.size() );

            for ( K element : iterable ) {
                result.add( action.apply( element ) );
            }

            return result;
        };

    }

    public static < K, V > Functional< List< K >, List< V > > concurrently( Function< K, V > action ) {
        return ( List< K > collection ) -> collection.stream()
                                                     .parallel()
                                                     .map( action )
                                                     .collect( Collectors.toList() );

    }

    public static < K > Functional< Collection< K >, Collection< K > > narrowingly( Function< K, Boolean > chooser ) {
        return ( Collection< K > collection ) -> collection.stream()
                                                           .filter( logically( chooser ) )
                                                           .collect( Collectors.toList() );
    }
}
