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


    public static int sminCharacters( String a, String b ) {


        var first  = a.length() > b.length() ? 9999 : 0;
        var second = b.length() > a.length() ? 9999 : 0;
        var third  = a.length() > b.length() + 1 ? 9999 : 0;

        for ( int i = 0; i < Math.min( a.length(), b.length() ); i++ ) {

            char characterA = a.charAt( i );
            char characterB = b.charAt( i );

            if ( characterA <= characterB ) {
                first++;
            }

            if ( characterB <= characterA ) {
                second++;
            }

            if ( characterB != characterA) {
                third++;
                if ( third > 1 ) {
                    third = 9999;
                }

            }

        }

        return Stream.of( first, second, third )
                     .min( Integer::compareTo )
                     .orElse( 0 );
    }

    public int minCharacters(String a, String b) {
        return Solution.sminCharacters( a, b );
    }

    public static void main( String[] args ) {

        compare( sminCharacters( "aba", "caa" ), 2 );
        compare( sminCharacters( "dabadd", "cda" ), 2 );


    }

}