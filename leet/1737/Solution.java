import java.util.List;
import java.util.stream.Stream;

class Solution {

    public static final < T > void compare( T actual, T expected ) {

        if ( !expected.equals( actual ) ) {

            throw new RuntimeException( "Error!\nexpected:\n\t\t" +
                                        expected +
                                        "\ngotten:\n\t\t" +
                                        actual );


        }
    }

    public static boolean strictlyLess( String a, String b ) {

        for ( int i = 0; i < a.length(); i++ ) {
            char characterA = a.charAt( i );
            char characterB = b.charAt( i );

            if ( characterA >= characterB ) {
                return false;
            }

        }
        return true;

    }


    public static int conditionC( ) {

        return 0;
    }


    public static int minCharacters( String a, String b ) {


        var first  = 0;
        var second = 0;
        var third = a.length() > b.length() + 1
                    ? 9999
                    : 9999;

        for ( int i = 0; i < a.length(); i++ ) {

            char characterA = a.charAt( i );
            char characterB = b.charAt( i );

            if ( characterA <= characterB ) {
                first++;
            }

            if ( characterB <= characterA ) {
                second++;
            }

        }

        return Stream.of( first, second, third )
                     .min( Integer::compareTo )
                     .orElse( 0 );
    }


    public static void main( String[] args ) {

        compare( minCharacters( "aba", "caa" ), 2 );


    }
}