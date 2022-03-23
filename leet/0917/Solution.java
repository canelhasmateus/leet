class Solution {


    public static final < T > void compare( T actual, T expected ) {

        if ( !expected.equals( actual ) ) {

            throw new RuntimeException( "Error!\nexpected:\n\t\t" +
                                        expected +
                                        "\ngotten:\n\t\t" +
                                        actual );

        }
    }


    public static final String reverse( String s ) {
        return new StringBuffer( s ).reverse().toString();
    }

    public static boolean isLetter( char i ) {

        return ( i >= 'a' && i <= 'z' ) || ( i >= 'A' && i <= 'Z' );

    }

    public static final String reverseOnly( String s ) {

        int p1 = 0;
        int p2 = s.length() - 1;

        StringBuilder sb = new StringBuilder( s.toString() );

        while ( p1 < p2 ) {

            char left  = sb.charAt( p1 );
            char right = sb.charAt( p2 );

            if ( isLetter( left ) ) {
                if ( isLetter( right ) ) {
                    sb.setCharAt( p1, right );
                    sb.setCharAt( p2, left );
                    p1++;
                    p2--;
                }
                else {
                    p2--;
                }
            }
            else {
                p1++;
            }
        }

        return sb.toString();
    }

    public static void main( String[] args ) {


        compare( reverseOnly( "ab-cd" ), "dc-ba" );
        compare( reverseOnly( "a-bC-dEf-ghIj" ), "j-Ih-gfE-dCba" );
        compare( reverseOnly( "Test1ng-Leet=code-Q!" ), "Qedo1ct-eeLg=ntse-T!" );
    }

    public String reverseOnlyLetters( String s ) {

        return reverseOnly( s );

    }

}