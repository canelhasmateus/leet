package canelhas.languaj.languaj.verbs;

import java.util.Optional;

import static canelhas.languaj.languaj.adverbs.ConversionAdverbs.logicallyNot;

public class OptionalVerbs {
    //endregion
    //endregion
    public static < T extends Enum< T > > Optional< T > maybe( Class< T > enumeration, String name ) {

        try {

            return Optional.of( Enum.valueOf( enumeration, name ) );

        }

        catch ( Exception e ) {

            return Optional.empty();
        }
    }

    public static < K > Optional< K > maybe( K input ) {
        return Optional.ofNullable( input );
    }

    public static Optional< String > maybe( String input ) {
        return Optional.ofNullable( input )
                       .filter( logicallyNot( ""::equals ) );
    }
}
