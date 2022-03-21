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

    public static final int countPalidromes( String source, int left, int right ) {

        int length = source.length();
        int res    = 0;

        while ( left >= 0 && right < length ) {

            System.out.println( source.substring( left , right + 1 ));
            if ( source.charAt( left ) == source.charAt( right ) ) {
                res += 1;
                left -= 1;
                right += 1;
            }
            else {
                break;
            }

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
                results.add( s.substring( i, j + 1 ) );
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

    public static final int fastPalidromicSubstrings( String s ) {


        int res = 0;
        int length = s.length();
        for ( int i = 0; i < length; i++ ) {

            res += countPalidromes( s, i, i );
            res += countPalidromes( s, i, i + 1);

        }
        return res;
    }


    public static void main( String[] args ) {

        compare( palidromicSubstring( "abc" ).size(), 3 );
        compare( palidromicSubstring( "aaa" ).size(), 6 );
        compare( palidromicSubstring( "aba" ).size(), 4 );

        compare( fastPalidromicSubstrings( "abc" ), 3 );
        System.out.println();
        compare( fastPalidromicSubstrings( "aaa" ), 6 );
        System.out.println();
        compare( fastPalidromicSubstrings( "aba" ), 4 );



    }


    public int countSubstrings( String s ) {

        return fastPalidromicSubstrings( s );
    }


//    We explore the fact that the 'central' part of a palindrome is also a palindrome.
//    ( Explore the compositional structure )
//    Thinking in terms of the 'reachability' matrix, to be an palindrome, an entry need to be  'near' a known palidrome.
//    SO we just 'propagate' the 'palindromeness', starting from the smallest known palidrome 'seeds' ( sort of a terminal case ), which is a single character
//    So, we only need to navigate through this 'known' path. The trick is the way in which we do that:
//    If we checked one at the left, and then one at the right of our starting entry, we would end up counting some palidromes twice:
//        Ex: Starting at 00, we would check 01 to the right; Then, at the next iteration at 11, we would check at the top which is 01 again.
//    To circunvent this problem, we propagate  only through the diagonal to the upper right.
//    Then, to make sure we cover the entire matrix, we manually propagate from the entry to the right ( still through the diagonal).
//    Since a matrix can be fully covered from going along its 'even' and 'odd' diagonals, we can be sure it will be fully covered.
//    Since a matrix diagonals are not overlapping, we can be sure we wont count twice.



}