import java.util.Arrays;

public class Solution {

    public static void main( String[] args ) {


        assert Arrays.equals( getMaximumXor( new int[]{ 0, 1, 1, 3 }, 2 ),
                              new int[]{ 0, 3, 2, 3 } );
        assert Arrays.equals( getMaximumXor( new int[]{ 2, 3, 4, 7 }, 3 ),
                              new int[]{ 5, 2, 6, 5 } );
        assert Arrays.equals( getMaximumXor( new int[]{ 0, 1, 2, 2, 5, 7 }, 3 ),

                              new int[]{ 4, 3, 6, 4, 6, 7 } );

    }

    public static int[] getMaximumXor( int[] nums, int maximumBit ) {

        final var length  = nums.length;
        final var result  = new int[ length ];
        final var extrema = ( 1 << maximumBit ) - 1;

        var total_xor = 0;

        for ( int i = 0; i < nums.length; i++ ) {
            final var element = nums[ i ];
            total_xor = total_xor ^ element;
            result[ length - i - 1 ] = extrema - total_xor;
        }

        return result;

    }

}