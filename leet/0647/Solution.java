import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

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
        return new StringBuilder( s ).reverse().toString();
    }

    public static final List< String > generativePalindrome( String source, int l, int r ) {

        int                 length = source.length();
        ArrayList< String > res    = new ArrayList<>();

        if ( length == 0 || l < 0 || r >= length ) {
            return res;
        }

        String seed = source.substring( l, r + 1 );

        if ( isPalidrome( seed ) ) {
            List< String > leftFruits = generativePalindrome( source, l - 1, r );
            res.add( seed );
            res.addAll( leftFruits );

        }

        return res;

    }

    public static final boolean isPalidrome( String s ) {
        return s.length() > 0 && s.equals( reverse( s ) );
    }

    public static final List< String > substrings( String s ) {

        ArrayList< String > results = new ArrayList<>();

        for ( int i = 0; i < s.length(); i++ ) {
            for ( int j = i; j < s.length(); j++ ) {
                results.add( s.substring( i , j + 1 ) );
            }


        }

        return results;

    }

    public static final List< String > palidromicSubstring( String s ) {

        return substrings( s )
                .stream()
                .filter( Solution::isPalidrome )
                .collect( Collectors.toList() );
    }
    public static final List< String > fastPalidromicSubstrings( String s ) {

        List< String > o = new ArrayList<>();

        int length = s.length();
        for ( int i = 0; i < length; i++ ) {

            List< String > fruits = generativePalindrome( s, i, i );
            o.addAll( fruits );

        }
        return o;
    }


    public static void main( String[] args ) {

        compare( palidromicSubstring( "abc" ).size(), 3 );

        compare( palidromicSubstring( "aaa" ).size(), 6 );

        compare( palidromicSubstring( "aba" ).size(), 4);

    }


    public int countSubstrings( String s ) {

        return palidromicSubstring( s ).size();
    }
}