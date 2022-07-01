package canelhas.languaj.languaj.nouns;

import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

public class Validation< X extends RuntimeException > {

    private final Function< String, X > messageReceiver;
    private       List< Exception >     errors;

    private Validation( Function< String, X > receiver ) {
        this.messageReceiver = receiver;
    }

    public static < E extends RuntimeException > Validation< E > of( Function< String, E > messageReceiver ) {
        return new Validation< E >( messageReceiver );
    }

    public < K, V > V check( K element, Function< K, V > action ) {

        try {
            return action.apply( element );
        }
        catch ( Exception e ) {
            if ( errors == null ) {
                errors = new ArrayList<>();
            }
            errors.add( e );
            return null;
        }
    }

    @SuppressWarnings( "OptionalUsedAsFieldOrParameterType" )
    public < K, V > Optional< V > check( Optional< K > element, Function< K, V > action ) {

        try {
            return element.map( action );
        }
        catch ( Exception e ) {
            if ( errors == null ) {
                errors = new ArrayList<>();
            }
            errors.add( e );
            return Optional.empty();
        }
    }


    public void verify( ) {

        if ( errors != null && !errors.isEmpty() ) {

            var message = errors.stream()
                                .map( Exception::getMessage )
                                .filter( Objects::nonNull )
                                .sorted( Comparator.comparing( String::length ) )
                                .collect( Collectors.joining( " \n " ) );

            throw messageReceiver.apply( message );
        }


    }
}