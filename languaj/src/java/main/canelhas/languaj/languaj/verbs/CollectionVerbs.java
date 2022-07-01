package canelhas.languaj.languaj.verbs;


import canelhas.languaj.languaj.nouns.Functional;
import canelhas.languaj.languaj.nouns.Searcher;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;

import static canelhas.languaj.languaj.adverbs.CollectionAdverbs.collectively;
import static java.util.function.Function.identity;

public class CollectionVerbs {
    public static < T > BiFunction< Collection< T >, Collection< T >, List< T > > mergeWith( Function< T, Object > keyExtractor ) {

        return ( Collection< T > base, Collection< T > merger ) -> {

            final Map< Object, T > mergerMap = toDictWith( keyExtractor ).apply( merger );

            final Functional< T, T > replaceIfExists = e -> {
                final Object key = keyExtractor.apply( e );
                return mergerMap.getOrDefault( key, e );
            };

            return collectively( replaceIfExists ).apply( base );

        };

    }

    public static < T > Predicate< T > seenWith( Function< T, ? > keyExtractor ) {
        final Set< Object > seen = ConcurrentHashMap.newKeySet();
        return ( T t ) -> seen.add( keyExtractor.apply( t ) );
    }

    public static < T, K > Function< Collection< T >, Map< K, T > > toDictWith( Function< T, K > keyExtractor ) {

        return toDictWith( keyExtractor, identity() );
    }

    private static < T, K, V > Function< Collection< T >, Map< K, V > > toDictWith( Function< T, K > keyExtractor, Function< T, V > valueExtractor ) {
        return list -> list.stream()
                           .collect( Collectors.toMap( keyExtractor,
                                                       valueExtractor,
                                                       ( a, b ) -> a )
                                   );
    }

    public static < K, V > Searcher< K, V > toSearcher( Map< K, V > existingDict ) {

        return ( K k ) -> Optional.ofNullable( existingDict.get( k ) );

    }
}
