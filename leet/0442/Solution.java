import java.util.*;

class Solution {
    public static final < T > void compare( T actual, T expected ) {

        if ( !expected.equals( actual ) ) {

            throw new RuntimeException( "Error!\nexpected:\n\t\t" +
                                        expected +
                                        "\ngotten:\n\t\t" +
                                        actual );

        }
    }

    public List< Integer > findDuplicates( int[] nums ) {
        return sfindDuplicates( nums );
    }

    public static List< Integer > sfindDuplicates( int[] nums ) {

        List< Integer > result = new ArrayList<>();

        for ( int num : nums ) {

            int idx = Math.abs( num ) - 1;

            if ( nums[ idx ] < 0 ) {
                result.add( idx + 1 );
            }

            nums[idx] *= -1;


        }

        return result;
    }


    public static void main( String[] args ) {
        {
            int[] a   = { 4, 3, 2, 7, 8, 2, 3, 1 };
            int[] res = { 2, 3 };
            compare( sfindDuplicates( a ), Arrays.stream( res ).boxed().toList() );
        }
        {
            int[] a   = { 1, 1, 2 };
            int[] res = { 1 };
            compare( sfindDuplicates( a ), Arrays.stream( res ).boxed().toList() );
        }
        {
            int[] a   = { 1 };
            int[] res = {};
            compare( sfindDuplicates( a ), Arrays.stream( res ).boxed().toList() );
        }
    }


}
