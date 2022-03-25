import java.util.Arrays;

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

        int[] freqsA = letterFreq( a );
        int[] freqsB = letterFreq( b );

        int[] cumSumA = prefixSum( freqsA );
        int[] cumSumB = prefixSum( freqsB );


        var res = a.length() + b.length()
                  - Arrays.stream( freqsA ).max().orElse( 0 )
                  - Arrays.stream( freqsB ).max().orElse( 0 );

        for ( int i = 0; i < 25; i++ ) {

            res = Math.min( res, a.length() - cumSumA[ i ] + cumSumB[ i ] );

            res = Math.min( res, b.length() - cumSumB[ i ] + cumSumA[ i ] );
        }

        return res;

    }

    public static int[] prefixSum( int[] freq ) {
        int[] rest = Arrays.copyOf( freq, freq.length );
        for ( int i = 1; i < rest.length; i++ ) {
            rest[ i ] = rest[ i ] + rest[ i - 1 ];
        }
        return rest;

    }

    public static int[] letterFreq( String a ) {
        int[] res = new int[ 26 ];

        for ( int i = 0; i < a.length(); i++ ) {
            char character = a.charAt( i );
            var  idx       = character - 'a';
            res[ idx ] += 1;
        }

        return res;


    }

    public int minCharacters( String a, String b ) {
        return Solution.sminCharacters( a, b );
    }

    public static void main( String[] args ) {

        compare( sminCharacters( "aba", "caa" ), 2 );
        compare( sminCharacters( "dabadd", "cda" ), 3 );


    }

}