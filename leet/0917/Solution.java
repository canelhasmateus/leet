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
        return new StringBuffer(s).reverse().toString();
    }
    
    public static final String reverseOnly( String s) {
        return reverse( s ) ;
    }
    public static void main( String[] args ) {


        compare(  reverseOnly( "ab-cd" ) , "dc-ba");
        compare(  reverseOnly(  "a-bC-dEf-ghIj" ) , "j-Ih-gfE-dCba");

    }
    
    
    
    public String reverseOnlyLetters( String s ) {
        
        return reverseOnly( s ); 
        
    }
}