import java.io.Serializable;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

class Scratch {

    public static final < T > void compare( T actual, T expected ) {

        if ( !expected.equals( actual ) ) {

            throw new RuntimeException( "Error!\nexpected:\n\t\t" +
                                        expected +
                                        "\ngotten:\n\t\t" +
                                        actual );

        }
    }

    public static final String reverse( String s ) {
        return new StringBuilder( s ).reverse().toString();
    }

    public static final boolean isPalidrome( String s ) {
        return s.length() > 0 && s.equals( reverse( s ) );
    }

    public static final List< String > substrings( String s ) {

        int            length = s.length();
        List< String > res    = new ArrayList<>();
        for ( int i = 0; i < length; i++ ) {

            for ( int j = i; j < length; j++ ) {

                String substring = s.substring( i, j + 1 );
                res.add( substring );

            }

        }

        return res;

    }

    public static final List< String > palidromicSubstring( String s ) {

        return substrings( s )
                .stream()
                .filter( Scratch::isPalidrome )
                .toList();
    }

    public static void main( String[] args ) {

        compare( palidromicSubstring( "abc" ),
                 List.of( "a", "b", "c" )
               );

        compare( palidromicSubstring( "aaa" ).stream().sorted().toList(),
                 List.of( "a",
                          "a",
                          "a",
                          "aa",
                          "aa",
                          "aaa"
                        ).stream().toList().stream().sorted().toList()
               );


    }
}