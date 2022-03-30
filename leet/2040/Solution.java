import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

class Solution {

    public static final < T > void compare( T actual, T expected ) {

        if ( !expected.equals( actual ) ) {

            throw new RuntimeException( "Error!\nexpected:\n\t\t" +
                                        expected +
                                        "\ngotten:\n\t\t" +
                                        actual );

        }
    }


    public long kthSmallestProduct( int[] nums1, int[] nums2, long k ) {

        return skthSmallestProduct( nums1, nums2, k );
    }

    public static long skthSmallestProduct( int[] nums1, int[] nums2, long k ) {

        List< Long > res = new ArrayList<>();

        for ( int i = 0; i < nums1.length; i++ ) {
            for ( int j = 0; j < nums2.length; j++ ) {
                res.add( ( long ) ( nums1[ i ] * nums2[ j ] ) );
            }
        }

        List< Long > longs = res.stream().sorted( Comparator.naturalOrder() ).toList();
        return longs.get( ( int ) ( k - 1 ) );
    }

    public static void main( String[] args ) {

        {
            int[] a = { 2, 5 };
            int[] b = { 3, 4 };
            long  k = 2;

            compare( skthSmallestProduct( a, b, k ), 8L );
        }
        {
            int[] a = { -4, -2, 0, 3 };
            int[] b = { 2, 4 };
            long  k = 6;

            compare( skthSmallestProduct( a, b, k ), 0L );
        }
        {
            int[] a = { -2, -1, 0, 1, 2 };
            int[] b = { -3, -1, 2, 4, 5 };
            long  k = 3;

            compare( skthSmallestProduct( a, b, k ), -6L );
        }
        {
            int[] a = { -100000, 100000 };
            int[] b = { -100000, 100000 };
            long  k = 1;

            compare( skthSmallestProduct( a, b, k ), -10000000000L );
        }

    }
}